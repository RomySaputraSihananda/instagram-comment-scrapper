import requests
from json import dumps

params = {
    "can_support_threading": True,
    "min_id": dumps({
        "cached_comments_cursor": "18004392299258417", 
        "bifilter_token": "KD8BDAB4ACAAGAAQABAACACn_f_6ff3c7N9_t-__9__gPvbH4rzx_zD_5___vz3n_f9-wv__f_77IZtqZpAZsUAA"
    }),
    "sort_order": "popular"
}

headers = {
    # 'Cookie': 'ig_nrcb=1; mid=ZSZi_gAEAAHXcCtsxv3cG8biTwgH; csrftoken=ZA4OXT11XEKVGS2sp9GAjElCwLpMAn5p; ds_user_id=46719067093; dpr=1.100000023841858',
    'Cookie': 'ig_did=C37733B2-2853-40A7-B3B1-70BBA58EBEA7; ig_nrcb=1; mid=ZSZi_gAEAAHXcCtsxv3cG8biTwgH; datr=_GImZcBIvUSXBBx6325xMiJH; ds_user_id=46719067093; dpr=1.100000023841858; shbid="15857\05446719067093\0541735462074:01f75729e3d962279bf746c9b9146fc7c61da319b01bc7eff14bce2087bf8e3c84411647"; shbts="1703926074\05446719067093\0541735462074:01f748b6143e0bfdf1e3d48a19d93bc85baa93c8504e5fef41a004dcbb0043de5b19709e"; csrftoken=eU7hjKHq1zXyNN8NdJoC7qIDK5Fq7emX; sessionid=46719067093%3AvXNDOezyRKUqjo%3A29%3AAYcGNBHS33I8sxt5ODQms_HHpxuESd2fThVOD_0pEA; rur="NHA\05446719067093\0541735465749:01f782cfcd3a549434f95ef7d3f746d60d1ee47493a68b4180002d1e675d31b1a4c63e97"',
    'User-Agent':'Instagram 126.0.0.25.121 Android (23/6.0.1; 320dpi; 720x1280; samsung; SM-A310F; a3xelte; samsungexynos7580; en_GB; 110937453)',
}

# res = requests.get('https://www.instagram.com/api/v1/media/3260617099286381188/comments/?cached_comments_cursor=15',headers=headers)
# res = requests.get('https://www.instagram.com/api/v1/media/3260617099286381188/comments/?can_support_threading=true&permalink_enabled=true',headers=headers)
res = requests.get('https://www.instagram.com/api/v1/media/3260617099286381188/comments/', headers=headers, params=params)

print(res)
# for comment in res.json()['comments']:
#     print(comment['text'])


with open('file5.json', 'w') as file:
    file.write(dumps(res.json(), ensure_ascii=False, indent=2))


# https://www.instagram.com/api/v1/media/3268838954052919246/comments/?can_support_threading=true&min_id=%7B%22cached_comments_cursor%22%3A%20%2217872723323022949%22%2C%20%22bifilter_token%22%3A%20%22KJEBAEGOGvXcRkAAQXfk6DMDQABEYmG4Bvw_AIeCkx19QUAAyqzPOskCQACLK4uf87xAAA5867fchz8AE3RBHGT4PwDfJ_z2yP8_AGGQOeLf3T8AI7kk6gz2PwCmarHgWmZBAOhszII17T8Ab8cMfNT6PwBw9XOYlxpAAPNOU8y_4j8A9xSNePIUQAA7W45ka5U_AAA%3D%22%7D&sort_order=popular
