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

def Send_Data(id, token):
    headers = {"authorization" : token}
    endpoint = f"https://discord.com/api/v9/channels/{id}/typing"
    res = requests.post(endpoint, headers=headers)
    if res.status_code == 204:
        print(f"Sent typing request to {id} under {token[:5]}")
    else:
        print(f"Failed to type in {id} under {token[:5]}")

def main():
    os.system("cls")
    print("Beginning autotyper")
    while True:
        for id in ids:
            for token in tokens:
                Send_Data(id, token)
        time.sleep(1)


if __name__ == "__main__":
    main()
