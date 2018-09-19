import urllib.request,os,logging
from bs4 import BeautifulSoup
import shutil

def initializ():
    '''每次脚本运行前进行初始化'''
    if os.path.exists('news_list'):
        shutil.rmtree('news_list')
    else:
        pass
def create_file():
    '''创建文件夹'''
    if not os.path.exists('news_list'):
        os.mkdir('news_list')


def download_page(url):
    '''下载网页'''
    file=urllib.request.urlopen(url).read()
    return file


def get_newscategory(file):
    '''得到新闻类别'''
    newscategory_list=[]
    soup=BeautifulSoup(file,'html.parser')
    for i in soup.find('div',{'class':'cNavLinks','data-sudaclick':'newsnav'}).find_all('a'):
        newscategory=i.get_text()
        link=i.get('href')
        str=newscategory+link
        newscategory_list.append(str)
    return newscategory_list

#网页爬虫部分
def get_scroll(url):
    '''滚动新闻，爬不出来'''
    dic={}
    file=download_page(url)
    soup=BeautifulSoup(file,'html.parser')
    news=soup.find_all('td',{'class':'ConsTi'})
    for i in news:
        title=i.find('a')
        link=i.find('a').get_text()
        dic[title]=link
    return (dic)
def get_world(url):
    '''获取国际页面新闻'''
    file=download_page(url)
    soup=BeautifulSoup(file,'html.parser')
    dic={}
    news=soup.find('div',{'class':'blk122'}).find_all('a')
    for i in news:
        title=i.get_text()
        link=i.get('href')
        if link==None:
            link='None'
        dic[title]=link
    new2=soup.find('div',{'id':'subShowContent1_static'}).find_all('h2')
    for i in new2:
        title=i.get_text()
        link=i.get('href')
        if link==None:
            link='None'
        dic[title]=link
    return(dic)
def get_mil(url):
    '''获取军事新闻'''
    file=download_page(url)
    dic={}
    soup=BeautifulSoup(file,'html.parser')
    news1=soup.find_all('ul',{'class':'part1 arcticle-list'})
    news2=soup.find_all('ul',{'class':'part2 arcticle-list'})
    news3=soup.find_all('ul',{'class':'mess_link_one'})
    news11=[]
    news22=[]
    news33=[]
    for i in news1:
        news11=news11+i.find_all('a')
    for i in news2:
        news22=news22+i.find_all('a')
    for i in news3:
        news33=news22+i.find_all('a')
    news=news11+news22+news33
    for i in news:
        title=i.get_text()
        link=i.get('href')
        dic[title]=link
    return(dic)

def get_gov(url):
    '''获取政务新闻'''
    dic={}
    file=download_page(url)
    soup=BeautifulSoup(file,'html.parser')
    dic={}
    news=soup.find_all('dt',{'class':''})
    for i in news:
        title=i.find('a').get_text()
        link=i.find('a').attrs['href']
        dic[title]=link
    return(dic)
def get_society(url):
    '''获取社会新闻，同样有元素无法定位  china'''
    file=download_page(url)
    dic={}
    soup=BeautifulSoup(file,'html.parser')
    news=soup.find('div',{'class':'right-content'}).find_all('a')
    for i in news:
        title=i.get_text()
        link=i.get('href')
        dic[title]=link
    return(dic)
def get_cul(url):
    '''简单得到文化页新闻'''
    file=download_page(url)
    dic={}
    soup=BeautifulSoup(file,'html.parser')
    news=soup.find('div',{'id':'subShowContent1'}).find_all('a')+soup.find('div',{'class':'blk122'}).find_all('a')
    for i in news:
        title=i.get_text()
        link=i.attrs['href']
        dic[title]=link
    dic.pop('评论')
    return(dic)

def get_sports(url):
    '''简单获取体育页的新闻'''
    file=download_page(url)
    dic={}
    soup=BeautifulSoup(file,'html.parser')
    news=soup.find_all('a',{'target':'_blank'})
    for i in news:
        title=i.get_text()
        link=i.attrs['href']
        dic[title]=link
    return(dic)
