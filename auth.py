#register
# - first name, last name, passsword, email
# - generate user account


#login
# -  account number and password

#bank operations


#initializing the system
import random

database = {}

def init():

    isValidOptionSelected = False
    print("Welcome to bankPHP")

    while isValidOptionSelected == False:
        
        haveAccount = int(input("Do you have an account with us? 1 (yes) 2 (no) \n"))
        
        if (haveAccount) == 1:
            isValidOptionSelected = True
            login() 
        elif (haveAccount) == 2:
            isValidOptionSelected = True
            register()
        else:
            print("You have selected an invalid option")


def login():
    #print("This is the login function.")
    print(" ****** Login ****** ")

    isLoginSuccessful = False

    while isLoginSuccessful == False:

        accountNumberFromUser = int(input("Enter your account number? \n"))
        password = input("Enter your password? \n")

        for accountNumber, userDetails in database.items():
            if (accountNumber == accountNumberFromUser):
                if (userDetails[3] == password):
                    isLoginSuccessful =True
            else:
                print("Invalid account or password")
    bankOperation(userDetails)
    
def register():
    #print("This is the register function.")
    print("***** Register *****")
    email  = input("What is your email address: \n")
    first_name  = input("What is your first name: \n")
    last_name  = input("What is your last name: \n")
    password  = input("Create a password: \n")

    accountNumber = generateAccountNumber()

    database[accountNumber] = [first_name, last_name, email, password]

    print("Your account has been created")
    print(" === === === === === === ")
    print("Your account number is: %d " % accountNumber)
    print("Make sure you keep it safe")
    print(" === === === === === === ")

    login()
    
def bankOperation(user):
    print("Welcome %s %s " % (user[0], user[1]))
    isSelectedOptionValid = False

    while isSelectedOptionValid == False:
        
        selectedOption = int(input("What would you like to do? (1) deposit (2) withdrawal (3) Logout (4) Exit \n"))

        if (selectedOption == 1):
            isSelectedOptionValid == True
            depositOperations()
        elif (selectedOption == 2):
            isSelectedOptionValid == True
            withdrawalOperation()
        elif (selectedOption == 3):
            isSelectedOptionValid == True
            login()
        elif (selectedOption == 4):
            isSelectedOptionValid == True
            exit()
        else:
            print("Invalid option selected")


def withdrawalOperation():
    print("Withdrawal")
    amountToWithdraw = int(input("How much do you want to withdraw? \n"))
    print("Transaction successful!")
    print("Take your cash!")
   

def depositOperations():
    print("Deposit Operations")

    amountToDeposit = int(input("How much do you want to deposit? \n"))
    print("Transaction successful!")
    print("You deposited %d" % amountToDeposit)

def generateAccountNumber():
    #print("Generating Account Number.")
    return random.randrange(1111111111, 9999999999)

    


### ACTUAL BANKING SYSTEM ###


init()
