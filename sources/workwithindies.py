import requests
from bs4 import BeautifulSoup


def get_jobs():

    response = requests.get(
        "https://www.workwithindies.com/",
        headers={"User-Agent": "Mozilla/5.0"}
    )

    jobs = []

    if response.status_code != 200:
        print("Status:", response.status_code)
        return jobs

    seen_titles = set()

    soup = BeautifulSoup(response.text, "html.parser")

    text = soup.get_text("\n")

    lines = text.split("\n")

    keywords = [
        "godot",
        "roblox",
        "unreal",
        "gameplay",
        "programmer",
        "developer"
    ]

    for line in lines:

        line = line.strip()

        if len(line) < 10:
            continue

        if len(line) > 80:
            continue

        lower = line.lower()

        if any(keyword in lower for keyword in keywords):

            if line not in seen_titles:

                seen_titles.add(line)

                jobs.append({
                    "title": line,
                    "source": "WorkWithIndies",
                    "url": "https://www.workwithindies.com/"
                })

    return jobs