# Update: 21.02.2019
# What's new?
# Added threading in each requests to speed up the script
# Added custom number of proxies generation capability
import threading
import socket
import urllib
from time import sleep
socket.setdefaulttimeout(5)

class StartThread(threading.Thread):
    def __init__(self, target, *args):
        self._target = target
        self._args = args
        threading.Thread.__init__(self)
 
    def run(self):
        self._target(*self._args)

def collect(i, target_source,):
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

def execute():
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
        t1 = StartThread(collect, i, target_source)
        t1.start()
        t1.join()

times = raw_input('How many times to run the collector?(Each time upto 35 proxies):\n')
for i in range(int(times)):
    execute()
    sleep(1)
