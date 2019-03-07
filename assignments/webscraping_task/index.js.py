# https://drizly.com/wine/c3
import requests
from bs4 import BeautifulSoup
import time


base_url = 'https://drizly.com/'
categories = ['wine/c3', 'beer/c2', 'liquor/c4']
wines = []
beers = []
liquor = []
myFile = open('drizly.csv', 'w')
myFile.write("CATEGORY, TITLE, LOW, HIGH,URL\n")

def prep_links(catg):
    for cnt in range(1, 417):
        url = ''
        if (cnt == 1):
            url = base_url + catg
        else:
            url = base_url + catg + '/page' + str(cnt)
        soup_content = BeautifulSoup(requests.get(url).content, 'lxml')
        # print('req1 start')
        time.sleep(2)
        # print('continue1')
        if (catg == 'wine/c3'):
            wines.extend(soup_content.find_all("li", {'class': 'CatalogResults__CatalogListItem___2qCwP'}))

        if (catg == 'beer/c2'):
            beers.extend(soup_content.find_all("li", {'class': 'CatalogResults__CatalogListItem___2qCwP'}))

        if (catg == 'liquor/c4'):
            liquor.extend(soup_content.find_all("li", {'class': 'CatalogResults__CatalogListItem___2qCwP'}))
def writetocsv(list_,category):
    for link in list_:
        prod_url = base_url + link.findChildren("a")[0]['href']
        raw_page = BeautifulSoup(requests.get(prod_url).content, 'lxml')
        # print('req2 start')
        time.sleep(2)
        # print('continue2')
        try:
            url = raw_page.find_all('div',{'class': 'ProductMeta__product-image'})[0].findChildren('img')[0]['src']
        except:
            url = ''
        try:
            title = raw_page.find_all('h1')[0].get_text().strip()
        except:
            title = ''
        try:
            low = raw_page.findChildren('span', {'class': 'value'})[0].get_text().replace(" ", "").split('-')[0][1:]
        except:
            low = 0
        try:
            high = raw_page.findChildren('span', {'class': 'value'})[0].get_text().replace(" ", "").split('-')[1][1:]
        except:
            high = 0
        # print('low,high,url,title',low,high,url,title)
        myFile.write(category+","+title+"," +str(low)+","+str(high)+","+url+"\n")

        # with myFile:
        #     myFields =
        #     writer = csv.DictWriter(myFile, fieldnames=myFields)
        #     writer.writeheader()
        #     writer.writerow({'TITLE': title, 'CATEGORY': 'WINE', 'LOW': low, 'HIGH': high, 'URL': url})
def taskforce():
    for catg in categories:
        prep_links(catg)
        if (catg == 'wine/c3'):
            print('wine', len(wines))
            writetocsv(wines,'WINE')
        if(catg == 'beer/c2'):
            print('beer', len(beers))
            writetocsv(beers,'BEER')
        if(catg == 'liquor/c4'):
            print('liquor', len(liquor))
            writetocsv(liquor,'LIQUOR')
taskforce()

print('done')
