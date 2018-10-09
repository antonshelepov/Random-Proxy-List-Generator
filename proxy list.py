import socket
import urllib
socket.setdefaulttimeout(15)
open('IPList.txt', 'a+').close()
try:
    target_source = urllib.urlopen('https://www.proxynova.com/proxy-server-list/').read()
except:
    print 'Target server unreachable ...\nHalting ...'
    exit(0)
hosts = target_source.split('abbr title="')
lop = 0
for i in hosts:
    lop += 1
    if lop == 1:
        continue
    host = i.split('"')[0]
    port = ''
    try:
        port = i.split('proxies">')[1].split('<')[0]
    except:
        i = i.split('\n')
        port = i[3].replace('\t', '').strip(' ')
    try:
        ip = socket.gethostbyname(host)
        server = ip + ':' + port
        server = server.strip(' ')
        if server not in open('IPList.txt', 'r').read():
            open('IPList.txt', 'a+').write(server + '\n')
            print server
    except:
        pass
