import requests
from bs4 import BeautifulSoup


def get_jobs():

    response = requests.get(
        "https://hitmarker.net/jobs",
        headers={"User-Agent": "Mozilla/5.0"}
    )

    print("Status:", response.status_code)

    with open("hitmarker.html", "w", encoding="utf-8") as f:
        f.write(response.text)

    print("Saved HTML")

    jobs = []

    if response.status_code != 200:
        print("Hitmarker status:", response.status_code)
        return jobs

    soup = BeautifulSoup(response.text, "html.parser")

    keywords = [
        "godot",
        "roblox",
        "unreal",
        "ue5",
        "gameplay",
        "programmer",
        "developer"
    ]

    text = soup.get_text("\n")

    seen = set()

    for line in text.split("\n"):

        line = line.strip()

        if len(line) < 10:
            continue

        if len(line) > 80:
            continue

        lower = line.lower()

        if any(k in lower for k in keywords):

            if line not in seen:

                seen.add(line)

                jobs.append({
                    "title": line,
                    "source": "Hitmarker",
                    "url": "https://hitmarker.net/jobs"
                })

    return jobs