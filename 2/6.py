"""Using the ‘switch case’ write a program to accept an input number from the user and output the day as follows.

Input
Output
1
Sunday
2
Monday
3
Tuesday
4
Wednesday
5
Thursday
6
Friday
7
Saturday
Any other input
Invalid Entry

"""

number=int(input("enter a number corresponding to the days in a week:"))
if number==1:
    print("sunday")
elif number==2:
    print("monday")
elif number==3:
    print("tuesday")
elif number==4:
    print("wednesday")
elif number==5:
    print("thursday")
elif number==6:
    print("friday")
elif number==7:
    print("saturday")
else:
    print("invalid entry")
