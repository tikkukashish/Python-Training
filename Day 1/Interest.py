principle=int(input("Enter the principal amount: "))
rate=float(input("Enter the rate of interest: "))
time=int(input("Enter the time period: "))

simple_interest=(principle*rate*time)/100
print(f"Simple Interest: {simple_interest}")

compound_interest=principle*(1+rate/100)**time-principle
print(f"Compound Interest: {compound_interest}")