import Manga
import Geturl

author_url = "https://home.gamer.com.tw/creationDetail.php?sn=3931437"
'''
Manga_list =
page_list =
journal_list =
img_list =
''' 
save_path = "D:/SystemFolder/OneDrive/code/MangaDownloader"
#manga = Manga.Manga1(url, save_path)
content = Geturl.get_content(author_url)
Manga.saveHtml("page",content)
# = Manga.get_title(page_url)
#print ()

MangaList = Manga.Booklet(author_url, 1)
MangaList.Title = MangaList.Title_()
for x in MangaList.Title
    creatPath(x)
MangaList.Url = MangaList.Url_()
for Manga_url in Manga_list.Url:
    PageList = Manga.Booklet(Manga_url, 2)
    for page_url in PageList.Url:
        journalList = Manga.Booklet(page_url, 3)
        for journal_url in journalList.Url:
            Manga.save_manga(journal_url)

print ("下载完成\n")