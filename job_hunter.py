import requests
import json
import os
import csv
from datetime import datetime

from sources.workwithindies import get_jobs

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]


def send_telegram(message):
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={
            "chat_id": CHAT_ID,
            "text": message
        }
    )


def load_seen():

    if not os.path.exists("seen_jobs.json"):
        return []

    try:
        with open("seen_jobs.json", "r") as f:
            return json.load(f)

    except:
        return []
def save_seen(data):
    with open("seen_jobs.json", "w") as f:
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

jobs = get_jobs()

for job in jobs:

    job_id = f"{job['source']}:{job['title']}"

    if job_id not in seen:

        seen.append(job_id)

        save_seen(seen)

        save_job(
            job["title"],
            job["source"],
            job["url"]
        )

        send_telegram(
            f"""🚨 NEW GAME DEV JOB

Role: {job['title']}
Source: {job['source']}

{job['url']}
"""
        )