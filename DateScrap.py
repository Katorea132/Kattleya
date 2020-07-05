#!/usr/bin/python3
"""This module contains the web scrapper for the information
about cyberpunk on steam
"""
from bs4 import BeautifulSoup as soup
import requests


def dateFinder():
    """This function retrieves the date of release posted on the Steam webpage

    Returns:
        list: Month, day and stimated time 'till release
    """
    url = 'https://store.steampowered.com/app/1091500/Cyberpunk_2077/'

    with requests.Session() as s:
        r = s.get(url)
        sopa = soup(r.text, "html.parser")
        message = str(sopa.select("p:nth-child(2)")[0])
        date = str(sopa.h1)
    message = message.replace("/", "")
    message = message.replace("<p>", "")
    date = date.replace("</h1>", "")
    date = date.split()
    return date[1], date[2], message
