import requests
import os
import random
import time
import webserver
from bs4 import BeautifulSoup
# Send an HTTP request to the website that lists the proxies
def proxies():
  urltoproxies = 'https://www.proxy-list.download/api/v1/get?type=https'
  response = requests.get(urltoproxies)
# Get the list of proxies from the response
  proxies = response.text.split('\n')
# Remove any empty entries in the list
  proxies = [proxy for proxy in proxies if proxy]
# Randomly select a proxy from the list
  proxy = random.choice(proxies)
  zelist = proxy
# Set the proxy for the HTTP request
  return zelist
# Set the URLs for each section you want to scrape
urls = ['https://www.nytimes.com/section/world', 'https://www.nytimes.com/section/politics', 'https://www.nytimes.com/section/business','https://www.nytimes.com/section/sports', 'https://www.nytimes.com/section/health', 'https://www.nytimes.com/section/food','https://www.nytimes.com/section/style', 'https://www.nytimes.com/section/arts', 'https://www.nytimes.com/section/travel','https://www.nytimes.com/section/opinion',]

    # Create an empty list to store the articles
news_articles = []

    # Loop through each URL and scrape the articles
for url in urls:
        # Make a request to the website
        response = requests.get(random.choice(urls))
        print("getting the stuff")
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all the articles on the page
        articles = soup.find_all('article')

        # Iterate through each article and extract the title, summary, and image
        for article in articles:
            title = article.find('h2').text
            summary = article.find('p').text
            image_src = article.find('img')['src']
            ok = str(os.environ['Webhook'])
            daba = {
  "embeds": 
  [
    {
      "title": f"{title}",
      "url": f"{response.url}",
      "description": f"{summary}",
      "color": 15258703,
      "image": {
        "url": f"{image_src}"
      }
    }
  ]
}
            webserver.keep_alive()
            oops = requests.post(url=ok,json=daba,proxies={'http': f'{proxies()}',})
            if oops.status_code == 429:
              print("shit")
              print(oops.status_code)
              time.sleep(120)
            elif oops.status_code == 204:
              print("hit wowow")
              print(oops.status_code)
              time.sleep(60)
            else:
              print(oops.status_code)