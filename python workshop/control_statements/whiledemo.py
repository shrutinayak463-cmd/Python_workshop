balance=10000
while True:
 type=input("Enter the type credit/debit : ")
 if (type == "stop"):
     break
 elif(type=="credit"):
    credit_amount=int(input("Enter the credit amount : "))
    balance = balance + credit_amount
    print(f"Current balance {balance}")

 elif(type=="debit"):
    debit_amount=int(input("Enter the debit amount : "))
    if(balance>debit_amount):
        balance = balance - debit_amount
        print(f"Amount debited and Current balance {balance}")

    else:
        print("Insufficient balance")
