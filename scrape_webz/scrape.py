import json
import re
import requests
from post.Post import Post
res=requests.get('https://www.phpbb.com/community/viewtopic.php?f=46&t=2159437')
con=res.text.replace('<br>','')

post_pat = r'<div id="p\d+"$>(.*?)</div>'
post_pat = r'<div id="p\d+" class="post has-profile bg\d">(.*?)(?=<div id="sig\d+" class="signature">)'
posts = re.findall(post_pat, con, re.DOTALL)

#could have been splitted to 4 different groups, maybe fix later..
posts = re.findall(post_pat, con, re.DOTALL) # get all posts exclude the signature
title_ptn = r'<div id="post_content\d+">.*?<a href="[^"]*">(.*?)</a>'
# author_ptn = r'<a href="\.\/member.*? class="username">(.*?)</a>'
author_ptn = r'<a.*?class="username.*?">(.*?)</a>'
date_ptn = r'<time datetime="([^"]*)">'
content_ptn = r'<div class="content">((?:<(?!div\b|/div\b)[^>]*>|<div[^>]*>.*?</div>|.)*?)</div>'


def format_phpb_web_site(p):
    title = re.search(title_ptn, p, re.DOTALL).group(1)
    author = re.search(author_ptn, p, re.DOTALL).group(1)
    date = re.search(date_ptn, p, re.DOTALL).group(1)
    content = re.search(content_ptn, p, re.DOTALL)
    content=re.sub(r'<[^>]*>', '', content.group(1))
    # print(content)
    return Post(title, content, author, date).__dict__

numbered_posts = {i+1:format_phpb_web_site(post) for i,post in enumerate(posts)}

with open('phpb_web.txt','w',encoding='utf-8') as f:
    json.dump(numbered_posts,f,indent=4)