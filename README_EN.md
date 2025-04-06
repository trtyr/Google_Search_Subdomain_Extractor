# Google Search Subdomain Extractor

English | [简体中文](README.md)

## Introduction

This is a tool for extracting subdomains from Google search results. It consists of a Tampermonkey script and a Python server that work together to automatically extract and save subdomains from Google search results.

## Installation

### 1. Install Python Server

1. Ensure Python 3.x is installed
2. Install required dependencies:

   ```bash
   pip install flask flask-cors colorama waitress
   ```

3. Run the server:

   ```bash
   python subdomain_server.py
   ```

### 2. Install Tampermonkey Script

1. First install the [Tampermonkey](https://www.tampermonkey.net/) browser extension
2. Click on the Tampermonkey icon and select "Add New Script"
3. Copy the contents of `tampermonkey.js` into the editor
4. Save the script

## Usage

1. Start the Python server (default listening on http://127.0.0.1:5123)
2. Use the site syntax in Google to search for target domains, for example:

   ```
   site:*.example.com
   ```

3. The script will automatically run and display extracted subdomains in the console
4. Extracted subdomains are automatically saved to `collected_subdomains.txt`

## Screenshots

Browser Screenshot:

<img src="images\6dffb9e4de72338ef0be3bbfbcb608b3.png" width="700px">

Python Server Screenshot:

<img src="images\5af63fcda7138641c4b04a434aa898db.png">

File Screenshot:

<img src="images\7f506d9ca02adb5448edacf23d229eda.png" width="200px">

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
