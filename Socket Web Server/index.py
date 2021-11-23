import socket
import config
from function.MethodParse import *

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

server.bind(('localhost', config.port))
server.listen(5)
print("-------------------\n [SERVER]\n Listening on: %s:%d"%(config.host,config.port))

while 1:

	#Server things
	(client, address) = server.accept()

	print(f"-------------------\n [SERVER]\n {address} sent request to server.")

	#Get request
	request = getRequest(client)

	if not request.empty: 
		print(f"-------------------\n [LISTENED REQUEST]\n Request catched: %s with %s has content %s\n"%(request.method, request.path, request.content))
		if request.method == "POST":
			postMethod(client, request)
		else:
			getMethod(client, request)

	client.shutdown(socket.SHUT_RD)
	print("\n--------[Request done]--------\n\n")
	
client.close()
