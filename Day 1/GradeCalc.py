marks=int(input("Enter the marks: "))
if (marks < 0) or (marks>100): 
    print(f"Invalid Input")

elif marks>=0 and marks<40:
    print("Grade: Fail")

elif marks>=40 and marks<50:
    print("Grade: C")

elif marks>=50 and marks<60:
    print("Grade: B")

elif marks>=60 and marks<75:
    print("Grade: A")   

elif marks>=75 and marks<95:
    print("Grade: A+") 

elif marks>=95:
    print("Grade: Outstanding") 