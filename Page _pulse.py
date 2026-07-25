import requests
from bs4 import BeautifulSoup

def analyze(url):

    html=requests.get(url).text

    soup=BeautifulSoup(html,"html.parser")

    title=soup.title.string if soup.title else ""

    meta=soup.find("meta",attrs={"name":"description"})

    h1=len(soup.find_all("h1"))

    images=len(soup.find_all("img"))

    alt=len([i for i in soup.find_all("img") if i.get("alt")])

    score=100

    if title=="":
        score-=20

    if meta is None:
        score-=20

    if h1==0:
        score-=20

    if images!=alt:
        score-=20

    return{
        "title":title,
        "h1":h1,
        "images":images,
        "images_with_alt":alt,
        "seo_score":score
  }
