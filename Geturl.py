
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
    header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    try:
        req = urllib.request.Request(url=the_url, headers=header)
        response = urllib.request.urlopen(req)
        html = response.read()
    except Exception as e:
        print (e)
        print ("Fail to open web:" + the_url)
        html = get_content(the_url)
    #while type(html) != bytes:
    #    res = Geturl.get_content(the_url)

    return html

def get_page_url_arr(author_url):
    
    content = get_content(author_url)
    encode_type = chardet.detect(content)
    content = content.decode(encode_type['encoding'])
    base_url = 'https://home.gamer.com.tw/'
    pattern = re.compile('└.*?</a>', re.S)
    comics_part = re.findall(pattern, content)
    pages = [page for page in range(26, 31)]
    
    arr = []
    for page in pages:
        page_url = base_url + 'creationCategory.php?page=' + str(page) + '&owner=tpesamguo&v=0&c=338592'
        arr.append(page_url)
    
    print("total pages: " + str(len(arr)))
    return arr

def get_journal_part(url):

    content = Geturl.get_content(url)
    #Manga.saveHtml("test2", content)
    encode_type = chardet.detect(content)
    content = content.decode(encode_type['encoding'])
    pattern = re.compile(r'<a\sclass="TS1"\shref="creationDetail.php\?sn=.*?">.*?</a>', re.S)
    result = str(re.findall(pattern, content))

    return result


def bulid_journal_url(url):

    base_url = 'https://home.gamer.com.tw/creationDetail.php?sn='
    pattern = re.compile(r'creationDetail\.php\?sn=(.*?)"', re.S)
    journal_arr = Geturl.get_journal_part(url)
    items = re.findall(pattern, journal_arr)

    arr = []
    for item in items:
        journal_url = base_url + item
        arr.append(journal_url)

    return arr

def get_manga_url(url):
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




