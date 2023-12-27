import socket

def scan_port(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((host, port))
    s.close()
    return result == 0

host = 'website.com'
for port in range(1, 65536):
    if scan_port(host, port):
        print('Port', port, 'is open')
