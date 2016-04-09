import urllib2, httplib
request = urllib2.Request('http://xxxx.com')
request.add_header('Accept-encoding', 'gzip')        1
opener = urllib2.build_opener()
f = opener.open(request)
