###############################################################################################################
## 
## Multithreaded Python server with socket for Aareeys TCP Server Socket Program Stub
## Aareys => Associative Array REgistry Yanking Service
##
##
## Conceptualised, Designed and Developed by : Abirlal Biswas
## Start Date : November 1, 2018
## Email : abirlalbiswas@gmail.com
##
###############################################################################################################




import sys
import socket
import json
from threading import Thread
from socketserver import ThreadingMixIn

#from SocketServer import ThreadingMixIn for python 2.6.x

import System
import UrlRequest
import Actions



# Multithreaded Python server : TCP Server Socket Program Stub
TCP_IP = '127.0.0.1'
TCP_PORT = 2019
LISTENER_SIZE = 10
BUFFER_SIZE = 20  # Usually 1024, but we need quick response

LOG_ENTRY = True


# Multithreaded Python server : TCP Server Socket Thread Pool
class ClientThread(Thread):
        def __init__(self, ip, port):
                Thread.__init__(self)
                self.ip = ip
                self.port = port
                print ("[+] New server socket thread started for " + ip + ":" + str(port))

        def run(self):
                if True:
                        try:	
                                clientmessage = conn.recv(2048).decode('utf-8')
                                #print ("Server received data:", clientmessage)
                                if (clientmessage!=''):
                                        reqString = clientmessage.split() # get the /filename from the string
                                        #print(reqString)
                                        reqType = reqString[0]
                                        urlPath = reqString[1][1:]
                                        urlPaths = urlPath.split('/')
                                        #print("Request Type:" + reqType) # for debugging
                                        print (urlPaths)
                                        urlPathsLength =  len(urlPaths)
                                        if urlPathsLength > 2:
                                                action = UrlRequest.urlPatterns[urlPaths[0] + '/' + urlPaths[1] + '/'] 
                                                if reqType == 'GET':
                                                        try:
                                                                if urlPathsLength > 4:
                                                                        name = urlPaths[2]
                                                                        data = "/".join(urlPaths[3:])
                                                                        print ('Call Type 3: ', action, name, data)
                                                                        result = getattr(Actions, action)(system, name, data)
                                                                elif urlPathsLength == 4:
                                                                        name = urlPaths[2]
                                                                        print ('Call Type 2:', action, name)
                                                                        result = getattr(Actions, action)(system, name)
                                                                elif urlPathsLength == 3:
                                                                        print ('Call Type 1:', action)
                                                                        result = getattr(Actions, action)(system)
                                                                else:
                                                                        pass
								#result = "{\"Status\":\"Error\", \"Response\":\"No Action Found\"}"
                                                        except IndexError:
                                                                pass
                                                elif reqType == 'POST':
                                                        try:
                                                                data = reqString[13]
                                                                result = getattr(Actions, action)(system, name, data)
                                                        except IndexError:
                                                                pass
                                                else:
                                                        pass
                                                res = "{\"response\":" + json.dumps(result) + "}"
                                        else:
                                                res = "{\"response\":{\"Status\":\"Error\", \"Response\":\"Please check the TLD of URL...!!\"}}"
                                else:
                                        res = "{\"response\":{\"Status\":\"Error\", \"Response\":\"No client message is Recevied to server end..!!\"}}"
                                
                                response = "HTTP/1.1 400 OK\r\nServer: AaReyS-Server/1.1\r\nDate: Tue, 05 Feb 2013 03:36:18 GMT\r\nVary: Accept-Charset, Accept-Encoding, Accept-Language, Accept\r\nAccept-Ranges: bytes\r\nAccess-Control-Allow-Origin: *\r\nAccess-Control-Allow-Methods: POST,OPTIONS,GET\r\nAccess-Control-Allow-Headers: Content-Type\r\nServer: Restlet-Framework/2.0m5\r\nContent-Type: application/json;charset=UTF-8\r\nContent-Length: " + str(len(res)) + "\r\n\r\n" + res
                                conn.sendall(response.encode('utf-8'))# 404, send to client
                                print ('Response:Sent to client....')
                                print ("--------------------------------------------------------------------------")
                                conn.close() # close client socket
                        except Exception as e:
                                print (e)
                                res = "{\"response\":{\"Status\":\"Error\", \"Response\":\"" + str(e) + "\"}}"
                                response = "HTTP/1.1 400 OK\r\nServer: AaReyS-Server/1.1\r\nDate: Tue, 05 Feb 2013 03:36:18 GMT\r\nVary: Accept-Charset, Accept-Encoding, Accept-Language, Accept\r\nAccept-Ranges: bytes\r\nAccess-Control-Allow-Origin: *\r\nAccess-Control-Allow-Methods: POST,OPTIONS,GET\r\nAccess-Control-Allow-Headers: Content-Type\r\nServer: Restlet-Framework/2.0m5\r\nContent-Type: application/json;charset=UTF-8\r\nContent-Length: " + str(len(res)) + "\r\n\r\n" + res
                                conn.sendall(response.encode('utf-8'))# 404, send to client
                                conn.close() 



def main():
	global system
	global conn
	system = System.Registry()

	tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	tcpServer.bind((TCP_IP, TCP_PORT))
	threads = []
	print ("\n***** AaReyS SErver Confuguration ***** \n")
	print ("Server Started ...\n")
	print ("IP Address(Default 127.0.0.1): " + TCP_IP )
	print ("PORT(Default 2019): "  + str(TCP_PORT))
	print ("Buffer Size(Default 20): " + str(BUFFER_SIZE))
	print ("Listner Size(Default 10): " + str(LISTENER_SIZE))
	print ("Server URL: http://" + TCP_IP + ":" + str(TCP_PORT) + "/ \n")

	while True:
        	tcpServer.listen(LISTENER_SIZE)
        	print ("Waiting for connections from TCP clients..." )
        	(conn, (ip,port)) = tcpServer.accept()
        	newthread = ClientThread(ip,port)
        	newthread.start()
        	threads.append(newthread)

	for t in threads:
        	t.join()

if __name__ == '__main__':
	if len (sys.argv) == 3 :
		TCP_IP = sys.argv[1]
		TCP_PORT = int(sys.argv[2])
	main()
