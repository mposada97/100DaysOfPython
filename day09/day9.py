#blind auction excercise
bids = {}

while True:
    bidder = input("Whats your name? ")
    bid = float(input("What is your bid? $"))
    bids[bidder]=bid
    more_bidders_q = input("Are there any other bidders? 'yes' or 'no' \n").lower()
    if more_bidders_q == 'yes':
        print('\n' * 1000)
    else:
        print('\n' * 1000)
        break
current_max = 0
winner = ''
for key in bids:
    if bids[key] > current_max:
        current_max = bids[key]
        winner = key
print(f'{winner} won by bidding ${current_max}')
