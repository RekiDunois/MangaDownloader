
import urllib.request
import re
import os
import zlib
import chardet
import Geturl
import Manga

class geturl:

    def __init__(self, url):
        self.base_url = url

def get_content(the_url):
    #获得指定url的页面信息
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    #传入一个header, 避免被服务器拒绝
    try:
        #使用异常检测机制
        req = urllib.request.Request(url=the_url, headers=header)
        response = urllib.request.urlopen(req)
        html = response.read()
        #此时, html为bytes形式
    except Exception as e:
        print (e)
        print ("Fail to open web:" + the_url)
        html = get_content(the_url)
        #若出现异常, 则重新调用该方法

    return html

def get_page_url_arr(author_url):
    #获得一个储存了单一漫画所有分页url的列表
    content = get_content(author_url)
    encode_type = chardet.detect(content)
    content = content.decode(encode_type['encoding'])
    base_url = 'https://home.gamer.com.tw/'
    pattern = re.compile('└.*?</a>', re.S)
    comics_part = re.findall(pattern, content)
    print (comics_part)
    pages = [page for page in range(26, 31)]
    
    arr = []
    for page in pages:
        page_url = base_url + 'creationCategory.php?page=' + str(page) + '&owner=tpesamguo&v=0&c=338592'
        arr.append(page_url)
    
    print("total pages: " + str(len(arr)))
    return arr

'''
def get_journal_part(url):
    #传入一个分页url, 获得该分页上与章节url和标题有关的部分
    content = Geturl.get_content(url)
    encode_type = chardet.detect(content)
    content = content.decode(encode_type['encoding'])
    pattern = re.compile(r'<a\sclass="TS1"\shref="creationDetail.php\?sn=.*?">.*?</a>', re.S)
    result = str(re.findall(pattern, content))

    return result
'''

def get_url(url, pattern):
    #使用part方法, 构建一个储存了一个分页上所有章节url的列表
    base_url = 'https://home.gamer.com.tw/creationDetail.php?sn='
    _pattern = re.compile(r'creationDetail\.php\?sn=(.*?)"', re.S)
    journal_arr = Manga.get_part(url, pattern)
    items = re.findall(_pattern, journal_arr)
    arr = []
    for item in items:
        journal_url = base_url + item
        arr.append(journal_url)
    return arr

def get_manga_url(url):
    #传入一个章节url, 获得该章节所有漫画图片的url
    content = Geturl.get_content(url)
    if not content:
        return None
    encode_type = chardet.detect(content)
    content = content.decode(encode_type['encoding'])

    pattern = re.compile(r'data-src="https?://i.imgur.com/.*?"', re.S)
    result_part = str(re.findall(pattern, content))

    pattern = re.compile(r'https?://i.imgur.com/.*?"', re.S)
    result = re.findall(pattern, result_part)

    return result




