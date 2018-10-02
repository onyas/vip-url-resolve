# -*- coding: utf-8 -*-
import re
import urllib.request

def getTargetUrl(url):
	requestUrl = "https://jx.618g.com/jx.php?url="+url
	#headers = ("user-agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36")
	opener = urllib.request.build_opener()
	#opener.addheaders =[headers,("refer","https://jx.618g.com/?url="+url)]
	opener.addheaders =[("user-agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"),
			    ("referer","https://jx.618g.com/?url="+url),
		            ("content-type","text/html; charset=utf-8")]
	
	urllib.request.install_opener(opener)
	data = urllib.request.urlopen(requestUrl).read().decode("utf-8")
	print(data)
	
	targetparse = '<iframe id="player".*?(https://.*?)"'
	targetUrl = re.compile(targetparse,re.S).findall(data)

	print(targetUrl)

	return targetUrl[0]
#getTargetUrl"https://jx.618g.com/?url=https://v.qq.com/x/cover/k4mutekomtrdbux/r0027sgyrx5.html?ptag=jimu.72342.zt")
