import requests

url = 'https://flk.npc.gov.cn/api/detail/'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
}
data = {
    'id': 'ZmY4MDgxODE4YTIxZGMxMzAxOGE1MTMyOGUwYzBjM2M%3D'
}
response = requests.post(url=url, data=data, headers=headers)

title = response.json()['result']['title']
path = response.json()['result']['body'][0]['path'] if response.json()['result']['body'][0]['path'] else ''
download_url = 'https://wb.flk.npc.gov.cn' + path
if not path:
    print(f"Path not found for title: {title}")
print(title, download_url)

file_extension = download_url.split('.')[-1]
content = requests.get(url=download_url, headers=headers).content
with open('single_item_scraping_folder\\' + title + '.' + file_extension, mode='wb') as f:
    f.write(content)