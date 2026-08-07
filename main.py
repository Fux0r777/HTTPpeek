import requests
import os
import sys
import json

# im bad at naming variables and functions :(

def create_url():
    
    url = input("URL with scheme: ")
    save = input("Save as file Y/N: ")

    if save.lower() == "y":
        with open("url.txt", "w") as created_url_file:
            created_url_file.write(url)

        return url

    elif save.lower() == "n":
        return url
    
    else:
        exit()
    



def get_url():
    if os.path.exists("url.txt"):
        print("Saved URL Found!")
        with open("url.txt", "r") as found_url_file:
            url = found_url_file.read()
            return url
    else:
        return create_url()

def get_mode():

    answer = input("code or page scan: ")
    return answer

def scan(url, mode):
    response = requests.get(url)

    if mode.lower() == "code":
        print(f"Returned status code: {response.status_code}")

    elif mode.lower() == "page":
        print(response.text)



url = get_url()
print(url) #not debug visual feature to info user to know what they are even scanning ig?
print()

mode = get_mode()
print(f"selected mode: {mode}") # for debugging purposes. 
print("scanning...\n")
scan(url, mode)
