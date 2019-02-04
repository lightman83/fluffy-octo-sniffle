import socket

# This program simply makes an HTTP request to google and prints out the response

target_host = 'www.google.com'
target_port = 80

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((target_host, target_port))

client.send(b"GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n")

response = client.recv(4096)

print(response)
