#!/usr/bin/python3

# Check to see if a bird is on sale at Murray McMurray Hatchery
# and alert the user when it is


# Imports
import requests
from bs4 import BeautifulSoup

#make a request from the website
page = requests.get("https://www.mcmurrayhatchery.com/juvenile_mandarin_ducks.html")

# create an instance of the beautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')

# find the sold out class
soldOut = []
soldOut = soup.find_all('span', class_='prod_is_bo_soldout')

print(soldOut)

# not sold out
if not soldOut:
    print("item in stock")
# sold out
else:
    print("sold out")

#print(soup.prettify())