import http.server
import socketserver
port=1145 #埠
directory='./' #訪問當前資料夾
handler=http.server.SimpleHTTPRequestHandler
httpd=socketserver.TCPServer(("", port),handler)
print("serving at port ",port)
httpd.serve_forever()