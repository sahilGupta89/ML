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
#     print(count)

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
                print(base_url,catg,cnt)
                url = base_url + catg + '/page'+str(cnt)
                print('val',url)
            if(catg == 'wine/c3'):
                soup_content = BeautifulSoup(requests.get(url).text,'lxml')
                links = soup_content.find_all("li",{'class':'CatalogResults__CatalogListItem___2qCwP'})
                wines.extend(links)
                print(soup_content.select('div.style'))
                # if(catg == 'beer/c2'):
                #     beers.extend(BeautifulSoup(requests.get(url).text, 'lxml').find_all("li", {
                #         'class': 'CatalogResults__CatalogListItem___2qCwP'}))
                # if(catg == 'liquor/c4'):
                #     liquor.extend(BeautifulSoup(requests.get(url).text, 'lxml').find_all("li", {
                #         'class': 'CatalogResults__CatalogListItem___2qCwP'}))
            for link in wines:
                children = link.findChildren("div", {'class': 'CatalogItem__CatalogItemImage___32wLN'},
                                            recursive=True)
                print(children[0]['style'])


call()

# wine = requests.get(base_url + 'wine/c3')
# beer = requests.get('https://drizly.com/beer/c2')
# liquor = requests.get('https://drizly.com/liquor/c4')

# soup_wine = BeautifulSoup(wine.text,'lxml')
# soup_liquor = BeautifulSoup(liquor.text,'lxml')
# soup_beer = BeautifulSoup(beer.text,'lxml')


#
# def text_detail ():
#     li = soup_wine.find_all("li",{'class':'CatalogResults__CatalogListItem___2qCwP'})
#     print(len(li))
#     for link in li:
#         children = link.findChildren("div",{'class':'CatalogItem__CatalogItemImage___32wLN'}, recursive=True)
#         print(children)
#     # return
# text_detail()

# style="background-image: url("https://products1.imgix.drizly.com/ci-the-pinot-project-pinot-noir-b03eba6f23633273.jpeg?auto=format%2Ccompress&dpr=2&fm=jpeg&h=240&q=20");"
# print(soup_wine.select('title'))
# location = soup_wine.find('strong', {'style': 'background-image'})


# div_style = soup_wine.find('div')['style']
# style = cssutils.parseStyle(div_style)
# url = style['background-image']

print('done')
# if location is not None:
#     location_text = location.text.strip()
# price = soup_wine.select('div > .xxxx-large')
# if price is not None:
#     price_text = price[0].text.strip('Rs').strip()
#
# images = soup_wine.select('#bigGallery > li > a')
# img = [image['href'].strip() for image in images]
# description = soup_wine.select('#textContent > p')
# if description is not None:
#     description_text = description[0].text.strip()
# # Creating a dictionary Object
# item = {}
# # item['title'] = title_text
# item['description'] = description_text
# # item['location'] = location_text
# # item['price'] = price_text
# item['images'] = img