import requests

proxies = {
"http":  "http://scraperapi:bd525434392e073afa5bf844f79dd0f6@proxy-server.scraperapi.com:8001"

}

r= requests.get('http://httpbin.org/ip',proxies=proxies,verify=False)
print(r.text)



