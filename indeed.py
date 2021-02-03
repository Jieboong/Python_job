import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = "https://kr.indeed.com/jobs?q=python&limit=50"

def get_last_page(pagination) :
    links = pagination.find_all('li')
    pages = []
    max_page = int(links[-2].string)
    return max_page

def extract_job(html) :
    title = (html.find("h2", {"class":"title"})).find("a")["title"]
    company = html.find("span", {"class":"company"})
    company_anchor = company.find("a")
    if company_anchor is not None :
        company = (str(company_anchor.string))
    else :
        company = (str(company.string))
    company = company.strip()
    location = html.find("div", {"class":"recJobLoc"})["data-rc-loc"]
    job_id = html["data-jk"]
    return {
        'title':title, 
        'company':company, 
        'location':location, 
        "link":f"https://kr.indeed.com/viewjob?jk={job_id}"
        }

def get_jobs():
    jobs = []
    start = 0
    while (True) :
        result = requests.get(f"{URL}&start={start*LIMIT}")
        soup = BeautifulSoup(result.text, "html.parser")
        pagination = soup.find("ul",{"class":"pagination-list"})
        max_page = get_last_page(pagination)
        print(f"Scrapping {start}")
        if (max_page < start) : 
            break
        start +=1
        results = soup.find_all("div", {"class":"jobsearch-SerpJobCard"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)

    return jobs