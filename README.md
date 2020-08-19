# SSLProxies
SSLProxies is a project(library) to obtain a proxy adress from the www.sslproxies.org.  
**NOTE:** It is important to know that some proxies may not work due to heavy load, being outdated, or some other internal problems. Thus, it is recommended to iteratively retrieve couple of proxies to receive smoothly working one.
## Prerequisites
These libraries are needed to be installed:  
* bs4  
* requests  

## Classes

### SSLProxy(recentlyChecked=False)
SSLProxy provides proxies in different format.  
  
* recentlyChecked is an optional parameter for retrieving only recently checked or controlled proxy adresses, i.o.w. these are up-to-date adresses which has more probablity of working normally.  
* getProxyList() - returns long list of **ProxyItem**s  
* getRandomProxyObject - returns single random **ProxyItem**  
* getRandomProxyAdress - returns single random proxy adress in the format of ip:port (e.g. 000.000.000.000:0000)  

### ProxyItem
ProxyItem is an object class for proxies.  
  
* getIp() - returns ip adress of **ProxyItem**  
* getPort() - returns port number of **ProxyItem**  
* getCountry() - returns country origin of **ProxyItem**  
* getAnonymityType() - returns anonymity level of **ProxyItem**  
* getLastChecked() - returns last check time of **ProxyItem**  

## Example Usage
Example code performs a retrieval of up-to-date proxy address and then connects to https://jsonip.com (The website returns the ip adress of the client) with that proxy.
```python
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
```
