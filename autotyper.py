import requests
import time

token = ""
ids = [
    1
]

headers = {"authorization" : token}
print("Beginning autotyper")
while True:
    for id in ids:
        endpoint = f"https://discord.com/api/v9/channels/{id}/typing"
        time.sleep(1)
        res = requests.post(endpoint,headers=headers)
        if res.status_code == 204:
            print(f"sent to {id}")
        else:
            print(f"failed to send to {id}")
