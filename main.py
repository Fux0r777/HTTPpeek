import requests
import os
import sys
import json

# im bad at naming variables and functions :(
# MADE BY SQL 2026



def create_url():
    print("\033[36m" + r"""
     _   _ _____ _____ ____                  _
    | | | |_   _|_   _|  _ \ _ __   ___  ___| | __
    | |_| | | |   | | | |_) | '_ \ / _ \/ _ \ |/ /
    |  _  | | |   | | |  __/| |_) |  __/  __/   <
    |_| |_| |_|   |_| |_|   | .__/ \___|\___|_|\_\
                            |_|
    """ + "\033[0m") # copied this color shi STRAIGHT from stack overflow
    
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
    print("\033[31m" + r"""
     _   _ _____ _____ ____                  _
    | | | |_   _|_   _|  _ \ _ __   ___  ___| | __
    | |_| | | |   | | | |_) | '_ \ / _ \/ _ \ |/ /
    |  _  | | |   | | |  __/| |_) |  __/  __/   <
    |_| |_| |_|   |_| |_|   | .__/ \___|\___|_|\_\
                            |_|
    """ + "\033[0m") # i made this ascii art with figlet. also copied the color thing from SO cause i dunno how to do that.

    print("""
    [1] Status Code
    [2] Headers
    [3] Cookies
    [4] Page HTML
    [99] Quit
    """)

    answer = input("Select: ")
    return answer

def scan(url, mode):
    response = requests.get(url)

    if mode.lower() == "1": # status code
        print(f"Returned status code: {response.status_code}")

    elif mode.lower() == "2": # Headers
            print(json.dumps(dict(response.headers), indent=4))
    
    elif mode.lower() == "3": # cookies
            print(response.cookies)
    
    elif mode.lower() == "4": # Page HTML --
        print(response.text)

    elif mode.lower() == "99": # QUIT 
        print("Bye.")
        exit()
    else:
        print("i have no idea what happened.")


url = get_url()
print(url) #not debug visual feature to info user to know what they are even scanning ig?
print()

mode = get_mode()
# print(f"selected mode: {mode}") # for debugging purposes.  okay now this just looks ugly ngl because its just a number.
print("scanning...\n")
print(url)
scan(url, mode)
