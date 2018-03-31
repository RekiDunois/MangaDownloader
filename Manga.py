import urllib.request
import re
import os
import zlib
import Geturl

class Manga:
    #谁告诉我这个类有p用?
    def __init__(the_url, path):
        exists = os.path.exists(path)
        if not exists:
            print ("Path Wrong.")
            exit(0)

        self.base_url = the_url
        self.path = path

class Booklet:
    #传入需要获得页面中的url信息或/和标题信息的url
    Title = ''
    Url = ''
    types = ''
    Pattern = ''
    def __init__(url,types):
        #传入一个url, 不过并不是全部url都用得上Title_方法, 但是都能用得上Url_方法
        self.url = url
        self.types = types
        if types = 1:
            Pattern = '└.*?</a>'
        if types = 2:
            Pattern = 'r<a\sclass="TS1"\shref="creationDetail.php\?sn=.*?">.*?</a>'
        if types = 3:
            Pattern = ''
    
    def Title_(url):
        pattern = re.compile(Pattern, re.S)
        result = Manga.get_title(url, pattern)
        return result
    
    def Url_(url):
        pattern = re.compile(Pattern, re.S)
        result = Manga.get_url(url, pattern)
        return result


def saveHtml(file_name, file_content):
    #测试正则表达式的时候用来保存html页面
    with open(file_name.replace('/','_')+".html","wb") as f:
        f.write(file_content)

def get_part(url, pattern):
    #获得某个需要的部分, 其正则表达式应在对应实例的类中计算, 该函数不计算正则表达式
    content = Geturl.get_content(url)
    encode_type = chardet.detect(content)
    content = content.decode(encode_type['encoding'])
    result = str(re.findall(pattern, content))

    return result

def get_title(url,pattern):
    #获得汉字标题, 漫画|章节标题
    TitlePart = Geturl.get_part(url, pattern)
    _pattern = re.compile(r'(\].*?<|>[\\u3000]|/>.+<)+', re.S)
    result = re.findall(_pattern, TitlePart)
    return result

def save_manga():
    #将漫画保存到本地
    journalList = Geturl.bulid_journal_url(url) 
    imgTitle = get_img_title(url)
    #传入分页url, 获得该分页上所有章节的url
    i = 0
    #用来表示现在保存的是第几个章节的标记
    for journalUrl in journalList:
        imgList = Geturl.get_manga_url(journalUrl)
        position = len(imgList)
        #传入一个章节url, 获得该章节中的所有漫画图片url
        if position != 1:
            #若该章节不止一张图, 则使用这一方式保存
            j = 1
            #用来标记本章节的第几张图
            for imgUrl in imgList:
                res = Geturl.get_content(imgUrl) #将图片以bytes形式储存
                name = str(imgTitle[i]) + str(j)
                if name.find('\\u') != -1:
                    name = re.sub('u3000', '', name)
                    #去掉unicode字符中代表括号的部分
                    if name == None:
                        name = 'empty'
                name = re.sub('[\/:*?"<>|翻譯\[\]]', '', name)
                #去掉windows系统不允许作为文件名的字符以及大量重复的字符如翻译二字
                print(name)
                with open("D:\\SystemFolder\\OneDrive\\code\\MangaDownloader\\Manga\\%s.jpg" %name, "wb") as f:
                    f.write(res)
                j += 1 #下一个循环将是本章节的下一张图, 故j标记每次循环递增
        if position == 1:
            #该章节只有一张图的保存方式
            res = Geturl.get_content(imgUrl[0])
            #因为只有一张图, 所以列表的首位就是我们需要的文件名
            name = str(imgUrl[i])
            if name.find('\\u') != -1:
                name = re.sub('u3000','',name)
                if name == None:
                    name = 'empty'
            name = re.sub('[\/:*?"<>|翻譯\[\]]', '', name)
            print(name)
            with open("D:\\SystemFolder\\OneDrive\\code\\MangaDownloader\\Manga\\%s.jpg"%name,"wb") as f:
                f.write(res)
        i += 1 #该章节保存完成, 进入下一章节

def creatPath(path)
    