from art import logo
from replit import clear

print(logo)

max_bid = 0
bidding_dic = {}
cont = "y"
bid = 0
max_name = 0

while cont == "y":
    name = input("Please enter your name : \n")
    bid = int(input("Your bid: \n"))
    bidding_dic["name"] = name
    bidding_dic["bid"] = bid
    if bidding_dic["bid"] > max_bid:
        max_bid = bidding_dic["bid"]
        max_name = bidding_dic["name"]
    cont = input("Do you want to continue? type 'y or Y' for yes: \n")
    if cont == "y":
        clear()

print(f"Winner is: {max_name}, his/her bid: {max_bid}")

while True:
    pass
