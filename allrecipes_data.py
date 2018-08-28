import fetch
import json
from bs4 import BeautifulSoup

raw_html = fetch.simple_get(
    "https://www.allrecipes.com/recipes/17562/dinner/")
html = BeautifulSoup(raw_html, "html.parser")

recipes = {}
links = []

for link in html.find_all('a'):
    href = link.get('href')
    if (isinstance(href, (str,))
        and href[:34] == 'https://www.allrecipes.com/recipe/'
            and href not in links):
        links.append(href)
    if len(links) > 0:
        break

for link in links:
    page = fetch.simple_get(link)
    recipe_html = BeautifulSoup(page, "html.parser")
    recipes[recipe_html.select("h1")
            [0].text.strip()] = [recipe_html.prettify()]

with open("allrecipes.txt", "w+") as file:
    file.write(json.dumps(recipes))

# for ul in recipe_html.find_all('ul'):
#     title = recipe_html.select("h1")
#     prep = recipe_html.select('ul[class=prepTime]')
#     print(type(prep), prep)
#     # recipes[title].append(prep)

# #print(len(recipes["Chef John's Pasta Primavera"]))
