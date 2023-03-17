class User:
    def __init__(self, first_name, last_name, gender, street_address, city,
                 email, cc_number, cc_type, balance, account_no):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.street_address = street_address
        self.city = city
        self.email = email
        self.cc_number = cc_number
        self.cc_type = cc_type
        self.balance = balance
        self.account_no = account_no
        userList.append(self)

    def displayInfo(self):
        print("########################")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Gender: {self.gender}")
        print(f"Street Address: {self.street_address}")
        print(f"City: {self.city}")
        print(f"Email: {self.email}")
        print(f"CC Num: {self.cc_number}")
        print(f"CC Type: {self.cc_type}")
        print(f"Balance: {self.balance}")
        print(f"Account No: {self.account_no}")


def generateUsers():
    import csv
    with open('bankUsers.csv', newline='') as csvfile:
        filereader = csv.reader(csvfile, delimiter=',', quotechar="'")
        for line in filereader:
            User(line[0], line[1], line[2], line[3], line[4], line[5],
                 line[6], line[7], float(line[8]), line[9])


def findUser():
    separate_full_name = []
    while len(separate_full_name) != 2:
        user_to_find = input("Enter the full name of the user: ").title()
        separate_full_name = user_to_find.split()
        if len(separate_full_name) == 0:
            print("You've left the name blank!")
        elif len(separate_full_name) == 1:
            print("You've only entered the first name! Pls enter the full "
                  "name!")
    first_name = separate_full_name[0]
    last_name = separate_full_name[1]

    for user in userList:
        if first_name == user.first_name and last_name == user.last_name:
            user.displayInfo()
            return user

    print("Sorry, no user was found with that name")
    return None


def overdrafts():
    count_overdraft = 0
    total_overdraft = 0
    print("OVERDRAFT NAMES:")
    for user in userList:
        if user.balance < 0:
            print(f"{user.first_name} {user.last_name}'s overdraft amount: "
                  f"{user.balance}")
            count_overdraft += 1
            total_overdraft += user.balance
    print()
    print(f"Total number of overdraft users: {count_overdraft}")
    print(f"Total amount overdraft: {total_overdraft:.2f}")


def missingEmails():
    no_email_count = 0
    print("NAMES WITH MISSING EMAIL:")
    for user in userList:
        if not user.email:
            print(f"{user.first_name} {user.last_name}")
            no_email_count += 1
    print(f"Total number of users with missing emails: {no_email_count}")


def bankDetails():
    user_count = 0
    bank_worth = 0
    highest_balance = 0
    highest_balance_first_name = ""
    highest_balance_last_name = ""
    lowest_balance = 0
    lowest_balance_first_name = ""
    lowest_balance_last_name = ""
    for user in userList:
        user_count += 1
        bank_worth += user.balance
        if user.balance > highest_balance:
            highest_balance = user.balance
            highest_balance_first_name = user.first_name
            highest_balance_last_name = user.last_name

        elif user.balance < lowest_balance:
            lowest_balance = user.balance
            lowest_balance_first_name = user.first_name
            lowest_balance_last_name = user.last_name

    print(f"Total number of users: {user_count}")
    print(f"Bank total worth: ${bank_worth:.2f}")
    print(f"User with highest balance: {highest_balance_first_name} "
          f"{highest_balance_last_name} with"
          f" ${highest_balance}")
    print(f"User with lowest balance: {lowest_balance_first_name} "
          f"{lowest_balance_last_name} with"
          f" {lowest_balance}")


def transfer():
    deduct_acct_balance = []
    acct_num_to_find = input("Account Number: ")
    for user in userList:
        if acct_num_to_find == user.account_no:
            print(f"Name: {user.first_name} {user.last_name} \n"
                  f"User balance: ${user.balance}")
            deduct_acct_balance.append(user.account_no)

    if not deduct_acct_balance:
        print("You haven't entered an appropriate account number from "
              "1-2014. \nPlease restart the transfer money function again "
              "from the main menu!")
        return None

    transfer_amount = float_checker("Transfer amount: $")
    acct_num_transfer = input(f"Enter Account Number to transfer "
                              f"${transfer_amount:,.2f} to: ")

    for user in userList:
        if acct_num_transfer == user.account_no:
            acct_transfer_name = user.first_name, user.last_name

            first_name = acct_transfer_name[0]
            last_name = acct_transfer_name[1]
            confirm = input(f"Confirm that you want to transfer"
                            f" ${transfer_amount:,.2f} to "
                            f"{first_name} {last_name} (Y or N): ").title()
            if confirm == "Y":
                user.balance += transfer_amount
                print(f"{first_name} {last_name}'s balance: ${user.balance} ("
                      f"increased by ${transfer_amount:,.2f})")
                deduct_user = deduct_acct_balance[0]

                for user in userList:
                    if deduct_user == user.account_no:
                        user.balance -= transfer_amount
                        print(f"{user.first_name} {user.last_name}'s balance: "
                              f"${user.balance} (decreased by $"
                              f"{transfer_amount:,.2f})")
            else:
                print("You've stopped the transaction! Return to the main "
                      "menu!")
                return None


def float_checker(question):
    error = "\nSorry, you must enter a float amount\n"
    number = ""
    while not number:
        try:
            number = float(input(question))
            return number
        except ValueError:
            print(error)


userList = []
generateUsers()

userChoice = ""
print("Welcome")

while userChoice != "Q":
    print("What function would you like to run?")
    print("Type 1 to find a user")
    print("Type 2 to print overdraft information")
    print("Type 3 to print users with missing emails")
    print("Type 4 to print bank details")
    print("Type 5 to transfer money")
    print("Type Q to quit")
    userChoice = input("Enter choice: ")
    print()

    if userChoice == "1":
        findUser()
    elif userChoice == "2":
        overdrafts()
    elif userChoice == "3":
        missingEmails()
    elif userChoice == "4":
        bankDetails()
    elif userChoice == "5":
        transfer()
    print()
