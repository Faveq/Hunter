import requests
from bs4 import BeautifulSoup
import re
import os


def format_url(hunted_item):
    words = hunted_item.split()
    url = "https://www.olx.pl/elektronika/komputery/podzespoly-i-czesci/q-"
    for x in words:
        url += x + "-"

    url = url[:-1]
    url += "/?search%5Border%5D=filter_float_price%3Aasc"
    return url


def find(hunted_item, search_black_list, price_range):
    black_list = set(search_black_list)
    url = format_url(hunted_item)
    response = requests.get(url)
    found_links = []

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        was = False
        title = soup.title
        print()

        paragraphs = soup.findAll('div', class_='css-1sw7q4x')

        for paragraph in paragraphs:
            was = False
            for word in paragraph.text:
                if word in black_list:
                    was = True
                    break
            if not was:
                price = paragraph.find(class_="css-10b0gli er34gjf0")
                if price is not None:
                    price = re.sub(r'\D', '', str(price.text))
                    if price_range[0] <= int(price) <= price_range[1]:
                        link = (paragraph.find('a'))
                        found_links.append("https://www.olx.pl/" + link.get('href'))
    return found_links

