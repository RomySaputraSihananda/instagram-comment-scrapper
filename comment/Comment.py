import os

from requests import Session, Response
from json import dumps
from dotenv import load_dotenv
from time import sleep
from datetime import datetime
from time import time

from comment.helpers import logging

class Comment:
    def __init__(self, cookie: str) -> None:
        self.__min_id: str =  None
        
        self.__result: dict = {}
        self.__result["caption"]: str = None
        self.__result["date_now"]: str = None
        self.__result["create_at"]: str = None
        self.__result["post_url"]: str = None
        self.__result['comments']: list = []
        
        self.__requests : Session = Session()
        self.__requests.headers.update({
            "Cookie": cookie,
            "User-Agent": "Instagram 126.0.0.25.121 Android (23/6.0.1; 320dpi; 720x1280; samsung; SM-A310F; a3xelte; samsungexynos7580; en_GB; 110937453)"
        })

    def __format_date(self, milisecond: int) -> str:
        try:
            return datetime.fromtimestamp(milisecond).strftime("%Y-%m-%dT%H:%M:%S")
        except:
            return datetime.fromtimestamp(milisecond / 1000).strftime("%Y-%m-%dT%H:%M:%S")


    def __dencode_media_id(self, post_id: str) -> int:
        alphabet: str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_'
        media_id: int = 0

        for char in post_id:
            media_id = media_id * 64 + alphabet.index(char)

        return media_id

    def __build_params(self) -> dict:
        return {
            "can_support_threading": True,
            "sort_order": "popular",
            **({"min_id": self.__min_id} if self.__min_id else {})
        }
    
    def __get_reply_comment(self, comment_id: str):
        min_id: str = ''
        child_comments: list = []

        while True:
            response: Response = self.__requests.get(f'https://www.instagram.com/api/v1/media/{self.__media_id}/comments/{comment_id}/child_comments/?min_id={min_id}').json()

            child_comments.extend([
                {
                    "username": comment["user"]["username"],
                    "full_name": comment["user"]["full_name"],
                    "comment": comment["text"],
                    "create_time": self.__format_date(comment["created_at"]),
                    "avatar": comment["user"]["profile_pic_url"],
                    "total_like": comment["comment_like_count"],
                } for comment in response['child_comments']
            ])

            if(not response['has_more_head_child_comments']): break
            
            min_id: str = response['next_min_child_cursor'] 

            sleep(1)
        return child_comments

    def __filter_comments(self, response: dict) -> None:
        for comment in response['comments']:
            logging.info(comment['text'])

            self.__result['comments'].append({
                "username": comment["user"]["username"],
                "full_name": comment["user"]["full_name"],
                "comment": comment["text"],
                "create_time": self.__format_date(comment["created_at"]),
                "avatar": comment["user"]["profile_pic_url"],
                "total_like": comment["comment_like_count"],
                "total_reply": comment["child_comment_count"],
                "replies": self.__get_reply_comment(comment['pk']) if comment['child_comment_count'] else [] 
            })
            
            sleep(1)

        if (not 'next_min_id' in response): return True 

        self.__min_id = response['next_min_id'] 

        
    def excecute(self, post_id: str):
        self.__media_id = self.__dencode_media_id(post_id)
        while(True):
            response: Response = self.__requests.get(f'https://www.instagram.com/api/v1/media/{self.__media_id}/comments/', params=self.__build_params())

            if(response.status_code != 200): return

            data: dict = response.json() 

            if(not self.__result['comments']): 
                print('ok')
                self.__result["username"]: data["user"]["username"]
                self.__result["full_name"]: data["user"]["full_name"]
                self.__result["caption"]: str = data["caption"]["text"]
                self.__result["date_now"]: str = self.__format_date(round(time() * 1000))
                self.__result["create_at"]: str = self.__format_date(data["caption"]["created_at"])
                self.__result["post_url"]: str = f"https://instagram.com/p/{post_id}"

            if(self.__filter_comments(data)): break
        
        return self.__result


# testing
if(__name__ == '__main__'):
    load_dotenv() 
    cookie = os.getenv("COOKIE") 

    comment: Comment = Comment(cookie)
    # comment.excecute('C1ACfnvh4KE')
    # comment.excecute('C1Ww1LChZhN')
    data: dict = comment.excecute('Cm2cJmABD1p')
    with open('test_data.json', 'w') as file:
        file.write(dumps(data, indent=2, ensure_ascii=False))

# "caption": "mau oleng ke siapapun tetep aja pulang lagi ke freya😣 #freyajkt48 #freyajayawardana #fypシ ",
# "date_now": "2023-12-22T21:24:08",
# "video_url": "https://t.tiktok.com/i18n/share/video/7299013864170032390/?_d=0&comment_author_id=6789225331385418754&mid=6703154980951427074&preview_pb=0&region=ID&share_comment_id=7299627887044461317&share_item_id=7299013864170032390&sharer_language=en&source=h5_t&u_code=0",
# "comments": [
# {
#     "username": "ryzzhighinthesky",
#     "nickname": "Not Ryz",
#     "comment": "freya aku mau cbr😣😣",
#     "create_time": "2023-11-10T07:44:48",
#     "avatar": "https://p16-sign-va.tiktokcdn.com/tos-maliva-avt-0068/4c3c29930e3420f1119852fee1767dea~c5_100x100.jpg?x-expires=1703340000&x-signature=j00DUxk%2B8pIXiUjAO3n%2Bs9dOWjo%3D",
#     "total_reply": 0,
#     "replies": []
# },')
