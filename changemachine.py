#this will take a given input to put into the changeMachine
generousDonation = input("How much change are you getting back today?")
giveBackAmount = float(generousDonation)

def changeMachine(giveBackAmount):
    #possible change types
    changeType = [100, 50, 20, 10, 5, 2, 1, 0.25, 0.10, 0.05, 0.01]
    changeAmount = 0
    changeForType = 0
    """
    for each different pass of change,
    while the amount of money is greater than the changetype
    remainderAmount is used to find the necessary coins needed for that changetype
    giveBackAmount must be subtracted by the change and the number of coins that fit in
    until it can move onto the next part of the list that works
    """
    for change in changeType:
        while giveBackAmount >= change:
            remainderAmount = giveBackAmount / change
            giveBackAmount = round(giveBackAmount, 2) - (change * int(remainderAmount))
            changeAmount += int(remainderAmount)
            """
            by doing this, we can see the coins per changeType
            that must be returned to customer
            """
            changeForType = int(remainderAmount)
            print (change, changeForType)
    return (changeAmount)

print(changeMachine(giveBackAmount))