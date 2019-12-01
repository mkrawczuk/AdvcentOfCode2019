import pickle
import requests
import os.path
import sys

from bs4 import BeautifulSoup
from getpass import getpass

CACHEDIR = os.path.join(sys.path[0] ,"cache")

class Parser:
    """ A simple parser for a newline-separated list of numbers. """
    def parse(self, inputdata: str):
        return list(map(int, inputdata.split()))

class Downloader:
    """ Download input with GitHub authentication. """
    _URL = "https://adventofcode.com/2019/day/{}/input"

    def downloadInput(self, day: int):
        with requests.Session() as session:
            url = "https://github.com/login"
            headers = {
                    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
                    }
            print("Provide your GitHub credentials: ")
            login_data = {
                    'commit': 'Sign in',
                    'utf8': '%E2%9C%93',
                    'login': input("Username: "),
                    'password': getpass()
                    }
            response = session.get(url, headers=headers)
            soup = BeautifulSoup(response.content, 'html5lib')
            login_data['authenticity_token'] = soup.find('input',
                    attrs={'name': 'authenticity_token'})['value']
            response = session.post("https://github.com/session",
                    data=login_data, headers=headers)
            response.raise_for_status()

            response = session.get("https://adventofcode.com/auth/github")
            response.raise_for_status()

            response = session.get(self._URL.format(day))
            response.raise_for_status()

            return response.text

class InputForDay:
    """Input handler for the given day's task."""

    def __init__(self, day: int,
            parser: Parser = Parser(),
            downloader: Downloader = Downloader()):
        self._day = day
        self._parser = parser
        self._downloader = downloader

    """Downloads the input from the AoC web API, parses it with the provided
       parser, pickles the resulting object, caches it, and returns it to
       the caller. If a cached object is found, un-pickles it and returns it
       to the caller."""
    def get(self):
        if not os.path.exists(CACHEDIR):
            os.mkdir(CACHEDIR)
            
        cachefn = os.path.join(CACHEDIR, str(self._day))
        if os.path.exists(cachefn):
            with open(cachefn, "rb") as f:
                return pickle.load(f)

        inputRaw = self._downloader.downloadInput(self._day)
        inputObj = self._parser.parse(inputRaw)

        with open(cachefn, "w+b") as f:
            pickle.dump(inputObj, f)

        return inputObj
