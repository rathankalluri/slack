"""
import requests, time
data = {"token": "Jhj5dZrVaK7ZwHHjRyZWjbDl","challenge": "3eZbrw1aBm2rZgRNFdxV2595E9CY3gmdALWMmHkvFXO7tYXAYM8P","type": "url_verification"}

r = requests.post('https://slackhrbot.herokuapp.com/webhook.py', data=data)
print r.status_code
print r.content
"""

import http.server
import socketserver

import requests

Handler = http.server.SimpleHTTPRequestHandler

def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

def do_POST(self):
	

def run():

	with socketserver.TCPServer(("", 8080), Handler) as httpd:
		print("serving at port", 8080)
		httpd.serve_forever()

run()
		
"""
class Handler(http.server.SimpleHTTPRequestHandler):

    def do_POST(self):
		
		
		data = request.POST
		if data["challenge"]:
			self.send_response(200)
			return data["challenge"]
		else:
			return "Error!!"
"""
