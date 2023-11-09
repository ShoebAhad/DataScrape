import requests
from bs4 import BeautifulSoup
with open ("sample.html","r") as f:
    docs_read = f.read()

soup= BeautifulSoup(docs_read,"html.parser")
# print(soup.prettify())
print(soup.findAll("div")[0])