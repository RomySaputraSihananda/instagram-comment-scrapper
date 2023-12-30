import os

from requests import Session, Response
from json import dumps
from dotenv import load_dotenv

class Comment:
    def __init__(self, cookie: str) -> None:
        self.__min_id: str =  None
        self.__requests : Session = Session()
        
        self.__requests.headers.update({
            "Cookie": cookie,
            "User-Agent": "Instagram 126.0.0.25.121 Android (23/6.0.1; 320dpi; 720x1280; samsung; SM-A310F; a3xelte; samsungexynos7580; en_GB; 110937453)"
        })

    def __encode_post_id(self, post_id: str) -> int:
        alphabet: str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_'
        media_id: int = 0

        for char in post_id:
            media_id = media_id * 64 + alphabet.index(char)

        return media_id

    def __build_params(self) -> dict :
        params: dict = {
            "can_support_threading": True,
            "sort_order": "popular"
        }

        if(self.__min_id): 
            params.update({
                "min_id": self.__min_id
            })
        
        return params
    
    def excecute(self, post_id: str):
        response: Response = self.__requests.get(f'https://www.instagram.com/api/v1/media/{self.__encode_post_id(post_id)}/comments/', params=self.__build_params())
        print(response)


# testing
if(__name__ == '__main__'):
    load_dotenv() 
    cookie = os.getenv("COOKIE") 

    comment: Comment = Comment(cookie)
    comment.excecute('CytLNXGBGYs')
