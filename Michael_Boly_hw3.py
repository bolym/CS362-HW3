"""
How to run:
1. Open a terminal and navigate to the file location
2. pip install pyinputplus
3. python [filename]

In this case, run python Michael_Boly_hw1.py

Enter the year as an integer and press Enter
"""

import pyinputplus as pyip

year = pyip.inputInt(prompt = "Enter a year: ", min = 0)

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
