import requests
import os
import sys
import json

# im bad at naming variables and functions :(
# MADE BY SQL – 2026


# for clearing the screen. not obvious at all...
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

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
        clear_screen()
        return url

    elif save.lower() == "n":
        clear_screen()
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
    """ + "\033[0m") # i made this ascii art with figlet on linux. also copied the color thing from SO cause i dunno how to do that.

    print("""
    [1] Status Code
    [2] Headers
    [3] Cookies
    [4] Page HTML
    [99] Quit
    """)

    answer = int(input("Select: "))
    return answer

def scan(url, mode):
    if mode == 99:
        print("Bye!") # Remember this first cuz it cant run if exit
        exit()
    print("scanning...\n")
    response = requests.get(url)

    if mode == 1: # status code
        
        print(url)
        print(f"Returned status code: {response.status_code}")

    elif mode == 2: # Headers
            
            print(url)
            print(json.dumps(dict(response.headers), indent=4))
    
    elif mode == 3: # cookies
            
            print(url)
            print(response.cookies)
    
    elif mode == 4: # Page HTML --
        
        print(url)
        print(response.text)
    else:
        print("i have no idea what happened.")


url = get_url()
print(url) # debug
print()

mode = get_mode()



scan(url, mode)
