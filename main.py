from assets import logo
import os


def clear_console():
    os.system('clear' if os.name == 'posix' else 'cls')

print(logo)
print("")
print("Welcome to the secret auction program")


end_of_auction = False
bids= {}
higher_bid = 0

def find_highest_bid(bidding_record):
    higher_bid = 0
    for bidder in bidding_record:
        ammount = bidding_record[bidder]
        if ammount > higher_bid:
            higher_bid = ammount
            winner = bidder
    print(f"\nThe winner is {winner} with the highest bid - ${ammount}\n")


while not end_of_auction:
    name = input("What is your name?: ")
    prize = int(input("What is your bid?: $"))
    add_another = input("Are there another bidder? type 'yes' or 'no': ")
    bids[name] = prize
    if add_another == "no":
        find_highest_bid(bids)
        end_of_auction = True
    elif add_another == "yes":
        
        print("\nczyszczę konsole....\n")
        print("\n" * 100)
# print(f"The winner is {bids(max_offer)} with the bid {bids(prize=max_offer)}")
