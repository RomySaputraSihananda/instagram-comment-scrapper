import os

from requests import Session, Response
from json import dumps
from dotenv import load_dotenv
from time import sleep

class Comment:
    def __init__(self, cookie: str) -> None:
        self.__min_id: str =  None
        self.__requests : Session = Session()
        
        self.__requests.headers.update({
            "Cookie": cookie,
            "User-Agent": "Instagram 126.0.0.25.121 Android (23/6.0.1; 320dpi; 720x1280; samsung; SM-A310F; a3xelte; samsungexynos7580; en_GB; 110937453)"
        })

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

        while True:
            response: Response = self.__requests.get(f'https://www.instagram.com/api/v1/media/{self.__media_id}/comments/{comment_id}/child_comments/?min_id={min_id}').json()

            for comment in response['child_comments']:
                print(f'\t=>{comment["text"]}')
                sleep(1)

            if(not response['has_more_head_child_comments']): break
            
            min_id: str = response['next_min_child_cursor'] 

    def __filter_comments(self, response: dict) -> None:
        for comment in response['comments']:
            print(comment['text'])

            if(comment['child_comment_count']): self.__get_reply_comment(comment['pk'])
            
            sleep(1)

        if (not 'next_min_id' in response): return True 

        self.__min_id = response['next_min_id'] 

        
    def excecute(self, post_id: str):
        self.__media_id = self.__dencode_media_id(post_id)
        while(True):
            response: Response = self.__requests.get(f'https://www.instagram.com/api/v1/media/{self.__media_id}/comments/', params=self.__build_params())
            
            if(self.__filter_comments(response.json())): break


# testing
if(__name__ == '__main__'):
    load_dotenv() 
    cookie = os.getenv("COOKIE") 

    comment: Comment = Comment(cookie)
    # comment.excecute('C1ACfnvh4KE')
    comment.excecute('C1Ww1LChZhN')
