# Shahriyar Mammadli
# Class to obtain proxies from www.sslproxies.org
# Import required libraries
import requests
from bs4 import BeautifulSoup
import random
import ProxyItem

# Class
class SSLProxy(object):
    # Initialize the prerequisite items
    def __init__(self, recentlyChecked=False):
        self.URL = 'https://www.sslproxies.org/'
        self.headers = {
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'en-US,en;q=0.8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Connection': 'keep-alive',
            }
        self.ProxyItems = []
        SSLProxy.__proxyList(self, recentlyChecked)

    # Proxy List
    def __proxyList(self, recentlyChecked):
        # Connect to the url
        req = requests.get(url=self.URL, headers=self.headers)
        soup = BeautifulSoup(req.text, 'html.parser')
        # Retrieve to obtain the proxy list
        body = soup.find('tbody')
        # Get the proxy data iteravtively
        for x in body.findAll('tr'):
            if(recentlyChecked):
                dateType = ""
                if (x.findAll('td')[7].get_text().split(" ")[1][len(x.findAll('td')[7].get_text().split(" ")[1]) - 1] == 's'):
                    dateType = x.findAll('td')[7].get_text().split(" ")[1][0:len(x.findAll('td')[7].get_text().split(" ")[1]) - 1]
                else:
                    dateType = x.findAll('td')[7].get_text().split(" ")[1]
                if(dateType == "second"):
                    self.ProxyItems.append(ProxyItem.ProxyItem(x.findAll('td')[0].get_text(), x.findAll('td')[1].get_text(),
                                                 x.findAll('td')[3].get_text(), x.findAll('td')[4].get_text(),
                                                 x.findAll('td')[7].get_text()))
                elif(dateType == "minute" and x.findAll('td')[7].get_text().split(" ")[0] == "1"):
                    self.ProxyItems.append(ProxyItem.ProxyItem(x.findAll('td')[0].get_text(), x.findAll('td')[1].get_text(),
                                                 x.findAll('td')[3].get_text(), x.findAll('td')[4].get_text(),
                                                 x.findAll('td')[7].get_text()))

            else:
                self.ProxyItems.append(ProxyItem.ProxyItem(x.findAll('td')[0].get_text(), x.findAll('td')[1].get_text(),
                                                           x.findAll('td')[3].get_text(), x.findAll('td')[4].get_text(),
                                                           x.findAll('td')[7].get_text()))
    # Get Proxies
    def getProxyList(self):
        return self.ProxyItems

    # Get a random proxy item
    def getRandomProxyObject(self):
        return self.ProxyItems[random.randint(0,len(self.ProxyItems)-1)]

    # Get a random proxy adress
    def getRandomProxyAdress(self):
        randIndex = random.randint(0,len(self.ProxyItems)-1)
        return "{}:{}".format(self.ProxyItems[randIndex].getIp(),
                              self.ProxyItems[randIndex].getPort())
