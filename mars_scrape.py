from splinter import Browser
from bs4 import BeautifulSoup
#import requests

def init_browser():
   # @NOTE: Replace the path with your actual path to the chromedriver
   executable_path = {"executable_path": "chromedriver.exe"}
   return Browser("chrome", **executable_path, headless=False)


def scrape():
   browser = init_browser()

# Dependencies
from bs4 import BeautifulSoup
import requests
import pymongo
from splinter import Browser
import pandas as pd
import time

# windowsuser
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)

# URL of page to be scraped
url = 'https://mars.nasa.gov/news/'
browser.visit(url)

# HTML Object
html = browser.html

# Create BeautifulSoup object; parse with 'html'
soup = BeautifulSoup(html, 'html.parser')

#find title or paragraphs    
news_title = soup.find('div', class_='content_title').text

news_p = soup.find('div', class_='article_teaser_body').text

    

    # print information

print(news_title)
print('-----------------')
print(news_p)

#Space Images with spilter
image_url= 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(image_url)

# HTML Object
html = browser.html

# Create BeautifulSoup object; parse with 'html'
soup = BeautifulSoup(html, 'html.parser')

#JPL_home_url = "https://www.jpl.nasa.gov"
#JPL_img_url = JPL_home_url+"/spaceimages/?search=&category=Mars"
items = soup.find("div",{"class":"carousel_items"})

featured_img = items.find("article")
featured_img_url = image_url+featured_img['style'].split(':')[1].split('\'')[1]
print(featured_img_url)

weather_twitter='https://twitter.com/marswxreport?lang=en'
browser.visit(weather_twitter)

# HTML Object
html = browser.html

# Create BeautifulSoup object; parse with 'html'
soup = BeautifulSoup(html, 'html.parser')

#find tweets
mars_weather = soup.find('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text').text
mars_weather

facts_url='https://space-facts.com/mars/'
browser.visit(facts_url)

#build dataframe
mars_data= pd.read_html(facts_url)
mars_data = pd.DataFrame(mars_data[0])
mars_data.columns =["Decription", "Values"]
mars_data = mars_data.set_index("Decription")
mars_data_html = mars_data.to_html('mars_data.html')
#mars_data_html

import requests
hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
#browser.visit(hemispheres_url)
response = requests.get(hemispheres_url)

#html object
#html = browser.html

# Create BeautifulSoup object; parse with 'html'
soup = BeautifulSoup(response.text, "html.parser")

print(soup.prettify())

#results 
results = soup.find_all('div', class_='item')
results

# Loop through returned results
mars_hemispheres =[]
for result in results:
        # Identify and return title of listing
        title = result.find('a', class_="itemLink product-item").text

        
        
        
        # Identify and image
        image_url = results.find_all("src")
#dictionary

        mars_dictionary={"Title":title, "img_url": hemispheres_url+image_url}
        mars_hemispheres.append(mars_dictionary)

print(mars_hemispheres)

mars_scrape_data = {
       'news_title': news_title, #title
       'news_p': news_p, #paragraph
       'featured_image_url': featured_image_url, #pic
       'mars_weather': mars_weather #twitter
   }

   return mars_scrape_data