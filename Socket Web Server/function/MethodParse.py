import socket
import config
from function.response import *

#Get request from client
def getRequest(client):
	request = ''
	client.settimeout(1)

	try:
		#receive request
		request = client.recv(1024).decode()
		while (request):
			request += client.recv(1024).decode()
	except socket.timeout:
		#if timedout
		if not request:
			print("-------------------\n [SERVER]\n No request from client")
	finally:
		#parse the request for better using
		return RequestParse(request)

class RequestParse:
	def __init__(self, request):
		#print(request)
		requestArray = request.split("\n")
		#print(requestArray)
		if request == "":
			self.empty = True	#if there is no request content
		else:
			self.empty = False
			self.method = requestArray[0].split(" ")[0]		#get method
			self.path = requestArray[0].split(" ")[1]		#get path
			self.content = requestArray[-1]					#get request content
		
		'''print(self.content)
		print(self.path)'''	

#POST Method Parser
def postMethod(client, request):
	#scan login content or return info.html or return 404.html

	if(request.path in ['/files.html?','/files.html']):
		f = open('block.txt',"w")
		f.write("True");
		f.close();
		client.sendall("HTTP/1.1 301 MOVED PERMANENTLY\nLOCATION: /files.html\n".encode('utf-8'))
		client.sendall(Response("/html/files.html").makeResponse())
		return

	if(request.path in ['/info.html?','/info.html'] and request.content == "Username=%s&Password=%s"%(config.username,config.password)):
		client.sendall("HTTP/1.1 301 MOVED PERMANENTLY\nLOCATION: /info.html\n".encode('utf-8'))
		client.sendall(Response("/html/info.html").makeResponse())
		f = open('block.txt',"w")
		f.write("True");
		f.close();
		return

	if(request.path in ['/info.html?','/info.html'] and request.content == ''):
		client.sendall("HTTP/1.1 301 MOVED PERMANENTLY\nLOCATION: /info.html\n".encode('utf-8'))
		client.sendall(Response("/html/info.html").makeResponse())
		f = open('block.txt',"w")
		f.write("True");
		f.close();
		return

	else:
		client.sendall("HTTP/1.1 301 MOVED PERMANENTLY\nLOCATION: /404.html\n".encode('utf-8'))
		client.sendall(Response("/html/404.html").makeResponse())
		return


#GET method parser
def getMethod(client, request):

	#if not "GET" method, abort 
	if request.method != 'GET':
		return

	f = open('block.txt',"r")
	check = f.read();
	f.close()
	#print(check)

	#Block access to page if not access via login form
	if(check == "False"):
		if (request.path in ['/files.html','/info.html','/info.html?','/files.html?']):
			request.path = config.get_404

	f = open('block.txt',"w")
	f.write("False")
	f.close()

	#Return to homepage first time connect
	if request.path in ['/','/index.html?']:
		request.path = config.get_index

	#print(request.path)
	
	#input the file path to send to to client
	client.sendall(Response(request.path).makeResponse())
	print(f"-------------------\n [SEND RESPONSE]\n Package for {Response(request.path).locOf_file} sent")