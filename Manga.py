import urllib.request
import re
import os
import zlib
import Geturl

class Manga:
    def __init__(the_url, path):
        exists = os.path.exists(path)
        if not exists:
            print ("Path Wrong.")
            exit(0)

        self.base_url = the_url
        self.path = path

def saveHtml(file_name, file_content):
    with open(file_name.replace('/','_')+".html","wb") as f:
        f.write(file_content)

def get_title(url):
    title_part = Geturl.get_journal_part(url)
    pattern = re.compile(r'(\].*?<|>[\\u3000]+<)+', re.S)
    result = re.findall(pattern, title_part)
    return result

def save_manga(url):
    journal_arr = Geturl.bulid_journal_url(url)
    Manga_title = get_title(url)
    i = 0 #'齊柏林，融入日本生活' '艦娘們，接受敵人的好意'
    for journal_url in journal_arr:
        Manga_arr = Geturl.get_manga_url(journal_url)
        position = len(Manga_arr)
        if position != 1:
            j = 1
            for Manga_url in Manga_arr:
                res = Geturl.get_content(Manga_url)
                name = str(Manga_title[i]) + str(j)
                if name.find('\\u') != -1:
                    name = re.sub('u3000', '', name)
                    if name == None:
                        name = 'empty'
                name = re.sub('[\/:*?"<>|翻譯\[\]]','',name)
                print(name)
                with open("D:\\SystemFolder\\OneDrive\\code\\python\\Manga\\%s.jpg" %name, "wb") as f:
                    f.write(res)
                j += 1
        if position == 1:
            res = Geturl.get_content(Manga_arr[0])
            name = str(Manga_title[i])
            if name.find('\\u') != -1:
                name = re.sub('u3000','',name)
                if name == None:
                    name = 'empty'
            name = re.sub('[\/:*?"<>|翻譯\[\]]', '', name)
            print(name)
            with open("D:\\SystemFolder\\OneDrive\\code\\python\\Manga\\%s.jpg"%name,"wb") as f:
                f.write(res)
        i += 1
    