balance=10000
amount=int(input("Enter amount : "))
if(amount<balance):
    print("Amount has been debited.  ")
    balance = amount
    new_balance = 10000 - balance
    print(f"Your new balance {new_balance}")

else:
    print("credited ")
    new_balance=balance+amount
    print(f"Your new balance {new_balance}")


