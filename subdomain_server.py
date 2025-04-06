import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import colorama
from colorama import Fore, Style, Back
from waitress import serve

app = Flask(__name__)
CORS(app, resources={r"/save_subdomains": {"origins": "https://*.google.com"}})

colorama.init(autoreset=True)

SAVE_FILE = "collected_subdomains.txt"
SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5123

saved_hostnames = set()

def print_info(message):
    print(f"{Fore.CYAN}[*]{Style.RESET_ALL} {message}")

def print_success(message):
    print(f"{Fore.GREEN}[+]{Style.RESET_ALL} {message}")

def print_error(message):
    print(f"{Fore.RED}[-]{Style.RESET_ALL} {message}")

def print_warn(message):
    print(f"{Fore.YELLOW}[!]{Style.RESET_ALL} {message}")

def load_hostnames():
    if os.path.exists(SAVE_FILE):
        try:
            with open(SAVE_FILE, 'r', encoding='utf-8') as f:
                for line in f:
                    hostname = line.strip()
                    if hostname:
                        saved_hostnames.add(hostname)
            print_info(f"Loaded {Fore.YELLOW}{len(saved_hostnames)}{Style.RESET_ALL} existing hostnames from '{Fore.MAGENTA}{SAVE_FILE}{Style.RESET_ALL}'.")
        except Exception as e:
            print_error(f"Error loading hostnames from '{Fore.MAGENTA}{SAVE_FILE}{Style.RESET_ALL}': {e}")
    else:
        print_warn(f"Save file '{Fore.MAGENTA}{SAVE_FILE}{Style.RESET_ALL}' not found. Starting fresh.")

@app.route('/save_subdomains', methods=['POST'])
def save_subdomains():
    if not request.is_json:
        print_warn("Received non-JSON request.")
        return jsonify({"status": "error", "message": "Request must be JSON"}), 400

    data = request.get_json()
    incoming_hostnames = data.get('hostnames')

    if not isinstance(incoming_hostnames, list):
        print_warn("Invalid data format: 'hostnames' key missing or not a list.")
        return jsonify({"status": "error", "message": "'hostnames' must be a list"}), 400

    newly_added_count = 0
    print(f"\n{Back.BLUE}{Fore.WHITE}--- Received Request ---{Style.RESET_ALL}")
    print_info(f"Received {Fore.YELLOW}{len(incoming_hostnames)}{Style.RESET_ALL} hostnames from client.")

    added_list = []
    try:
        with open(SAVE_FILE, 'a+', encoding='utf-8') as f:
             for hostname in incoming_hostnames:
                hostname = str(hostname).strip().lower()
                if hostname and hostname not in saved_hostnames:
                    saved_hostnames.add(hostname)
                    f.write(hostname + '\n')
                    newly_added_count += 1
                    added_list.append(hostname)

        if newly_added_count > 0:
            for added_host in added_list:
                 print(f"  {Fore.GREEN}[+]{Style.RESET_ALL} Added new: {Fore.WHITE}{added_host}{Style.RESET_ALL}")
            print_success(f"Added {Fore.YELLOW}{newly_added_count}{Style.RESET_ALL} new hostnames.")
        else:
            print_info("No new hostnames added in this batch.")

        print_info(f"Total unique hostnames stored: {Fore.YELLOW}{len(saved_hostnames)}{Style.RESET_ALL}")
        print(f"{Back.BLUE}{Fore.WHITE}------------------------{Style.RESET_ALL}")

        return jsonify({
            "status": "success",
            "received": len(incoming_hostnames),
            "newly_added": newly_added_count,
            "total_saved": len(saved_hostnames)
        }), 200

    except Exception as e:
        print_error(f"Error processing or saving hostnames: {e}")
        return jsonify({"status": "error", "message": "Internal server error"}), 500

if __name__ == '__main__':
    load_hostnames()
    print_info(f"Starting Waitress server at {Fore.GREEN}http://{SERVER_HOST}:{SERVER_PORT}{Style.RESET_ALL}")
    print_info(f"Ready to receive subdomains at {Fore.YELLOW}/save_subdomains{Style.RESET_ALL}")
    print_info(f"Save file: {Fore.MAGENTA}{os.path.abspath(SAVE_FILE)}{Style.RESET_ALL}")
    print_info("Press CTRL+C to stop.")
    serve(app, host=SERVER_HOST, port=SERVER_PORT, threads=4)