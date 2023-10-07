import requests
import time
import os

tokens =  [
    "token",
]

ids = [
    1,
]

# Seperate with commas (people genuinely don't understand this)

def startup():
    os.system("cls")
    print("Beginning autotyper")

def update(start_time):
    program_time = time.time() - start_time
    hours = int(program_time // 3600)
    minutes = int((program_time % 3600) // 60)
    seconds = int(program_time % 60)
    os.system(f"title Discord Autotyper - Duration: {hours}:{minutes}:{seconds}")

def main():
    startup()
    start_time = time.time()
    while True:
        update(start_time)
        for id in ids:
            for token in tokens:
                headers = {"authorization" : token}
                endpoint = f"https://discord.com/api/v9/channels/{id}/typing"
                res = requests.post(endpoint, headers=headers)
                if res.status_code == 204:
                    print(f"Sent typing request to {id} under {token[:5]}")
                else:
                    print(f"Failed to type in {id} under {token[:5]}")
        time.sleep(1)

main()
