# MIT License

# Copyright (c) 2023 [konk-gg/knok]


# Free to use and distribute. Selling or commercial use requires permission.
# Email 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense
# copies of the Software

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.





#the libraries that I need to import
import requests
import fade
import time
import os
from colorama import Fore

#the menu
print(Fore.RED + """
                                        ╔══════════════════════════════════════╗
                                        ║      made by knok.gg/knok-gg :)      ║
                                        ║                                      ║
                                        ║         ┬┌─┐  ┬  ┌─┐┌─┐┬┌─┬ ┬┌─┐     ║
                                        ║         │├─┘  │  │ ││ │├┴┐│ │├─┘     ║
                                        ║         ┴┴    ┴─┘└─┘└─┘┴ ┴└─┘┴       ║
                                        ║             [1] IP LOOKUP            ║
                                        ║                                      ║
                                        ║                                      ║
                                        ║               [0] Exit               ║
                                        ║                                      ║
                                        ╚══════════════════════════════════════╝
""")
#asking the user for the choice
choie = input("""
                                                 choose a choice: """)
#if they put 0 it exits
if choie == "0":
    exit()

#if they put 1 it ask for the ip
if choie == "1":
    ip = input("                                                 what is the ip: ")
    #the api
    url = f'https://ipinfo.io/{ip}/json'
    response = requests.get(url)
    
    print(response.json())

#when its done it asks the user to put x if they want to exit
exit = input("                                                  Put x to exit: ")

#if they do it exits
if exit == "x":
    exit()