#! /usr/bin/env python
# -*- coding:utf-8 -*-
import requests
from lxml import etree
import json

for i in range(10):
	url = 'https://movie.douban.com/top250?start={}'.format(i*25)
	data = requests.get(url).text
	f = etree.HTML(data)
	films = f.xpath('//*[@id="content"]/div/div[1]/ol/li')
	for div in films:
		name = div.xpath('./div/div[2]/div[1]/a/span[1]/text()')[0]
		#introduction=div.xpath('./div/div[2]/div[2]/p[1]/text()')
		href = div.xpath('./div/div[2]/div[1]/a/@href')[0]
		d_film=requests.get(href).text
		df=etree.HTML(d_film)
		intro=df.xpath('//*[@id="info"]')
		# import pdb; pdb.set_trace()
		for intr in intro:
			#import pdb; pdb.set_trace()
			director=intr.xpath('./span[1]/span[2]/a/text()')
			playwright=intr.xpath('./span[2]/span[2]/text()')
			actor=intr.xpath('./span[3]/text()')
			ondate=intr.xpath('./span[11]/text()')
			timing=intr.xpath('./span[13]/text()')
		rank = div.xpath('./div/div[2]/div[2]/div/span[2]/text()')[0]
		comment = div.xpath('./div/div[2]/div[2]/p[2]/span/text()')

		if len(comment)>0:
			print('{} {} {} {} {}\n'.format(name,director,playwright,actor,ondate,timing,rank,href,comment))
		else:
			print('{} {} {} {}\n'.format(name,director,playwright,actor,ondate,timing,rank,href))
		print('\n')

		with open("top250films.json","a",encoding='utf-8') as f:
			f.write("影片名称：%s\n导演：%s\n编剧：%s\n演员：%s\n上映日期：%s\n片长：%s\n评分：%s\n链接：%s\n短评：%s\n"%(name,director,playwright,actor,ondate,timing,rank,href,comment))
			f.write("\n")

