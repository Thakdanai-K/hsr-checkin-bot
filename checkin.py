import requests
import time
import random
import hashlib
import os

ACT_ID = 'e202303301540311'
UID = os.getenv('UID')
REGION = 'os_asia'
COOKIE = os.getenv('COOKIE')

SALT = "xV8v4Qu54lUKrEYFZkJhB8cuOh9Asafs"

def create_ds():
    t = str(int(time.time()))
    r = str(random.randint(100000, 200000))
    h = hashlib.md5(f"salt={SALT}&t={t}&r={r}".encode()).hexdigest()
    return f"{t},{r},{h}"

def checkin():
    url = "https://api-takumi.mihoyo.com/event/luna/sign"
    headers = {
        "Cookie": COOKIE,
        "DS": create_ds(),
        "x-rpc-client_type": "5",
        "x-rpc-app_version": "2.60.1",
        "User-Agent": "okhttp/4.8.0",
        "Content-Type": "application/json"
    }
    payload = {
        "act_id": ACT_ID,
        "region": REGION,
        "uid": UID
    }
    resp = requests.post(url, json=payload, headers=headers)
    print(resp.json())

if __name__ == "__main__":
    checkin()
