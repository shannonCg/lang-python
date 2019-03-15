import requests
from bs4 import BeautifulSoup

#basic used
url = 'https://www.nhi.gov.tw/News.aspx?n=A7EACB4FF749207D&sms=587F1A3D9A03E2AD&topn=A7EACB4FF749207D'
html = requests.get(url).text
sp = BeautifulSoup(html, 'html.parser')

#find all tags <a>
links = sp.find_all('a')
# for link in links:
#     print("type of link:", type(link))
#     print("link:", link)
#     print("href:", link.get('href')) #attribute 'href' in tag <a>
#     print("title:", link.get('title')) #attribute 'title' in tag <a>
#     print("content:", link.contents) #content in tag <a>
#     print()

#find tag <div> with attribut id=base-content
div = sp.find_all('div', {'id':'base-content'})
# print(div)
# print("---------------------")

#parse table element
table = sp.find_all('table')
# print(table)
tbody = table[0].find_all('tbody')
# print(tbody)
trs = tbody[0].find_all('tr')
# print(trs)
row_contents = []
for tr in trs:
    tds = tr.find_all('td')
    # print(tds)
    # print()

    span_content = tds[0].find_all('span')[0].contents[0]
    # print(span_content)
    a_content = tds[1].find_all('a')[0].contents[0]
    # print(a_content)
    # print()
    contents = [span_content, a_content]
    row_contents.append(contents)

print(row_contents)
