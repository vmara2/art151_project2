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

@app.route('/herb_patch')

def herb_patch():
    request = requests.get(f"https://oldschool.runescape.wiki/?search={herb_patch}&title=Special:Search&limit=250&fulltext=1")
    soup = BeautifulSoup(request.content, "html.parser")

    divs = soup.find_all('div')
    titles = soup.find_all('a')

    title = titles[seed].text
    body = divs[seed].text

    return render_template("herb_patch.html", head_text = title, body_text = body)