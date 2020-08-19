import SSLProxy
import requests
# Creates longlist of proxies
# proxyObj = SSLProxy.SSLProxy()
# Creates only up-to-date proxies
proxyObj = SSLProxy.SSLProxy(recentlyChecked=True)
proxy = proxyObj.getRandomProxyAdress()
httpText = 'http://' + str(proxy)
httpsText = 'https://' + str(proxy)
proxyText = {'http': httpText, 'https': httpsText}
print(proxyText)
s = requests.session()
proxies = proxyText
s.proxies.update(proxies)
print(s.get('https://jsonip.com').content)
