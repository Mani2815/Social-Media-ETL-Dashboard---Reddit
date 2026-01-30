import requests
import json
import os
from datetime import datetime
import time

def extract_subreddit(subreddit="dataengineering", limit=20):

    url = f"https://www.reddit.com/r/{subreddit}/top.json?t=day&limit={limit}"

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/120.0.0.0 Safari/537.36"
    }

    # Try 3 times
    for attempt in range(3):
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            try:
                json_data = response.json()
                break
            except:
                print("❌ JSON decode failed, retrying...")
        else:
            print(f"❌ Status: {response.status_code}, retrying...")

        time.sleep(1)

    else:
        print("🔴 Failed after 3 attempts. Reddit blocked the request.")
        return

    # Extract posts
    children = json_data.get("data", {}).get("children", [])

    if not children:
        print("❌ No data received. Possibly rate-limited.")
        return

    results = []
    for item in children:
        post = item["data"]
        results.append({
            "caption": post.get("title", ""),
            "likes": post.get("ups", 0),
            "image_url": post.get("url", ""),
            "timestamp": datetime.fromtimestamp(post["created_utc"]).isoformat(),
            "hashtags": [subreddit]
        })

    # Save to raw folder
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    RAW_DIR = os.path.join(BASE_DIR, "data", "raw")
    os.makedirs(RAW_DIR, exist_ok=True)

    file_path = os.path.join(
        RAW_DIR, f"{subreddit}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    )

    with open(file_path, "w") as f:
        json.dump(results, f, indent=4)

    print(f"✅ Extracted {len(results)} Reddit posts → {file_path}")
    return file_path


if __name__ == "__main__":
    extract_subreddit("dataengineering", limit=20)
