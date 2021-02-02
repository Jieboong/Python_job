import requests
from bs4 import BeautifulSoup

indeed_result = requests.get("https://kr.indeed.com/%EC%B7%A8%EC%97%85?as_and=python&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&jt=all&st=&salary=&radius=25&l=&fromage=any&limit=50&sort=&psf=advsrch&from=advancedsearch")

indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")

pagination = indeed_soup.find("ul", {"class":"pagination-list"})

links = pagination.find_all('li')
pages = []
for link in links[:-1] :
    pages.append(int(link.string))
max_page = pages[-1]

for n in range(max_page) :
    print(f"start={n*50}")