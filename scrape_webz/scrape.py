import re
import requests
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

i=1
for p in posts:
    print(f'---------------{i}------------------')
    title = re.search(title_ptn, p, re.DOTALL)
    print(f'title={title.group(1)}\n')
    author = re.search(author_ptn, p, re.DOTALL)
    print(f'author={author.group(1)}\n')
    date = re.search(date_ptn, p, re.DOTALL)
    print(f'date={date.group(1)}\n')
    content = re.search(content_ptn, p, re.DOTALL)
    # print(f'content={content.group(1)}\n')
    print(re.sub(r'<[^>]*>', '', "content="+content.group(1)))
    print("----------------------------------")
    print("\n")
    i+=1