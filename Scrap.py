import requests
# from bs4 import BeautifulSoup

def FetchAndSave(url,path):
     page = requests.get(url)
     with open (path, "w",encoding="utf-8") as f:
          f.write(page.text)


url = "https://www.espncricinfo.com"

FetchAndSave(url,"Keeper/scrap.html")
