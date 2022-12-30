import random, string, requests, urllib.request, urllib, urllib.parse, colorama, os, threading, green
from colorama import Fore as C
from colorama import Style as S
from threading import Thread
os.system("")

class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'
    
def gencode():
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(16))
    
f = open("Valid codes.txt", "a+")

class NitroGenerator:
    def __init__(self):
        self.codes = []
        self.check()
    
    def check(self):
        while True:
            code = gencode()
            self.codes.append(code)
            response = requests.get(
                "https://discord.com/api/v7/entitlements/gift-codes/" + code + "?with_application=false&with_subscription_plan=true")
            data = response.json()
            if response.status_code == 200:
                print(style.GREEN + "Worked | " + code)
                f.write(f"\ndiscord.gift/{code}")
            else:
                print(style.RED + "invalid | " + code)



NitroGenerator()
