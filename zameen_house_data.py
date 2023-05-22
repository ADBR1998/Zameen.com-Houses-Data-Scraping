import pandas as pd
import requests
from bs4 import BeautifulSoup
# first_page_url = "https://www.zameen.com/Houses_Property/Islamabad-3-1.html"
# first_page_r = requests.get(first_page_url)
# first_page_soup = BeautifulSoup(first_page_r.text, 'lxml')

# print(first_page_url)

title = []
bed = []
bath = []
location = []
price = []
land_area = []
date = []
base_url = 'https://www.zameen.com/Houses_Property/Islamabad-3-{}.html'

for page in range(1,41):
    url = base_url.format(page)
    r = requests.get(url)


    soup = BeautifulSoup(r.text, 'lxml')
    # box = soup.find('ul',class_='_5fe78509')

    # titles = soup.find_all('h2', class_='c0df3811')

    # for title in titles:
    #     title_text = title.text.strip()
    #     print(title_text)
        

    prices = soup.find_all('span', class_='f343d9ce')
    for i in prices:
        name = i.text
        price.append(name)

 
    date_span = soup.find_all('span', {'aria-label':"Listing creation date"})
    if date_span:
        for span in date_span:
            date_text = span.text
            # Extract the time from the date string
            time = date_text.split(': ')[1]
            date.append(time)

    # title_elements = box.find_all('div', {'title':True})
    # for title_element in title_elements:
    #     titles = title_element['title']
    #     name = titles.replace(',', '')  # Remove commas from the text
    #     title.append(name)
    #     title = list(set(title))  # Remove duplicates and convert back to a list
    #     # Filter out elements containing 'Page' or 'Next'
    #     title = [t for t in title if 'Page' not in t and 'Next' not in t]

    box = soup.find('ul', class_='_357a9937')

    title_elements = soup.find_all('h2', {'aria-label': 'Title'})
    for i in title_elements:
        name = i.text
        title.append(name)


    # Filter out elements containing 'Page' or 'Next'
    # title = [t for t in title if 'Page' not in t and 'Next' not in t]

    area = soup.find_all('span', {'class':'_984949e5'})
    for i in area:
        name = i.text
        keywords = ['kanal', 'marla']
        if any(keyword in name.lower() for keyword in keywords):
            land_area.append(name)


    locations = soup.find_all('div', {'aria-label': 'Location'})
    for i in locations:
        name = i.text
        location.append(name)

    # beds = soup.find_all('span', {'aria-label': 'Beds'})
    # bed = []

    # for i in range(1, 251):
    #     found = False
    #     for span in beds:
    #         name = span.text
    #         if name == str(i):
    #             bed.append(name)
    #             found = True
                

    articles = soup.find_all('div', {'class':'_27f6c93d'})
    # print(len(articles))
    baths = [article.find_all('span')[2].text for article in articles]
    baths = [number if number.replace(' ','').isdigit() else '' for number in  baths]
    # print(baths)
    beds = [article.find_all('span')[1].text for article in articles]
    beds = [number if number.replace(' ','').isdigit() else '' for number in  beds]
    # print(beds)
    for i in beds:
        bed.append(i)
    for i in baths:
        bath.append(i)

    # baths = soup.find_all('span', {'class': '_984949e5', 'aria-label':'Baths'})
    # for i in baths:
    #     name = i.text
    
    #     if not any(keyword in name.lower() for keyword in keywords):
    #             bath.append(name)

    # beds = soup.find_all('span', {'class': '_984949e5', 'aria-label':'Beds'})
    # for i in beds:
    #     name = i.text

    #     if not any(keyword in name.lower() for keyword in keywords):
    #         bed.append(name)


    # beds = soup.find_all('span', {'aria-label':'Beds'})
    # for i, item in enumerate(beds):
    #     for in range(len(price)):
    #         break
    #     name = item.text
    #     bed.append(name)



# print(date)
# print(len(date))
# print(location)
# print(bed)
# print(bath)
# # print(price)
# # print(land_area)
# # print(len(land_area))
# # print(len(price))
# # print(len(location))
# print(len(bed))
# print(len(bath))
# print(len(title))
# print(title)

df = pd.DataFrame({'Title':title, 'Location':location,'Land Area':land_area,'No of Beds':bed, 'No. of Baths':bath, 'Price':price })
# # # print(df)
# Set display options to show full cell content
pd.set_option('display.max_colwidth', None)

# Save DataFrame to a new CSV file
df.to_csv('C:/Users/Latitude/Downloads/zameen_houses_data.csv', index=False, header=True)


# title = []
# bed=[]
# bath=[]
# location=[]
# price =[]

# prices = soup.find_all('span', class_='f343d9ce')
# # print(prices) 
# for i in prices:
#     name=i.text
#     price.append(name)
#     print(price)


# title_elements = soup.find_all('div',{'title': True})
# for title_element in title_elements:
#     titles = title_element['title']
# #     print(titles)
# for i in titles:
#     name=i.text
#     title.append(name)
# print(title)

# locations = soup.find_all('div',{'aria-label':'Location'})
# # print(locations)
# for i in locations:
#     name=i.text
#     location.append(name)
# print(location)

# beds = soup.find_all('span', {'aria-label':'Beds'})
# # print(beds)
# for i in beds:
#     name=i.text
#     bed.append(name)
# print(bed)

# baths = soup.find_all('span',{'aria-label':'Baths'})
# # print(baths)
# for i in baths:
#     name=i.text
#     bath.append(name)
# print(bath)

    # np = soup.find('a', title='Next').get('href')
    # cnp = "https://www.zameen.com/" + np
    
    # print(cnp)
