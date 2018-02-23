


'''
import urllib.request
import re
import threading
import requests

class Testip(object):
    def __init__(self):
        self.sFile = r'ip.txt'
        self.dFile = r'saveip.txt'
        self.URL = r'http://ip.chinaz.com/getip.aspx'
        self.threads = 10
        self.timeout = 3
        self.regex = re.compile(r'baidu.com')
        self.aliveList = []
        self.run()
    def run(self):
        with open(self.sFile,'r') as fp:
            lines = fp.readlines()
            line = lines.pop()
            while lines:
                for i in range(self.threads):
                    t = threading.Thread(target=self.linkWithip,args=(line,))
                    t.start()
                    if lines:
                        line = lines.pop()
                    else:
                        continue
        with open(self.dFile,'w') as fp:
            for i in range(len(self.aliveList)):
                fp.write(self.aliveList[i])

    def linkWithip(self,line):
        server = r'http://'+line[1:-2]
        #protocol = 'http'
        #opener = urllib.request.build_opener(urllib.request.ProxyHandler({protocol:server}))
        #urllib.request.install_opener(opener)
        #print(server)
        opener = urllib.request.build_opener(urllib.request.ProxyHandler({"http":server}))
        try:
            response = urllib.request.urlopen(self.URL,timeout=self.timeout)
        except:
            print('%s connect failed' % server)
            return
        else:
            try:
                str = respone.read()
            except:
                print('%s connect failed' % server)
                return
            if self.regex.search(str):
                print('%s connect success .............' %server)
                self.aliveList.append(line)
if __name__ == '__main__':
    tp = Testip()
'''
import urllib
import socket
socket.setdefaulttimeout(3)

inf = open("ip.txt")    # 这里打开刚才存ip的文件
lines = inf.readlines()
proxys = []
for i in range(0,len(lines)):
    print(lines[i])
    proxy_host = "http://" + lines[i].replace('\n','')
    proxy_temp = {"http":proxy_host}
    proxys.append(proxy_temp)

# 用这个网页去验证，遇到不可用ip会抛异常
url = "http://ip.chinaz.com/getip.aspx"
# 将可用ip写入valid_ip.txt
ouf = open("saveip.txt", "a+")

for proxy in proxys:
    try:
        res = urllib.urlopen(url,proxies=proxy).read()
        valid_ip = proxy['http'][7:]
        print ('valid_ip: ' + valid_ip)
        ouf.write(valid_ip)
    except Exception:
        print(proxy)
        continue