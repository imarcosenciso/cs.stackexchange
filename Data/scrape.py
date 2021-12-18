"""Wikipedia scraper using their API

This scraper role is to recieve a tag and return its
description, using Wikipedia's API: MediaWiki API.
"""
import requests


test_tags = ["Algorithm",
             "Big O notation",
             "Turing Complete",
             "cpu-pipelines",
             "computer-architecture",
             "database-theory",
             "average-case",
             "time-complexity"
             ]

URL = "https://en.wikipedia.org/w/api.php"  # Engish Wikipedia API endpoint

"""A lot of tunning has gone into it and they return good results for the most part. Better not touch."""
PARAMS = {
    "action": "query",
    "generator": "prefixsearch",
    "gpssearch": None,
    "format": "json",
    "prop": "extracts",
    "exintro": 1,
    "explaintext": 1,
    "redirects": 1,
    "exchars": 300,
    "cmtitle": "Category:Computer science"
}


def get_description(tag: str) -> str:
    PARAMS["gpssearch"] = tag
    data = s.get(url=URL, params=PARAMS).json()

    # Extract unknown key (each query returns a random number as key).
    key = list(data["query"]["pages"].keys())[0]

    return data["query"]["pages"][key]["extract"]


if __name__ == "__main__":
    s = requests.Session()

    for t in test_tags:
        desc = get_description(t)
        print(
            f"Tag: {t}.\nDescription: {desc}\n == == == == == == == == == == == == == == ==\n")
