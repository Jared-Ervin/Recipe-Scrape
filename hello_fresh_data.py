import fetch
import json
from bs4 import BeautifulSoup

raw_html = fetch.simple_get(
    "https://www.hellofresh.com/recipe-archive/search/_____1?order=-rating")
html = BeautifulSoup(raw_html, "html.parser")

links = []
recipes = {}

for link in html.find_all('a'):
    hrefs = link.get('href')
    if hrefs[:8] == '/recipes' and hrefs not in links:
        links.append(hrefs)

for link in links:
    page = fetch.simple_get(
        "https://www.hellofresh.com" + link)
    recipe_html = BeautifulSoup(page, "html.parser")
    recipes[recipe_html.select("h1")
            [0].text.strip()] = recipe_html.prettify()

with open("hellofresh.txt", "w+") as file:
    file.write(json.dumps(recipes))
