import Manga
import Geturl

author_url = "https://home.gamer.com.tw/creation.php?page=1&owner=tpesamguo&v=0&t=0"
save_path = "D:/SystemFolder/OneDrive/code/python"
#manga = Manga.Manga1(url, save_path)
#content = Geturl.get_content(page_url)
#Manga.saveHtml("page",content)


page_list = Geturl.get_page_url_arr(author_url)
for page_url in page_list:
    Manga.save_manga(page_url)
#    title = Manga.get_title(page_url)
#    print (title)


print ("下载完成\n")