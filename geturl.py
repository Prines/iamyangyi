import urllib.request
import re
TitleList=[]
UseList=[]

def url_open(url):
    #声明这个变量是全局变量，不然系统默认为局部
    global UseList
    r=urllib.request.urlopen(url)
    if r.getcode()!=200:
        print("网页打开失败")
    text=r.read().decode('utf-8')
      #合并各种链接列表
    HyperlinksList=re.findall(r'<a href="(.+?)"',text)
    HyperlinksList=HyperlinksList+re.findall(r'<area href="(.+?)"',text)
    HyperlinksList=HyperlinksList+re.findall(r"<a href='(.+?)'",text)
    #将有用的链接传过去
    UseList=HyperlinksList
    HyperlinksList=HyperlinksList+re.findall(r'<script.+?src="(.+?)"',text)
    HyperlinksList=HyperlinksList+re.findall(r'<img.+?src="(.+?)"',text)
    HyperlinksList=HyperlinksList+re.findall(r'<embed.+?src="(.+?)"',text)
    HyperlinksList=HyperlinksList+re.findall(r'<link.+?href="(.+?)"',text)
    print("url如下:")
    for i in HyperlinksList:
        if(i.find('./')==0):
            i=i.replace('./','/')
            use_str='http://english.whut.edu.cn'+i
            print(use_str)  
        elif i.find('http://')!=0:
            use_str='http://'+i
            print(use_str)   
        else:
            print(i)


def GetTitle():
    global TitleList
    for i in UseList:
        if(i.find('./')==0):
            i=i.replace('./','/')
            use_str='http://english.whut.edu.cn'+i  
        elif i.find('http://')!=0:
            use_str='http://'+i
        else:
            use_str=i
        if use_str.find("mailto")==-1:
            file=urllib.request.urlopen(use_str)
            if(file.getcode()==200):
                title=re.findall(r'<title>(.+?)</title>',file.read().decode('utf-8'))[0]
                if title!='':
                    TitleList.append(title)

def show():
    print("title如为")
    for i in TitleList:
        print(i)


if __name__=='__main__':
    print("请输入网址")
    aimurl=input() 
    url_open(aimurl)
    GetTitle()
    show()
    
