from bs4 import BeautifulSoup
import requests
import re

def htmlParser(data, domain):
    resp = requests.get(url="https://www.ps.kz/domains/whois/result", params={"q": domain})
    html = resp.text
    soup = BeautifulSoup(html, 'html.parser')
    date = soup.find(string="Дата окончания:").find_all_next(string=True)
    ExpirationDate = date[1].lstrip('\n ').rstrip(' ')
    data['ExpirationDate']=  ExpirationDate[:10]
    #data['ExpirationDateLeft']= date[2].lstrip('\n (').rstrip(' ').lstrip('(').rstrip(')')
    data['ExpirationDateLeft']= date[2].lstrip('\n (осталось').rstrip(' ').rstrip(')')

#data = []
#htmlParser(data,"ps.kz")
