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
res = requests.get('https://www.instagram.com/api/v1/media/3260617099286381188/comments/', headers=headers, params=params)

print(res)
# for comment in res.json()['comments']:
#     print(comment['text'])


with open('file6.json', 'w') as file:
    file.write(dumps(res.json(), ensure_ascii=False, indent=2))


# https://www.instagram.com/api/v1/media/3268838954052919246/comments/?can_support_threading=true&min_id=%7B%22cached_comments_cursor%22%3A%20%2217872723323022949%22%2C%20%22bifilter_token%22%3A%20%22KJEBAEGOGvXcRkAAQXfk6DMDQABEYmG4Bvw_AIeCkx19QUAAyqzPOskCQACLK4uf87xAAA5867fchz8AE3RBHGT4PwDfJ_z2yP8_AGGQOeLf3T8AI7kk6gz2PwCmarHgWmZBAOhszII17T8Ab8cMfNT6PwBw9XOYlxpAAPNOU8y_4j8A9xSNePIUQAA7W45ka5U_AAA%3D%22%7D&sort_order=popular
