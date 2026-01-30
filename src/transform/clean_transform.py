import json
import re
import os
import sys

# Fix import path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(BASE_DIR)

from utils.sentiment import get_sentiment


def clean_text(text):
    text = re.sub(r"#\w+", "", text)
    text = re.sub(r"@\w+", "", text)
    text = re.sub(r"\s+", " ", text)
    text = text.encode("ascii", "ignore").decode()
    return text.strip()


def transform(raw_file):
    with open(raw_file, "r") as f:
        data = json.load(f)

    processed = []
    for post in data:
        caption = clean_text(post.get("caption", ""))
        sentiment = get_sentiment(caption)

        processed.append({
            "caption": caption,
            "sentiment": sentiment,
            "likes": post.get("likes", 0),
            "image_url": post.get("image_url", ""),
            "timestamp": post.get("timestamp", ""),
            "hashtags": post.get("hashtags", [])
        })

    # Output folder
    processed_dir = os.path.join(BASE_DIR, "data", "processed")
    os.makedirs(processed_dir, exist_ok=True)

    out_file = raw_file.replace("raw", "processed")

    with open(out_file, "w") as f:
        json.dump(processed, f, indent=4)

    print(f"✅ Transformed → {out_file}")
    return out_file


if __name__ == "__main__":
    print("🔧 Please run transform() from Python shell by passing the raw file path.")
