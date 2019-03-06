# https://drizly.com/wine/c3
import requests
import cssutils
from bs4 import BeautifulSoup
import scrapy

base_url = 'https://drizly.com/'
categories = ['wine/c3','beer/c2','liquor/c4']
wines = []
beers = []
liquor = []

# for count in range(0,416):
#     print(count)       s

# content = {
#     'img':'','title':'','price_low':0,'price_high':0
# }

def call():
    for catg in categories:
        for cnt in range (1,2):
            url = ''
            soup_content=''
            if(cnt == 1):
                url = base_url + catg
            else:
                url = base_url + catg + '/page'+str(cnt)
            if(catg == 'wine/c3'):
                soup_content = BeautifulSoup(requests.get(url).content,'lxml')
                wines.extend(soup_content.find_all("li", {'class': 'CatalogResults__CatalogListItem___2qCwP'}))

            if(catg == 'beer/c2'):
                soup_content = BeautifulSoup(requests.get(url).content,'lxml')
                beers.extend(soup_content.find_all("li", {'class': 'CatalogResults__CatalogListItem___2qCwP'}))

            if(catg == 'liquor/c4'):
                soup_content = BeautifulSoup(requests.get(url).content, 'lxml')
                liquor.extend(soup_content.find_all("li", {'class': 'CatalogResults__CatalogListItem___2qCwP'}))

        print('w',len(wines))
        print('b',len(beers))
        print('l',len(liquor))
        if(catg == 'wine/c3'):
            for link in wines[23:] :
                prod_url = base_url + link.findChildren("a")[0]['href']
                raw_page = BeautifulSoup(requests.get(prod_url).content, 'lxml')
                print('wine',raw_page.find_all('div', {
                    'class': 'ProductMeta__product-image'})[0].findChildren('img')[0]['src'])
                print('wine - title',raw_page.find_all('div', {
                    'class': 'ProductMeta__product-image'})[0].findChildren('img')[0]['src'])
        # if(catg == 'beer/c2'):
        #     for link in wines:
        #         prod_url = base_url + link.findChildren("a")[0]['href']
        #         print('beer',BeautifulSoup(requests.get(prod_url).content, 'lxml').find_all('div', {
        #             'class': 'ProductMeta__product-image'})[0].findChildren('img')[0]['src'])
        # if(catg == 'liquor/c4'):
        #     for link in wines:
        #         prod_url = base_url + link.findChildren("a")[0]['href']
        #         print('liquor',BeautifulSoup(requests.get(prod_url).content, 'lxml').find_all('div', {
        #             'class': 'ProductMeta__product-image'})[0].findChildren('img')[0]['src'])

call()
print('done')