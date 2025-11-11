import os
import requests
import shutil

print("TikTok Comment Scraper".center(shutil.get_terminal_size().columns))
print('\n')

video_link = input('          [?] TikTok link > ').strip()

# ✅ CASE 1: User enters a real link
if "tiktok.com" in video_link:
    try:
        # Handle short links
        if "vm.tiktok.com" in video_link or "vt.tiktok.com" in video_link:
            video_link = requests.head(video_link, allow_redirects=True, timeout=5).url

        parts = video_link.split("/")
        # Find the aweme ID anywhere in the URL
        videoid = next((p for p in parts if p.isdigit()), None)

        if not videoid:
            raise ValueError("Cannot extract video ID.")

    except Exception as e:
        print("Invalid TikTok link:", e)
        exit()

# ✅ CASE 2: User enters only the ID
elif video_link.isdigit():
    videoid = video_link

# ❌ Invalid input
else:
    print("Invalid TikTok ID or URL.")
    exit()


t = 0
comm_num = 0

while True:
    try:
        headers = {
            'user-agent': 'Mozilla/5.0',
            'referer': f'https://www.tiktok.com/@x/video/{videoid}',
        }

        response = requests.get(
            f"https://www.tiktok.com/api/comment/list/?aid=1988&aweme_id={videoid}&count=50&cursor={t}",
            headers=headers
        )
        response.raise_for_status()

        data = response.json()
        comments = data.get("comments", [])

        if not comments:
            print("No more comments.")
            break

        for comment in comments:
            print(comment["text"])
            comm_num += 1

        t += 50

    except Exception as e:
        print("Error:", e)
        break

print(f"\nTotal comments scraped: {comm_num}")
