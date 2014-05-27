# Create your views here.
from django.http import HttpResponse
from karandeepcom.settings import STATIC_URL
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
import json, requests



def home(request, template_name="thebigsmallgif/gifs.html", extra_context=None):
	if request.GET.get('query') == None or request.GET.get('query') == "":
		query = "lol"
	else:
		query = request.GET.get('query')

	print "size =", request.GET.get('size')
	if request.GET.get('size') == None or request.GET.get('size')=="":
		size = 500
	else:
		size = request.GET.get('size')

	if request.GET.get('offset') == None or request.GET.get('offset') == "":
		offset = 0
	else:
		offset = request.GET.get('offset')

	if request.GET.get('refresh') == None:
		refresh = "no"
	else:
		template_name = "thebigsmallgif/gif_entry.html"

	print "query = ", query
	print "size = ", size
	print "offset = ", offset
 	gifdata,offset = getGifs(query,size,offset)
 	print "new offset = ", offset
	gif_data = []
	for gif in gifdata:
		data = []
		url =  str(gif['images']['original']['url'])
		gif_size =  int(gif['images']['original']['size'])/1024
		giphyurl = str(gif['url'])
		gif_data.append({'url':url,'gif_size':gif_size,'giphyurl':giphyurl})
	return render_to_response(template_name,{'STATIC_URL':STATIC_URL,'gif_data':gif_data,'offset':offset,'query':query,'size':size, 'js':"thebigsmallgif/more.js"},RequestContext(request))

def getGifs(query,size,offset):
	gifdata = []
	api = "http://api.giphy.com"
	endpoint = "/v1/gifs/search"
	offset_multiple = 50
	api_key = "dc6zaTOxFJmzC"
	amount_of_requests = 0
	offset = int(offset)
	while len(gifdata) < 10 and amount_of_requests < 20:
		params = dict(q=query,offset=offset,limit=offset_multiple,api_key=api_key)
		resp = requests.get(url=api+endpoint, params=params)
		data = resp.json()
		print data['pagination']
		for gif in data['data']:
			if int(int(gif['images']['original']['size'])/1024) < int(size) and len(gifdata) < 10:
				gifdata.append(gif)
			offset = offset + 1
		amount_of_requests = amount_of_requests + 1
		print amount_of_requests
	print "offset in the getGifs function", offset
	return [gifdata,offset]

