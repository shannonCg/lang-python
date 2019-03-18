import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import os
import shutil

url = 'https://www.nhi.gov.tw/News.aspx?n=A7EACB4FF749207D&sms=587F1A3D9A03E2AD&topn=A7EACB4FF749207D'
html = requests.get(url).text
sp = BeautifulSoup(html, 'html.parser')
parse_url = urlparse(url)
domain = "{}://{}".format(parse_url.scheme, parse_url.netloc)

#create directory to store images
dir_path = "./images"
if not os.path.exists(dir_path):
    os.mkdir(dir_path)
    print("create directory successfully!")

#find all tags <img>
imgs = sp.find_all('img')
print(imgs)
for img in imgs:
    img_url = img.get('src')
    if img_url and ('.png' in img_url or '.jpg' in img_url):
        if not img_url.startswith('http'):
            img_url = domain + img_url
        print("img", img_url)

    #store image into the directory
    file_path = os.path.join(dir_path, img_url.split('/')[-1])
    if os.path.exists(file_path):
        continue
    img_content = requests.get(img_url, stream=True)
    with open(file_path, 'wb') as f:
        shutil.copyfileobj(img_content.raw, f)
    print("create image successfully")
