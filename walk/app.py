from flask import Flask, render_template

app = Flask(__name__)

from bs4 import BeautifulSoup
import requests
import re

runescape = "runescape"
herb_run = "herb+run"
herb_patch = "herb+patch"

# Our seed is what the current price of irit seeds are in OSRS
seed_request = requests.get("https://secure.runescape.com/m=itemdb_oldschool/Irit+seed/viewitem?obj=5297")
seed_soup = BeautifulSoup(seed_request.content, "html.parser")
seed = int(seed_soup.find('div', class_="stats").span.text)

@app.route('/')

def index():
    return render_template("index.html")

@app.route('/runescape')

def rs():
    request = requests.get(f"https://oldschool.runescape.wiki/?search={runescape}&title=Special:Search&limit=250&fulltext=1")
    soup = BeautifulSoup(request.content, "html.parser")
    titles = soup.find_all('a')

    title = titles[seed].text

    body_link = titles[seed].get('href')
    request2 = requests.get(f"https://oldschool.runescape.wiki{body_link}")
    soup = BeautifulSoup(request2.content, "html.parser")

    body = soup.p.text
    image = f"https://oldschool.runescape.wiki{soup.img.get('src')}"

    return render_template("runescape.html", head_text = title, body_text = body, image = image)

@app.route('/herb_run')

def run():
    request = requests.get(f"https://oldschool.runescape.wiki/?search={herb_run}&title=Special:Search&limit=250&fulltext=1")
    soup = BeautifulSoup(request.content, "html.parser")
    titles = soup.find_all('a')

    title = titles[seed].text

    body_link = titles[seed].get('href')
    request2 = requests.get(f"https://oldschool.runescape.wiki{body_link}")
    soup = BeautifulSoup(request2.content, "html.parser")

    body = soup.p.text
    image = f"https://oldschool.runescape.wiki{soup.img.get('src')}"

    return render_template("herb_run.html", head_text = title, body_text = body, image = image)

@app.route('/herb_patch')

def patch():
    request = requests.get(f"https://oldschool.runescape.wiki/?search={herb_patch}&title=Special:Search&limit=250&fulltext=1")
    soup = BeautifulSoup(request.content, "html.parser")
    titles = soup.find_all('a')

    title = titles[seed].text

    body_link = titles[seed].get('href')
    request2 = requests.get(f"https://oldschool.runescape.wiki{body_link}")
    soup = BeautifulSoup(request2.content, "html.parser")

    body = soup.p.text
    image = f"https://oldschool.runescape.wiki{soup.img.get('src')}"

    return render_template("herb_patch.html", head_text = title, body_text = body, image = image)