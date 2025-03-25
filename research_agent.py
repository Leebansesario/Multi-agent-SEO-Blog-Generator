import requests
from bs4 import BeautifulSoup

def fetch_trending_topics():
    url = "https://www.hrmagazine.co.uk/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    topics = [h2.text for h2 in soup.find_all("h2")[:5]]
    return topics

if _name_ == "_main_":
    print(fetch_trending_topics())
