import requests


def get_jobs():

    response = requests.get(
        "https://arc.dev/",
        headers={"User-Agent": "Mozilla/5.0"}
    )

    jobs = []

    if response.status_code != 200:
        print("Arc status:", response.status_code)
        return jobs

    text = response.text.lower()

    keywords = [
        "godot",
        "roblox",
        "unreal",
        "game developer",
        "gameplay"
    ]

    for keyword in keywords:

        if keyword in text:

            jobs.append({
                "title": f"Keyword found: {keyword}",
                "source": "Arc",
                "url": "https://arc.dev/"
            })

    return jobs