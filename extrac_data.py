import requests
from bs4 import BeautifulSoup
proxies = {'http': 'opengate.br.scania.com:3128', 'https': 'opengate.br.scania.com:3128'}
url = 'https://www.yellowpages.com/search?search_terms=barber+shop&geo_location_terms=Miami'

r = requests.get(url=url, proxies=proxies)

soup = BeautifulSoup(r.text)
g_data = soup.find_all('div', {'class': 'result'})
for item in g_data:
    name = item.contents[0].find('a', {'class': 'business-name'})
    web_site = item.contents[0].find('a', {'class': 'track-visit-website'})
    if web_site != None:
        print(f"Name: {name.text}, Site: {web_site.get('href')}")