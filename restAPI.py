# -*- coding: utf-8 -*-

from flask import Flask,request,jsonify,make_response,render_template
from resolveUrl import getTargetUrl
from resolveQuery import query

app = Flask(__name__)


@app.route('/search',methods=['GET'])
def search():
	name = request.args.get('q')
	print(name)
	result = query(name)
	if len(result) == 0:
		res = make_response(jsonify({'message':'not support','data':''}) )
	else:
		res =  make_response(jsonify(result))
	
	res.headers['Access-Control-Allow-Origin'] = '*'
	res.headers['Access-Control-Allow-Methods'] = 'GET'
	res.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type' 
	return res;

@app.route('/parseUrl', methods=['GET'])
def parseUrl():
	sourceUrl = request.args.get('sourceUrl')
	print (sourceUrl)	
	
	if 'https://v.qq.com' in sourceUrl:
		targetUrl = getTargetUrl(sourceUrl)
		return jsonify({'message':'success','data':targetUrl})
	else:
		return jsonify({'message':'not support','data':''})

@app.route('/', methods=['GET'])
def index():
	return render_template('index.html')

if __name__ == '__main__':
    app.run(
	host = '0.0.0.0',
	port=environ.get("PORT", 6789)
	)
