import requests
import os
import sys
import json


def get_url():
    

    if os.path.exists("url.txt"):
        print("Saved URL Found!")
        with open("url.txt", "r") as found_url_file:
            url = found_url_file.read()
            return url
    else:
        exit() # adding saving

def get_mode():

    answer = input("code or page scan: ")
    return answer

def scan(url, mode):
    response = requests.get(url)

    if mode == "code" or mode == "Code":
        print(f"Returned status code: {response.status_code}")
    elif mode == "page" or mode == "Page":
        print(response.text)



url = get_url()
print(url) #not debug visual feature to info user to know what they are even scanning ig?
print()

mode = get_mode()
print(f"selected mode: {mode}") # for debugging purposes. 
print("scanning...\n")
scan(url, mode)
