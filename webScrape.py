import requests
from bs4 import BeautifulSoup

url_map = {
    'moon': "https://www.asc-csa.gc.ca/eng/multimedia/search/image/8382#longdesc",
    'mars': "https://www.asc-csa.gc.ca/eng/multimedia/search/image/4982#longdesc",
    'mercury': "https://www.asc-csa.gc.ca/eng/multimedia/search/image/11919#longdesc",
    'venus': "https://www.asc-csa.gc.ca/eng/multimedia/search/image/11920#longdesc",
    'jupiter': "https://www.asc-csa.gc.ca/eng/multimedia/search/image/15251#longdesc",
    'saturn': "https://www.asc-csa.gc.ca/eng/multimedia/search/image/15252#longdesc",
    'uranus': "https://www.asc-csa.gc.ca/eng/multimedia/search/image/17479#longdesc",
    'neptune': "https://www.asc-csa.gc.ca/eng/multimedia/search/image/17477#longdesc"
}

planet_list = ["moon", "mercury", "venus", "jupiter", "saturn", "uranus", "neptune"]
extracted_text = []

for planetName in planet_list:
    url = url_map[planetName]
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    final_str = ""

    for details in soup.find_all('details'):
        ul = details.find('ul')
        if ul:
            for li in ul.find_all('li'):
                final_str += li.get_text() + "\n"

    with open(planetName + '.txt', 'w', encoding='utf-8') as f:
        f.write(final_str)



