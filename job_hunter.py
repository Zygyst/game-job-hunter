import requests
import json
import os
import csv
from datetime import datetime

BOT_TOKEN = "8922676320:AAHNGNiNlSu0QIt-9UnwVl8TYiqRBsvqsDU"
CHAT_ID = "6610169350"

KEYWORDS = [
    "godot",
    "gdscript",
    "roblox",
    "luau",
    "unreal",
    "game developer",
    "gameplay programmer"
]

def send_telegram(message):
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={
            "chat_id": CHAT_ID,
            "text": message
        }
    )

def load_seen():
    if not os.path.exists("seen_jobs.[]"):
        return []

    with open("seen_jobs.[]", "r") as f:
        return json.load(f)

def save_seen(data):
    with open("seen_jobs.[]", "w") as f:
        json.dump(data, f)

def save_job(title, source, url):
    file_exists = os.path.exists("jobs.csv")

    with open("jobs.csv", "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        if not file_exists:
            writer.writerow(["Date", "Title", "Source", "URL"])

        writer.writerow([
            datetime.now(),
            title,
            source,
            url
        ])

seen = load_seen()

# TEST JOB
job = {
    "title": "Gameplay Programmer",
    "source": "Test Source",
    "url": "https://example.com/job1"
}

job_id = job["url"]

if job_id not in seen:

    seen.append(job_id)

    save_seen(seen)

    save_job(
        job["title"],
        job["source"],
        job["url"]
    )

    send_telegram(
        f"""🚨 NEW JOB

Role: {job['title']}
Source: {job['source']}

{job['url']}
"""
    )