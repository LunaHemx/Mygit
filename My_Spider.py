#! /usr/bin/env python
# -*- coding:utf-8 -*-
import requests
from lxml import etree

for i in range(10):
	url = 'https://movie.douban.com/top250?start={}'.format(i*25)
	data = requests.get(url).text
	f = etree.HTML(data)
	films = f.xpath('//*[@id="content"]/div/div[1]/ol/li')
	for div in films:
		name = div.xpath('./div/div[2]/div[1]/a/span[1]/text()')[0]
		introduction=div.xpath('./div/div[2]/div[2]/p[1]/text()')
		href = div.xpath('./div/div[2]/div[1]/a/@href')[0]
		rank = div.xpath('./div/div[2]/div[2]/div/span[2]/text()')[0]
		comment = div.xpath('./div/div[2]/div[2]/p[2]/span/text()')

		if len(comment)>0:
			print('{} {} {} {} {}\n'.format(name,introduction,rank,href,comment))
		else:
			print('{} {} {} {}\n'.format(name,introduction,rank,href))
		print('\n')

		with open("top250films.txt","a",encoding='utf-8') as f:
			f.write("影片名称：%s\n简介：%s\n评分：%s\n链接：%s\n短评：%s\n"%(name,introduction,rank,href,comment))
			f.write("\n")
