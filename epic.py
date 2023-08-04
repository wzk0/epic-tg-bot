import os
from bs4 import BeautifulSoup
import requests

headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0'}

def req(link):
	r=requests.get(link,headers=headers)
	soup=BeautifulSoup(r.text,features='html5lib')
	return soup

def get_xi():
	data_list=[]
	for tr in req('https://steamstats.cn/xi').find('tbody').find_all('tr'):
		td_list=tr.find_all('td')
		name=td_list[1].find('a')['title']
		link=td_list[1].find('a')['href']
		start_time=td_list[3].text.replace(' ','').replace('\n','')
		end_time=td_list[4].text.replace(' ','').replace('\n','')
		forever=td_list[5].text.replace(' ','').replace('\n','')
		via=td_list[6].text.replace(' ','').replace('\n','')
		data_list.append({'name':name,'start_time':start_time,'end_time':end_time,'forever':forever,'via':via,'link':link})
	return data_list