"""
How to run: 
1. Open a terminal and navigate to the file location
2. python [filename]

In this case, run python Michael_Boly_hw1.py

Enter the year as an integer and press Enter
"""

val = input("Enter a year: ")

year = int(val)

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print ("Leap Year!")
        else:
            print ("Not a leap year")
    else:
        print ("Leap Year!")
else: 
    print ("Not a leap year")
