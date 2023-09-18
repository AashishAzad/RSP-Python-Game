import random


def winOrLoss(userPick, compPick):
    winner = ''
    if userPick == compPick:
        winner = "No"
    elif userPick == 'R' and compPick == 'S':
        winner = "Your"
    elif userPick == 'R' and compPick == 'P':
        winner = "Computer's"
    elif userPick == 'S' and compPick == 'P':
        winner = "Your"
    elif userPick == 'S' and compPick == 'R':
        winner = "Computer's"
    elif userPick == 'P' and compPick == 'R':
        winner = "Your"
    elif userPick == 'P' and compPick == 'S':
        winner = "Computer's"

    return winner


sample_string = 'RSP'
compPick = ''.join((random.choice(sample_string)) for x in range(1))
userPick = input("What's your pick:\n"
                 "For Rock : Press R\n"
                 "For Scissors : Press S\n"
                 "For Paper : Press P\n")
if userPick == 'R' or userPick == 'r'\
        or userPick == 'S' or userPick == 's'\
        or userPick == 'P' or userPick == 'p':
    print(f'Your value :', userPick.upper())
    print(f'Computer value :', compPick)
    print(winOrLoss(userPick.upper(), compPick) + " victory")
else:
    print("Wrong input!!!")
