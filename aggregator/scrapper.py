from bs4 import BeautifulSoup
from .models import Article
import requests

url = "https://theintercept.com/"


def scrapper():
    intercept_scrapper()
    vox_scrapper()


def intercept_scrapper():
    result = requests.get("https://theintercept.com/");
    if result.status_code == 200:
        doc = BeautifulSoup(result.text, "html.parser")
        articles = doc.find_all("article")
        artCount = 0
        for article in articles:
            title = article.find('h3').text.strip()

            authorObject = article.find('div', class_="content-card__author")
            # theres a section for podcasts in the intercept website
            # that does not have an author tag either skip them
            # or put none for the author instead
            if authorObject is None:
                continue
            else:
                author = authorObject.text.strip()
                artCount += 1
                Art = Article(title=title, author=author, source='Intercept')
                Art.save()


def vox_scrapper():
    result = requests.get("https://www.vox.com/")
    doc = BeautifulSoup(result.text, "html.parser")
    Titles = doc.find_all("h2")
    artCount = 0
    # Authors = doc.find_all("span", class_="c-byline__author-name")
    for title in Titles:
        parent = title.parent
        authorObject = parent.find("span", class_="c-byline__author-name")
        if authorObject is None:
            continue
        else:
            author = authorObject.text.strip()
            artCount += 1
            Art = Article(title=title.text.strip(), author=author, source="Vox")
            Art.save()
