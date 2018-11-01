#----------------------------------------- Word Guess Game
word="zeeshan"
guess=""
count=0
limit=3
out_of_guess=False
while guess!= word and not(out_of_guess):
    if count<limit:
        guess=input("Enter Guess Name")
        count+=1
    else:
        out_of_guess=True
if out_of_guess:
    print("You Loose ! Out of Guess")
else:
    print("You Win")
