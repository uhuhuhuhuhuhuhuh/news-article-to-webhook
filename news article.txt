import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def news():
    # Set the URLs for each section you want to scrape
    urls = ['https://www.nytimes.com/section/world', 'https://www.nytimes.com/section/politics', 'https://www.nytimes.com/section/business','https://www.nytimes.com/section/sports', 'https://www.nytimes.com/section/health', 'https://www.nytimes.com/section/food','https://www.nytimes.com/section/style', 'https://www.nytimes.com/section/arts', 'https://www.nytimes.com/section/travel','https://www.nytimes.com/section/opinion',]

    # Create an empty list to store the articles
    news_articles = []

    # Loop through each URL and scrape the articles
    for url in urls:
        # Make a request to the website
        response = requests.get(url)

        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all the articles on the page
        articles = soup.find_all('article')

        # Iterate through each article and extract the title, summary, and image
        for article in articles:
            title = article.find('h2').text
            summary = article.find('p').text
            image_src = article.find('img')['src']
            news_articles.append((title, summary, image_src))

    # Render the template and pass in the list of articles
    return render_template('news.html', articles=news_articles)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
