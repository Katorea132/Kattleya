#!/usr/bin/python3
"""This creates a tweet based on the amount of missing days
"""


def TweetMaker(d, m, da, me):
    """This will pick one from 4 different tweets
    """
    C, S, T = "#Cyberpunk2077", "@Steam", "There are still"
    CU = "current official date of release"
    days = d.split()
    days = int(days[0])
    if days % 5 == 0:
        t = "{} for {} to reach our lives! *-*".format(d, C)
    elif days % 3 == 0:
        t = "'{}' says {} - {}\n T-{}".format(me, S, C, d)
    elif days % 2 == 0:
        t = "The {} is {} {} - 2020.\n\
That means we are {} away from {}".format(CU, m, da, d, C)
    else:
        t = "{} {} before {} is released!".format(T, d, C)

    return t
