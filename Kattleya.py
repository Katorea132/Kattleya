#!/usr/bin/python3
"""This module contains the formed message and the twitting logic
"""
from DateScrap import dateFinder
from datetime import datetime, date
import tweepy
import json

data = {"CONSUMER_KEY": None,
        "CONSUMER_SECRET": None,
        "ACCESS_KEY": None,
        "ACCESS_SECRET": None}


def main():
    """This is where the message for the tweet is forged
as well as the tweet itself
    """
    try:
        with open("json.config", "r") as file:
            data.update(json.load(file))
    except Exception:
        print("Something is wrong with the 'json.config' file")
        exit(1)
    auth = tweepy.OAuthHandler(data["CONSUMER_KEY"], data["CONSUMER_SECRET"])
    auth.set_access_token(data["ACCESS_KEY"], data["ACCESS_SECRET"])
    api = tweepy.API(auth)

    day, month, message = dateFinder()
    current = datetime.today()
    release = "2020-{}-{}".format(month, day)
    release = datetime.strptime(release, "%Y-%B-%d")
    delta = release - current
    delta = str(delta).split(",")
    delta = delta[0]

    tweet = "There are still {} before #Cyberpunk2077 is \
released!\n'{}' - @Steam".format(delta, message)
    api.update_status(tweet)
    print("Success!")

if __name__ == "__main__":
    main()
