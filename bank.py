

def get_customer_info():
    customer_name =input("Enter the name:")
    customer_address =input("Enter the address:")
    email_id =input("Enter the email id:")
    username=input("Enter the username:")
    password =input("Enter the password:")

    return(customer_name,customer_address,email_id,username,password)

customers=get_customer_info()

#TESTING CHANGE =================


def create_user():
    with open("customers.txt","a")as customers_file,open("user.txt","a")as user_file:
        file.write (f"{customers[0]},{customers[1]},/n")

create_user()


# def create_account():
#     coustomer_name = input("Enter the name:")
#     coustomer_address = input("Enter the address:")
#     email_id = input("Enter the email:")
#     account_number = input("Enter the account number:")
#     initial_balance=input("Enter the initial balance:")
#     if account_number in account:
#         print("account already exsit")
#     return
#     name(input("Enter the account holder name"))
#     else:
#     balance=float("Enter initial balance must be greater than 0")
#     if balance<0:
#         print("initial balance")
#     else:   
#         print("invalid number")

# create_account()



def deposit(balance,amount):
    if amount <= 0:
        print("deposit amount. Must be positive number.")
        balance
    balance += newbalance
    print(f"deposit successfully!,{amount}.new balance:{balance}")
    return balance

    deposit(balance,amount)


def withdraw(balance,amount):
    if amount <= 0:
        print("invalid amount. Must be greater than 0.")
    elif balance>amount:
        print("insufficient funds.")
    else:
        print(f"withdraw successfully!,{amount}.currentbalance:{balance}")
    return balance

# withdraw(balance,amount)


# def check_balance():
#     input("Enter the acount number:")
#     if account_number in account:
#         print("your current balance is:")

# check_balance()

# def transaction_history(deposit,withdraw)
# input("Enter the account number:")
# if account_number in account:
#     print("transaction_history,")


# transaction_history(deposit,withdraw)






# def main_menu():
#     while True:
#         print("Menu-Driven")
#         print("1.Account Creation")
#         print("2.Deposit Money")
#         print("3.withdraw Money")
#         print("4.Check Balance")
#         print("5.Transaction")
#         print("6.Exit")




#     choice = input("Enter your choice (1-6):")
        
#     if choice == "1":
#         print ("create_account")
#     elif choice =="2":
#         amount = float(input("Enter amount to deposit:"))
#         if amount:=Balance:
#             Balance +=depositamount
#             print("Deposit successfully!. Thank You.")
#         else:
#             print("Deposid Failed")
#     elif choice =="3":
#         amount = float(input("Enter amount to withdraw:"))
#          if amount:=balance:
#             balance -= amount
#             print(f"withdraw successful. New balance:{Balance}")
#         else:
#          print("withdraw failed!.Try again;")
#     elif choice =="4":
#         print("Check Balance")
#         balance+=newbalance
#     elif choice =="5":
#         print("Your Transaction is:(Withdraw,deposit money)")
#     break
#     else:
#         print("exit")

# main_menu()