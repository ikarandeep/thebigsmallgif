# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
import json, requests




def home(request, slug="none", size=500, template_name="thebigsmallgif/gifs.html"):
	print "slug = ", slug
	print "size = ", size
	gifdata = getGifs(slug,size)
	gif_data = []
	for gif in gifdata:
		data = []
		url =  str(gif['images']['original']['url'])
		size =  int(gif['images']['original']['size'])/1024
		giphyurl = str(gif['url'])
		gif_data.append({'url':url,'size':size,'giphyurl':giphyurl})
	return render_to_response(template_name,{'gif_data':gif_data},RequestContext(request))

def getGifs(slug,size):
	gifdata = []
	api = "http://api.giphy.com"
	endpoint = "/v1/gifs/search"
	query = slug
	offset = 0
	offset_multiple = 10
	api_key = "dc6zaTOxFJmzC"
	i = 0
	while len(gifdata) < 10 and i < 10:
		params = dict(q=query,offset=offset,limit=offset_multiple,api_key=api_key)
		resp = requests.get(url=api+endpoint, params=params)
		data = resp.json()
		for gif in data['data']:
			print int(int(gif['images']['original']['size'])/1024)
			print size
			if int(int(gif['images']['original']['size'])/1024) < int(size):
				gifdata.append(gif)
		offset = offset+offset_multiple
		i = i + 1
	return gifdata

