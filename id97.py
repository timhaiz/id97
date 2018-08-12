import requests
from bs4 import BeautifulSoup
import time
video_list     = []
page_list      = []
down_url       = []
videos_info    = []
#构建网站目录
def url_list():
    print('抓取电影链接中。。。')
    q = 'http://www.id97.com/movie/?page='
    for i in range(1):
        url = q + str(i)
        video_list.append(url)
    print(video_list)

#获取电影页
def page_info():
    print('获取电影页...')
    for i in video_list:
        html = requests.get(i).text
        soup = BeautifulSoup(html,'html.parser')
        page_url = soup.select('div.meta h1 a[href]')
        for url in page_url:
            url = url.get('href')
            page_list.append(url)
        print(page_list)

#解析电影页，获取电影信息
def soup():
    print('获取电影信息...')
    for html in page_list:
        video_html = requests.get(html).text
        soup = BeautifulSoup(video_html,'html.parser')
        video_name = soup.select('div > h1')
        for name in video_name:
            video_n = name.text
        video_info = soup.select('div table:nth-of-type(1)')
        for info_video in video_info:
            i_video = info_video.text
        print(i_video)


        url = html.split('/')[-1]
        video_url = 'http://www.id97.com/videos/resList/' + url
        i_html = requests.get(video_url).text
        i_soup = BeautifulSoup(i_html,'html.parser')
        down_urls = i_soup.select('div > a')
        for i in down_urls:
            info = i.get('href')
            if info.startswith('https://pan.baidu.com'):
                password = i_soup.select('td.text-break > div > strong')
                for p in password:
                    password = p.text
                Pan_info = info,password
                pan = list(Pan_info)
                BaiduPan = pan[0] + ' '+  pan[1]
                down_url.append(BaiduPan)
            if info.startswith('ed2k') or info.startswith('magnet'):
                CiLi = info
                down_url.append(CiLi)
        print(down_url)
        videos_info.append(video_n)
        videos_info.append(i_video)
        videos_info.append(down_url)




while True:
    url_list()
    page_info()
    soup()
    print(videos_info)
    print('等6秒')
    time.sleep(6)


