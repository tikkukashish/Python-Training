salary=int(input("Enter the salary: "))
credit_score=int(input("Enter the credit score: "))
existing_loans=int(input("Enter the number of existing loans: "))
employment_type=input("Enter employment type")

if salary>80000 and credit_score>=750 and existing_loans<=20000:
    print("Loan Approved")

elif salary>50000 and credit_score>650:
    print("Proceed with caution")

elif credit_score<600:
    print("Loan Denied")

else:
    print("Enter manual approval")