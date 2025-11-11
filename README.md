TikTok Comment Scraper

A simple Python tool that extracts all public comments from any TikTok video using its video link or video ID.
This script works without needing an API key and prints comments directly to your terminal.

--------------------------------------------------

Features:

- Accepts TikTok URL or direct video ID
- Automatically resolves short URLs (vt.tiktok.com, vm.tiktok.com)
- Scrapes comments in batches
- Handles errors safely
- Works on Windows / Linux / Mac

--------------------------------------------------

Requirements:

- Python 3.7+
- requests library

Install requirements:

pip install requests

--------------------------------------------------

Usage:

Run the script:

python main.py

You will be asked to enter a TikTok link or ID:

[?] TikTok link > https://www.tiktok.com/@user/video/{ID}

or just:

[?] TikTok link > 7302154645734984992

The scraper will start printing comments:

Nice video!
Haha this is funny 😂
I love this!

--------------------------------------------------

How It Works:

- Detects if input is a full TikTok URL or only the video ID
- Extracts the aweme_id used internally by TikTok
- Requests comment data using TikTok’s web API endpoint
- Loops through pages until no more comments are found

--------------------------------------------------

Disclaimer:

This tool is for educational and research purposes only.
Do not use it for violating TikTok's Terms of Service or scraping private data.

--------------------------------------------------

Contact:

If you want improvements (CSV export, GUI, proxy support, async speed boost), feel free to open an issue or message.

--------------------------------------------------

Support:

If you like this project, consider giving it a star on GitHub!
