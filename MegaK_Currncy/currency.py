from bs4 import BeautifulSoup
import requests

def f(link):
    dollar_rub = link
    
    full_page = requests.get(dollar_rub, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
    return convert
