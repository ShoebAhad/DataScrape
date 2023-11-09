import requests
from bs4 import BeautifulSoup
import pandas as pd

proxies = {
"http":  "http://scraperapi:bd525434392e073afa5bf844f79dd0f6@proxy-server.scraperapi.com:8001"

}

# r= requests.get('http://httpbin.org/ip',proxies=proxies,verify=False)
# print(r.text)




 
     
data = { "title": [],"price":[]}

url = "https://www.amazon.in/s?k=iphone&crid=LSAJ0RXFL15M&sprefix=iphon%2Caps%2C221&ref=nb_sb_ss_ts-doa-p_2_5"

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

page = requests.get(url, headers=headers)


# page = requests.get(url ,proxies=proxies)
soup= BeautifulSoup(page.text,"html.parser")
spans =soup.select("span.a-size-medium.a-color-base.a-text-normal")
prices =soup.select("span.a-price")

for span in  spans:
    print(span.string)
    data["title"].append(span.string)

for price in prices:
    if not("a-text-price" in price.get("class")):
       print(price.find("span").get_text())
    data["price"].append(price.find("span").get_text())
    if(len(data["price"])==len(data["title"])):
        break

df=pd.DataFrame.from_dict(data)
df.to_csv("data.csv",index=False)

