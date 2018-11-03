from urllib.request import urlopen#用于获取网页
from bs4 import BeautifulSoup#用于解析网页
import urllib.request
import certifi
from urllib.parse import unquote
import os, errno
import wget
import easygui
from pget.down import Downloader
import os.path

import login
import setting

user = setting.USER
pwd  = setting.PWD

webroot = "https://github.com"

main = login.Login()
main.login(user,pwd)


def fast_download(url,filename):
    chunk_count = 1
    downloader = Downloader(url, filename, chunk_count)
    downloader.start_sync()
    #downloader.start()
    #downloader.subscribe(callback, callback_threshold)
    #downloader.wait_for_finish()
    return;

folder = ""
#pemfile = '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/certifi/cacert.pem'

def to_utf8(text):
    if isinstance(text, unicode):
        # unicode to utf-8
        return text.encode('utf-8')
    try:
        # maybe utf-8
        return text.decode('utf-8').encode('utf-8')
    except UnicodeError:
        # gbk to utf-8
        return text.decode('gbk').encode('utf-8')
    
def create_folder(directory):
    try:
        directory = unquote(directory)
        os.makedirs(directory)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    return directory;

def create_dir(path):
    # define the access rights
    path = unquote(path)
    access_rights = 0o755
    try:  
        os.mkdir(path, access_rights)
    except OSError:  
        print ("Creation of the directory %s failed" % path)
    else:  
        print ("Successfully created the directory %s" % path)
    
def down_file( url,folder ):
    name = url[url.rfind("/") + 1:] 
    file_name = folder + "/" + unquote(name)
    #if not os.path.isfile(file_name):
    print(url)
        #fast_download(url, file_name)
    print(file_name)
    #else:
        #print(file_name)
    with urllib.request.urlopen(url) as response, open(file_name, 'wb') as out_file:
        data = response.read() # a `bytes` object
        out_file.write(data)
    return file_name;

count = 0

def downfile(url, folder):
    name = url[url.rfind("/") + 1:] 
    file_name = unquote(name)
    #folder = './' + folder  
    #count += 1
    #file_name = str(count) + '.mp4'
    #wget.download(url, file_name)
    filename = wget.download(url)
    print(file_name)
    return file_name;
    
path = 'url.txt'
days_file = open(path,'r')
#print (days_file.read())
stock_list = []
#print (days_file.readline())
while True:
    li = days_file.readline()
    if len(li) > 2:      
        #li.replace("\n","")
        li = li[:-1]
        stock_list.append(li)   
    #print(line)
    if not li: 
        break
        
myurl = stock_list[0]
print(myurl)

if myurl[-1:] == '/' :
    urlshort = myurl[0:len(myurl)-1]
    name = urlshort[urlshort.rfind("/") + 1:] 
    folder = unquote(name)
    print(folder)
    create_folder(folder)
    
urls = []
folder1 = []
folder0 = ""
name = ""

count = 0
def down_folder( url,fold):
    html = urlopen(url)
    bsObj = BeautifulSoup(html, 'html.parser')
    t1 = bsObj.find_all('a')
    for h in t1:
        #a = h.find('a')
        a = h
        if a is not None and 'href' in a.attrs:
            l = a.get('href')
            #print(l)
            root = webroot + l      
            if len( root ) < len(myurl) :
                if root[-1:] == '/' :
                    urlshort = root[0:len(root)-1]
            else:
                if root[-1:] == '/' :
                    folder1.append(root)
                    #print(root)
            try:
                if root[-4:] == '.dcm' :
                    print(root)
                    newroot="https://raw.githubusercontent.com" + root[len(webroot):]
                    urls.append(newroot)
                    count += 1
                    if count > 5 :
                        break;
                        return;
                    #down_file(root, fold) 
                #filename = wget.download(root)
                #print(filename)
            except:
                pass
    return;

down_folder(myurl,folder)    
create_folder('./dcm')
print("Download Start")
folder = "./dcm"
for u in urls:
    try:
        down_file(u, folder)
    except:
        pass  
print("Download End")

print('====folder1====')
for h in folder1:
    print(h)
    urlshort = h[0:len(h)-1]
    name = urlshort[urlshort.rfind("/") + 1:] 
    folder1_1 = "./" + folder + "/" + name
    print(folder1_1)
    create_dir(folder1_1)
    down_folder(h, folder1_1)   
print('====Done====')
easygui.msgbox(folder, title="====Done====")

