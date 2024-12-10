register_bid = "yes"
bid_detail = {}

while register_bid == "yes":
    register_bid = input("Do you want to register for the auction? yes or no ")
    if register_bid != "yes":
        break
    name = input("Please enter your name. ")
    bid = int(input("Please enter your bid in $. "))
    bid_detail[name] = bid
    print("\n" * 100)

max_bid = 0
max_bid_user = ""

for key in bid_detail:
    if bid_detail[key] > max_bid:
        max_bid = bid_detail[key]
        max_bid_user = key

print(f"Max bid of $ {max_bid} made by {max_bid_user}")
