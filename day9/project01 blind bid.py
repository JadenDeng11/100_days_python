from replit import clear
import art
print(art.logo)
print('Welcome to the Blind Bid')

name = input("What is your name:\n")
bid = float(input("What is your bid:\n"))
people = input("More people to bid? yes or no\n")

all_name = []
all_bid = []

# def add_files(name01,bid01):
#     new_add = {"name" : name01,"bid" : bid01}
#     all_files.append(new_add)

end = False
while not end:
    if people == "yes":
        clear()
        name = input("What is your name:\n")
        bid = float(input("What is your bid:\n"))
        people = input("More people to bid? yes or no\n")

        all_name.append(name)
        all_bid.append(bid)
    else:
        clear()
        max_bid=max(all_bid)
        position=all_bid.index(max_bid)

        print(f"Winner is {all_name[position]}, bid is {max_bid}")
        end = True