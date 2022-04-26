""" Write a program to show the grade obtained by a student after he/she enters their total mark percentage.
Program should accept an input from the user and display their grade as follows
Mark
Grade
> 90
A
80-89
B
70-79
C
60-69
D
50-59
E
< 50
Failed

"""

mark=int(input("enter the percentage of mark attained by the student in 100 :"))
if mark<50:
    print("sorry you have failed in the exam try again")
elif mark>50 and mark<59  :
    print("congratulations you  have cleared the exam and your  grade is E")
elif mark>60 and mark<69  :
    print("congratulations you  have cleared the exam and your  grade is D")
elif mark>70 and mark<79  :
    print("congratulations you  have cleared the exam and your  grade is C")
elif mark>80 and mark<89  :
    print("congratulations you  have cleared the exam and your  grade is B")
elif mark>89 and mark<90  :
    print("congratulations you  have cleared the exam and your  grade is A")