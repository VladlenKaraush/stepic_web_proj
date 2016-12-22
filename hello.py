from cgi import parse_qs

def application(environ, start_response):
        #just comment for commiting
	status = '200 OK'
        #here i declare headers of returning http request
	headers = [
	('Content-type', 'text-plain')
	]
	start_response(status,headers)
	return ["\n".join(environ["QUERY_STRING"].split("&"))]
