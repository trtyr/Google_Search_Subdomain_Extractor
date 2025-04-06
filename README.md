# Google Search Subdomain Extractor

[English](README_EN.md) | 简体中文

## 项目介绍

这是一个用于从 Google 搜索结果中提取子域名的工具。它由一个油猴脚本和一个 Python 服务器组成，能够自动从 Google 搜索结果中提取并保存子域名。

## 安装说明

### 安装 Python 服务器

1. 确保你已安装 Python 3.x
2. 安装所需依赖：

   ```bash
   pip install flask flask-cors colorama waitress
   ```

3. 运行服务器：

   ```bash
   python subdomain_server.py
   ```

### 安装油猴脚本

1. 首先安装[Tampermonkey](https://www.tampermonkey.net/)浏览器扩展
2. 从 GreasyFork 安装（推荐）：

   - 访问[脚本安装页面](https://greasyfork.org/scripts/531972)，点击「安装」按钮

   或者手动安装：

   - 点击 Tampermonkey 图标，选择「添加新脚本」
   - 将`tampermonkey.js`中的内容复制到编辑器中
   - 保存脚本

## 使用方法

1. 启动 Python 服务器（默认监听在 http://127.0.0.1:5123）
2. 在 Google 中使用 site 语法搜索目标域名，例如：

   ```
   site:*.example.com
   ```

3. 脚本会自动运行并在控制台中显示提取到的子域名
4. 提取的子域名会自动保存到`collected_subdomains.txt`文件中

## 使用截图

浏览器截图：

<img src="images\6dffb9e4de72338ef0be3bbfbcb608b3.png" width="700px">

Python 服务器截图

<img src="images\5af63fcda7138641c4b04a434aa898db.png">

文件截图：

<img src="images\7f506d9ca02adb5448edacf23d229eda.png" width="200px">

## 许可证

本项目采用 GNU General Public License v3.0 许可证 - 查看[LICENSE](LICENSE)文件了解更多详情。
