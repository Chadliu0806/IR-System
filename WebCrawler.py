import requests
from bs4 import BeautifulSoup

def web_crawler():
    
    response = requests.get("https://www.cnbc.com/2021/11/23/business-vaccine-mandate-biden-administration-asks-court-to-lift-pause-.html")
    
    soup = BeautifulSoup(response.text, "html.parser")
    print(soup.prettify())  