def get_china(url):
    '''获取国内新闻，有元素无法准确定位'''
    dic={}
    file=download_page(url)
    soup=BeautifulSoup(file,'html.parser')
    news1=soup.find('div',{'class':'right-content'}).find_all('li')
    for i in news1:
        title=i.find('a').get_text()
        link=i.find('a').get('href')
        dic[title]=link
    #print(dic)
    # news2=soup.find('div',{'class':'feed-card-txt'})

    # print('news2:',news2)
    # for i in news2:
    #     title=i.find('a').get_text()
    #     link=i.find('a').get('href')
    #     dic[title]=link
    return(dic)
def get_ent(url):
    '''获取娱乐页面新闻'''
    dic={}
    file=download_page(url)
    soup=BeautifulSoup(file,'html.parser')
    news=soup.find('div',{'class':'feed_card'}).find_all('a',{'target':'_blank'})
    for i in news:
        title=i.get_text()
        link=i.attrs['href']
        dic[title]=link
    return(dic)

def get_finance(url):
    '''获取财经新闻，未做详细处理'''
    dic={}
    file=download_page(url)
    soup=BeautifulSoup(file,'html.parser')
    news=soup.find('div',{'class':'m-p-middle fleft','id':'directAd_huaxia'}).find_all('a',target='_blank')
    for i in news:
        title=i.get_text()
        link=i.attrs['href']
        dic[title]=link
    return(dic)

def get_hotnews(url):
    '''新闻排行'''
    dic={}
    file=download_page(url)
    soup=BeautifulSoup(file,'html.parser')
    news=soup.find_all('td',{'class':'ConsTi'})
    for i in news:
        title=i.find('a').get_text()
        link=i.find('a').get('href')
        dic[title]=link
    return (dic)


def get_tech(url):
    '''科技新闻页面爬虫'''
    dic={}
    html=download_page(url)
    soup=BeautifulSoup(html,'html.parser')
    all_news=soup.find('div',{'class':'tech-main width-1240 clearfix'})
    mid_news=all_news.find('div',{'class':'tech-mid'})
    right_news=all_news.find('div',{'class':'tech-right'})
    news1=mid_news.find('div',{'class':'tech-news'}).find_all('li')
    news2=right_news.find('div',{'class':'zl-box'}).find_all('p',{'class':'zl-tit'})
    news3=right_news.find('ul',{'class':'rank-con'}).find_all('li')

    #先爬得列表1的新闻标题及链接
    for i in news1:
        title=i.find('a').get_text()
        link=i.find('a').get('href')
        dic[title]=link


     #爬的列表2的新闻标题及链接
    for i in news2:
        link=i.find('a').get('href')
        title=i.find('a').get_text()
        dic[title]=link

     #爬取列表3的新闻标题及链接
    for i in news3:
        title=i.find('a').get_text()
        link=i.find('a').get('href')
        dic[title]=link

    return (dic)
#网页爬虫部分


def save_content(dic,str):
    '''保存内容到文件'''
    for i in dic:
        with open('news_list/{}news_list.txt'.format(str),'a') as f:
            f.write(i)
            f.write(dic[i])
            f.write('\n')
    print('{}保存成功'.format(str))
def slect_newscatgory(news,dd):
    category=news.split('htt')[0]
    #若成功调用爬虫，则返回爬虫爬到的内容
    try:
        news_list=globals().get('get_%s'%dd[category])(news.split(category)[1])#动态函数名，根据类别选择合适的爬虫
    except Exception as e:
        #logging.exception(e)
        print('{}爬虫未创建'.format(category))
    else:
        if len(news_list)==0:
            print('{}NOne'.format(category))
        else:
            save_content(news_list,category)#将爬到的内容保存到相应文件

def main():
    initializ()#初始化
    create_file()#建立文件夹
    dd={
    '科技':'tech',
    '滚动':'scroll',
    '直播':'',
    '调查':'',
    '国际':'world',
    '娱乐':'ent',
    '财经':'finance',
    '社会':'society',
    '文化':'cul',
    '军事':'mil',
    '体育':'sports',
    '专题':'',
    '政务':'gov',
    '国内':'china',
    '评论':'',
    '图片':'',
    '排行':'hotnews',
    '视频':'',
    '黑猫投诉':''

    }
    html=download_page('https://news.sina.com.cn/')
    newscategory_list=get_newscategory(html)#得到新闻类别列表
    for i in newscategory_list:
        slect_newscatgory(i,dd)
        
if __name__=='__main__':
    main()
