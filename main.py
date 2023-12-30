import requests
from json import dumps
from dotenv import load_dotenv
import os
load_dotenv() 
cookie = os.getenv("COOKIE") 

params = {
    "can_support_threading": True,
    "sort_order": "popular",
    "min_id": dumps({
        "cached_comments_cursor": "18004392299258417", 
        "bifilter_token": "KD8BDAB4ACAAGAAQABAACACn_f_6ff3c7N9_t-__9__gPvbH4rzx_zD_5___vz3n_f9-wv__f_77IZtqZpAZsUAA"
        # "cached_comments_cursor": None, 
        # "bifilter_token": None
    }),
}

headers = {
    'Cookie': cookie,
    'User-Agent':'Instagram 126.0.0.25.121 Android (23/6.0.1; 320dpi; 720x1280; samsung; SM-A310F; a3xelte; samsungexynos7580; en_GB; 110937453)',
}

# res = requests.get('https://www.instagram.com/api/v1/media/3260617099286381188/comments/?cached_comments_cursor=15',headers=headers)
# res = requests.get('https://www.instagram.com/api/v1/media/3260617099286381188/comments/?can_support_threading=true&permalink_enabled=true',headers=headers)
res = requests.get('https://www.instagram.com/api/v1/media/3246603194377677047/comments/', headers=headers, params=params)

# for comment in res.json()['comments']:
#     print(comment['text'])

# res = requests.get('https://www.instagram.com/api/v1/media/3246603194377677047/comments/18098933587367200/child_comments/?min_id=QVFBWm1seWZuOHdlVG9KdjZ0NUNaQWgtS2lMMXNaMDBiQzd5blFkV3BIcGlUdEM5VGdIbmU1d2h3RVhjWFR1TXFhRTBEVC0wZFdhTnBCM2JsbFd4ZkxkbQ==', headers=headers)
print(res)

with open('file.json', 'w') as file:
    file.write(dumps(res.json(), ensure_ascii=False, indent=2))
