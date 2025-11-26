balance=10000
amount=int(input("Enter amount : "))
if(amount>balance):
    print("Insufficient balance!! ")

else:
    print("Amount has been debited. ")
    balance=amount
    print(f"Your balance {balance}")
    new_balance=10000-balance
    print(f"Your new balance {new_balance}")
