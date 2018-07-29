# -------------------------------------------------#
# Title: github-latest.py
# Dev: Scott Luse
# Date: 07/28/2018
# -------------------------------------------------#

import sys
import json

import requests

def github(user):
    print("Retrieving event list for: " + user)

    '''
    https://api.github.com/users/{user}/repos{?type,page,per_page,sort}",
    
    1. Retrieve a list of "events" associated with the given user name
    2. Print out the time stamp associated with the first event in that list.
    
    '''
    response = requests.get("https://api.github.com/users/{}/events".format(user))
    mod_date = response.json()[0]['created_at']
    print(mod_date)


if __name__ == "__main__":
    username = sys.argv[1]
    github(username)



