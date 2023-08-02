import requests
import time
import os

tokens =  [
    "token" # seperate with comma
]

ids = [
    1 # seperate with comma
]

def startup():
    os.system("title Autotyper v2")
    os.system("cls")
    print("Beginning autotyper")

def main():
    startup()
    while True:
        for id in ids:
            for token in tokens:
                headers = {"authorization" : token}
                endpoint = f"https://discord.com/api/v9/channels/{id}/typing"
                time.sleep(0.5)
                res = requests.post(endpoint, headers=headers)
                if res.status_code == 204:
                    print(f"Sent typing request to {id} under {token[:5]}")
                else:
                    print(f"Failed to type in {id} under {token[:5]}")

main()
