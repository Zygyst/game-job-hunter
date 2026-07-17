from sources.arc import get_jobs

jobs = get_jobs()

print("Found:", len(jobs))

for job in jobs:
    print(job)