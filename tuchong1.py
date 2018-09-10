import requests,time,re
from bs4 import BeautifulSoup
def download_picture(url):
    '''下载图片'''
    r=requests.get(url)
    with open('{}'.format(url.split('/')[-1]),'wb') as f:
    	f.write(r.content)
def create_dir():
  '''创建本地文件夹'''
	if not os.path.exist('/pic'):
		os.path.mkdir('/pic')

def download_page(url):
    '''下载网页'''
	res=requests.get(url)
	return res.text
def get_pic_list(res):
'''分析网页，得到图片下载链接'''
	soup=BeautifulSoup(res,'html.parser')
	list=soup.find_all('img')
	list=[i.get('src') for i in list]
	for i in list:
		if not re.match(r'.jpg$',i):
			list.remove(i)#此处出现一个问题，不能删除最后一项
	for i in list:
	    if i.find(r'.jpg')==-1:
	        list.remove(i)
	return list
def main():
	url='http://tuchong.com/1166544/21207709/'
	res=download_page(url)
	list=get_pic_list(res)
	for url in list:
		download_picture(url)
		time.sleep(1)
if __name__=='__main__':
	main()
