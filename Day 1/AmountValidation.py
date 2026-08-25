while(True):
    amount = int(input("Enter the amount: "))
    if amount == 0:
        continue
    if amount < 0:
        print("Amount cannot be negative. Please enter a valid amount.")
        break
    if amount>1000:
        print(amount)