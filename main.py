import requests
from bs4 import BeautifulSoup

KEYWORDS = ['дизайн', 'фото', 'web', 'python']
base_url = 'https://habr.com'
url = base_url + '/ru/all/'

HEADERS = {
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
    "Connection": "keep-alive",
    "Cookie": "_ga=GA1.2.2063098236.1579294195; _ym_uid=1579294195381853071; _ym_d=1641302173; \
    __gads=ID=e487ff71e75ec085-22fcd4d2dfd300ee:T=1628432062:R:S=ALNI_Maq4eBOKN_tOJTG_gcolgCNCrCksQ; \
    cto_bundle=T5t0Xl9mUmVMRWFXVUlXTWJKZVRmNWRhbHpTWjJKMSUyQiUyRnExaGR4Tzd6cXFhQUZiJTJGNE1TVExSdHc2NVdkWU5qeTgxODJqazN5Wm1nNnV5dVhaUnZUVjkwRCUyRjYyRVRVS0FCQWJjUHVXSEVxS2M3b2hyZlJYY3BsY0lJODF1NEZ6TGF1VmclMkJBT0dKc3dpMUd3T3dyJTJCelB5ckNwZGclM0QlM0Q;\
    hl=ru; fl=ru; visited_articles=531472; _gid=GA1.2.1874216268.1655576523; habr_web_home_feed=/all/; _ym_isad=2",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0"
}

ret = requests.get(url, headers=HEADERS)
soup = BeautifulSoup(ret.text, 'html.parser')
articles = soup.find_all('article')
for article in articles:
    preview = article.find(class_='article-formatted-body article-formatted-body article-formatted-body_version-2')
    if preview != None:
        a = set(preview.text.split(sep = " ")).intersection(set(KEYWORDS))
        if len(a) > 0:
            href = article.find(class_='tm-article-snippet__title-link').attrs['href']
            title = article.find(class_='tm-article-snippet__title tm-article-snippet__title_h2').text
            date = article.find('time').attrs['title']
            print(f'{date} - {title} - {base_url}{href}')
    else:
        pass
