""" 
[Start Date: 2025|02|04] [Total Time (hr): 01 Hours 23 Minutes] [Finish Date: 2025|02|04] 
[Author: FirstOfLast]
"""

userAmount = float(input("Enter a decimal amount you want to convert to change: $"))

roundedUserAmount = round(userAmount * 100)

changeNeeded = {
    200:0,
    100:0,
    25:0,
    5:0,
    1:0
    }

if roundedUserAmount > 0: #To check if it a valid amount

    for coin in [200, 100, 25, 5, 1]: #Loop to check how many coin we need
        changeNeeded[coin] = roundedUserAmount // coin
        roundedUserAmount = roundedUserAmount % coin

    else:
        print(f"Need {changeNeeded[200]} * $2, {changeNeeded[100]} * $1, {changeNeeded[25]} * ¢25,  {changeNeeded[5]} * ¢5 and {changeNeeded[1]} * ¢1") #Output of how many of each coins we need to give the change
        """
        To validate that this program has no logical error, hightlight the below code and uncomment it using \"Ctrl + K + U\" to validate after which hightlight the below code agian and comment it using \"Ctrl + K + C\"
        """
        # validateCalc = ((changeNeeded[200] * 200) + (changeNeeded[100] * 100) + (changeNeeded[25] * 25) + (changeNeeded[5] * 5) + (changeNeeded[1] * 1)) / 100
        # if userAmount  == validateCalc:
        #     print("Calculation has no logical error")
        # else:
        #     print("Calculation has logical error")
        
else:
    print("Change not needed")
    