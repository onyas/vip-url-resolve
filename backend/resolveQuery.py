# -*- coding: utf-8 -*-
import re
import urllib.request
import ssl
import json
from resolveUrl import getTargetUrl

#使用urllib模块访问https网站时，由于需要提交表单，而python3默认是不提交表单的，所以这时只需在代码中加上以下代码即可。
ssl._create_default_https_context = ssl._create_unverified_context

NOTFOUND = "notFound"

headers = {"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}

def queryVid(keyword):
	quote_keyword = urllib.request.quote(keyword)
	url = "https://s.video.qq.com/smartbox?plat=2&ver=0&num=10&otype=json&query=" + quote_keyword
	req = urllib.request.Request(url=url,headers=headers)
	res = urllib.request.urlopen(req).read().decode("utf-8")
	
	targetparse = 'QZOutputJson=.*?({.*?);'
	data = re.compile(targetparse,re.S).findall(res)

	data_json = json.loads(data[0])
	print(data_json)
	
	resultVids = []
	if 'item' in data_json:
		items = data_json["item"]
		for item in items:
			if 'tt' in item and item['tt']== keyword:
				print (item)
				print("\n")
				print("id="+item['id'])
				resultVids.append(item['id'])		

	return resultVids

def queryPlaySource(vid):
	url = "https://s.video.qq.com/get_playsource?plat=2&type=4&data_type=2&video_type=3&plname=qq&range=1-99&otype=json&id="+vid	
	req = urllib.request.Request(url=url,headers=headers)
	res = urllib.request.urlopen(req).read().decode("utf-8")
	
	targetParse = 'QZOutputJson=.*?({.*?);'	
	data = re.compile(targetParse,re.S).findall(res)
	
	data_json = json.loads(data[0])
	print(data_json)
	
	targetPS = []
	if 'PlaylistItem' in data_json and 'videoPlayList' in data_json["PlaylistItem"]:
		playList = data_json["PlaylistItem"]["videoPlayList"]
		print(playList)
		for pl in playList:
			if 'payType' in pl and pl["payType"] == 1:
				print(pl)
				targetPS.append(pl)
	return targetPS
	

def query(keyword):
	vids = queryVid(keyword)
	print(vids)
	targetPlaySource = []
	if len(vids) !=0 :
		for vid in vids:
			targetPS = queryPlaySource(vid)
			for playSource in targetPS:
				if 'playUrl' in playSource:
					targetUrl = getTargetUrl(playSource["playUrl"])
					playSource["targetUrl"]=targetUrl
					targetPlaySource.append(playSource)
	return targetPlaySource
