#!/usr/bin/env python
# coding: utf-8

# In[12]:


word = input( '請輸入中文字:' )
url = f'https://ideaking.info/searchresult/type=image&page=1&keywords={word}'
url


# In[2]:


import requests
from bs4 import BeautifulSoup

def get_image_url(word):
    url = f'https://ideaking.info/searchresult/type=image&page=1&keywords={word}'

    try:
        html = requests.get(url)
        html.raise_for_status()  # 確保請求成功

        bs = BeautifulSoup(html.content, 'lxml')
        data = bs.find('div', id='search-results-gallery')

        if data:
            # 找到第一個圖片元素
            img_tag = data.find('img')
            if img_tag:
                img_src = img_tag.get('src')
                return img_src
            else:
                return '找不到圖片'
        
        else:
            return '找不到搜尋結果'

    except requests.exceptions.RequestException as e:
        return f"Error fetching URL: {e}"

word = input('請輸入中文字:')
result = get_image_url(word)
print(result)


# In[ ]:




