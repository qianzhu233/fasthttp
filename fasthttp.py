import http.server
import socketserver
import socket

ip=socket.gethostbyname(socket.gethostname()) #裝置的IP位址
port=1145 #埠
directory='./' #訪問當前資料夾

handler=http.server.SimpleHTTPRequestHandler
httpd=socketserver.TCPServer(("", port),handler)
print("serving at ",ip,":",port,sep="") #提示使用者位址
httpd.serve_forever() #開始