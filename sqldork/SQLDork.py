import bs4
import urllib
import requests 
from bs4 import BeautifulSoup
import time
import sys
import random
import threading
class SQLDork:
    def __init__(self,dork='', random_user_agent=False, page=0, output='', random_dork=False):
        self._list_url = []
        self._dork = dork
        self._random_user_agent = random_user_agent
        self._page = int(page) - 1
        self._output = output
        self._random_dork = random_dork
        
        if self._random_dork == True:
            ran_dork = self.random_dork()
            print("\n{:<20}".format(" <---- Google Dork Scan ---->\n"))
            print('[*] Dork :',ran_dork)
            self.google_dork(f'inurl:{ran_dork}')
        else:
            self.google_dork(self._dork)

    def random_dork(self):
        dork = []
        with open('sqldork/data/dork.txt','r') as file:
            for data in file:
                dork.append(data.replace('\n',''))
        return random.choice(dork)
    # def random_proxy(self):
    #     prox = []
    #     with open('sqldork/data/proxy-list.txt','r') as file:
    #         for data in file:
    #             prox.append(data.replace('\n',''))
    #     return random.choice(prox) 

    def google_dork(self, dork):
        text = urllib.parse.quote_plus(dork)
        get = self.execute_dork(f'https://www.google.com/search?q={dork}&start={self._page*10}')
        return self.get_result(get)       

    def execute_dork(self,url):
        try:
            if self._random_user_agent == True:
                ua = random_user_agent()
                headers = {"user-agent":f"{ua}",'referer':'https://www.google.com/'}
                # print("[*] Search Dork..")
                res = requests.get(url, headers=headers).text
            else:
                res = requests.get(url).text
            bs = BeautifulSoup(res, "html.parser").find_all('div',class_='g')
            # print(res)
        except requests.ConnectionError as ce:
            print('[!] Error:', ce)
        except requests.RequestException as e:
            print('[!] Error:', e)
        except KeyboardInterrupt:
            print('\nBye')
            exit()
        return bs

    def get_result(self, result):
        """ Display result """
        
        twidh = 10
        for rc in result:
            time.sleep(0.2)
            print("[+] URL :",rc.a['href'])
            self._list_url.append(rc.a['href'])
        while True:
            c = input('[?] Scan ? [Y/n] ~ ')
            if c.lower() == 'y':
                self.check_vuln(self._list_url)
                exit()
            elif c.lower() == 'n':
                exit()
            else:
                print('[!] Error')

    def check_vuln(self, list_url):
        print("\n{:<20}".format(" <---- SQLi Checker ---->\n"))
        ua = random_user_agent()
        header = {"user-agent":f"{ua}",'referer':'https://www.google.com/'}
        for url in list_url:
            Check(url, header)
        return

class Check():
    # fix random agent
    def __init__(self, url, header):
        self.session = requests.Session()
        self.thread(url, header)

    def scan_sql(self, url, header='', deep=False):
        simple = ("'",'\\', "%27")
        complex = ("'", "')", "';", '"', '")', '";', '`', '`)', '`;', '\\', "%27", "%%2727", "%25%27", "%60", "%5C")
        scan = simple
        if deep == True:
            scan = complex
        x = 0
        for met in scan:
            try:
                scanurl = f"{url}{met}"
                res = self.session.get(scanurl, headers=header)
                if self.is_vuln(res):
                    print("[+] Scanning :", url)
                    print(f"{cl.gn}[*] SQL Injection vulnerability found :{cl.c}", url)
                    break
                else:
                    x += 1
                    if x == len(scan):
                        print("[+] Scanning :", url)
                        print(f"{cl.rd}[!] SQL Injection vulnerability not found : {cl.c}")
                        x = 0
            except Exception as e:
                print("{}[!] Error :{}".format(cl.rd,cl.c), e)
                return
            except KeyboardInterrupt:
                print('\nBye')
                exit()

    def thread(self, url, header):
        try:
            thread = threading.Thread(target=self.scan_sql, args=(url, header))
            thread.start()
        except KeyboardInterrupt:
            print('\nBye')

    def is_vuln(self, res):
        errors = (
                "you have an error in your sql syntax;",
                "warning:mysql",
                "unclosed quotation mark after the character string",
                "quoted string not properly terminated" 
            ) 
        # decode = res.content.decode().lower()   
        # for error in errors:
        #     if error in decode:
        #         return True
        for error in errors:
            if error in res.text.lower():
                return True
                break
        return False
def random_user_agent():
    ua = []
    with open('sqldork/data/user-agent.txt','r') as file:
        for data in file:
            ua.append(data.replace('\n','')) 
    return random.choice(ua)
   
class cl:
    gn = '\033[92m'
    c = '\033[0m'
    rd = '\033[91m'
    
"""
// random Proxy
// bing dork
// duck dork
// output file
"""