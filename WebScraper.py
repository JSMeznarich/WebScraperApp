#!/usr/bin/python3

# Check to see if a bird is on sale at Murray McMurray Hatchery
# and alert the user when it is


# Imports
import requests
from bs4 import BeautifulSoup
import smtplib


# Function that you can notify however you want
# Currently it lets you sent a simple email throught a gmail account
# To use on sender email turn on "Less secure app access"
def notify():
    sender = "from@from.com"
    password = "password"
    receiver = "t0@to.com"
    message = "enter message"

    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()

    server.login(sender, password)

    server.sendmail(sender, receiver, message)
    server.quit()




#make a request from the website
page = requests.get("https://www.mcmurrayhatchery.com/juvenile_mandarin_ducks.html")

# create an instance of the beautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')

# find the sold out class
soldOut = []
soldOut = soup.find_all('span', class_='prod_is_bo_soldout')

# not sold out
if not soldOut:
    print("item in stock")
    notify()
else:
    print("sold out")
