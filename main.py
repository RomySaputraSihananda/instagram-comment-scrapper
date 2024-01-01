import os
import re

from comment import Comment
from argparse import ArgumentParser
from json import dumps

from comment.helpers import logging

if(__name__ == '__main__'):
    argp: ArgumentParser = ArgumentParser()
    argp.add_argument("--url", '-u', type=str, default='Cm2cJmABD1p')
    argp.add_argument("--cookie", '-c', type=str)
    argp.add_argument("--output", '-o', type=str, default='data')
    args = argp.parse_args()

    post_id: str = (match := re.compile(r'https://www\.instagram\.com/(p|reel)/([^/?]+)|([^/]+)$').search(args.url)) and (match.group(2) or match.group(3)) 

    comment: Comment = Comment(args.cookie)

    if(not os.path.exists(args.output)):
            os.makedirs(args.output)

    with open(f'{args.output}/{post_id}.json', 'w') as file:
        file.write(dumps(comment.excecute(post_id), ensure_ascii=False, indent=2))
        logging.info(f'Output data : {args.output}/{post_id}.json')