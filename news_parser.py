from bs4 import BeautifulSoup
import requests




#CBC
url_cbc = "https://www.cbc.ca/news/world"
request = requests.get(url_cbc)

soup_cbc = BeautifulSoup(request.text, "html.parser")

header_cbc = soup_cbc.find_all("div", class_="card")

for description_cbc in header_cbc:
    description_cbc = description_cbc.find("a", {'class': 'contentWrapper'})

    if description_cbc is not None:
        link_cbc = description_cbc.get('href')

    print(str(description_cbc.text) + " \n" + str("https://www.cbc.ca"+link_cbc))
    print("******************************")


#NYT
url_nyt = "https://www.nytimes.com/section/world"
request = requests.get(url_nyt)

soup_nyt = BeautifulSoup(request.text, "html.parser")

header_nyt = soup_nyt.find_all("li", class_="css-ye6x8s")

for description_nyt in header_nyt:
    description_nyt = description_nyt.find("div", {'class': 'css-1l4spti'}).find('a')

    if description_nyt is not None:
        link_nyt = description_nyt.get('href')
        print(str(description_nyt.text) + " \n" + str("https://www.nytimes.com/"+link_nyt))
        print("******************************")

#Aljazeera
url_alj = "https://www.aljazeera.com/europe/"
request = requests.get(url_alj)

soup_alj = BeautifulSoup(request.text, "html.parser")

header_alj = soup_alj.find_all("article", class_="gc")

for description_alj in header_alj:
    description_alj = description_alj.find("div", {'class': 'gc__header-wrap'}).find('a')

    if description_alj is not None:
        link_alj = description_alj.get('href')
        print(str(description_alj.text) + " \n" + str("https://www.aljazeera.com"+link_alj))
        print("******************************")















