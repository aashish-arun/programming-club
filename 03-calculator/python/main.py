""" 
[Start Date: 2025|03|6] [Total Time (hr): 0 hr 48 mins] [Finish Date: 2025|03|6] 
[Author: FirstOfLast]
"""

while True:
    try:
        num = int(input("Enter the 1st number: "))
        break
    except ValueError:
        print("Invalid input! Please enter a valid number.")

while True:
    try:
        anotherNum = int(input("Enter the 2nd number: "))
        break
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        
operation = input("Choose a operation (+, -, * or /): ")

while operation not in ['+', '-', '*', '/']:
    operation = input("Invalid operator! Please choose from +, -, *, or /.")
    
if operation == "+":
    res = num + anotherNum

elif operation == "-":
    res = num - anotherNum

elif operation == "*":
    res = num * anotherNum
    
elif operation == "/":
    try:
        res = num / anotherNum
    except ZeroDivisionError:
        res = "Error"

if res != "Error":
    print(f"The result is: {res}")
else:
    print("Error: Cannot divide by zero. Sorry!")