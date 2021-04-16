import random
import validation
database = {
    8537385884:[ 'Nonye', 'Ana', 'nonye@zuri.team', 'ana' , 0]
}

def init():
    print('Welcome to Bank Providus')
    isValidOptionSelected = False
    

    while isValidOptionSelected == False:
        haveAccount = int(input('Do you have an account with us? 1 (yes) or 2 (no) \n'))

        if (haveAccount == 1):
            isValidOptionSelected = True
            login()
        elif (haveAccount ==2):
            isValidOptionSelected = True
            print( register())

        else:
            print ('You have entered incorrect options')
            init()

def login ():
    print('***** Please Login *****')

    accountNumberFromUser = input('Enter your Account Number \n')
    isValidAccountNumber = validation.accountNumberValidation(accountNumberFromUser)

    if  isValidAccountNumber:
        password = input('Enter your Pin \n')

        for accountNumber, userDetails in database.items():
            if accountNumber == int(accountNumberFromUser):
                if (userDetails[3] == password):
                    bankOperation(userDetails)
                            
        print('*** Invalid Account or Password! ***')
        login()
    else:
        login()
    



def register(): 
    print('****** Please Register *********')
    email = input('What is your email address \n')
    firstName = input('What is your First Name? \n')
    lastName = input('What is your Last Name? \n')
    password= input('Create a Password \n')
    
    accountNumber = generateAccountNumber()
    
    #adding the registered users to the database
    database[accountNumber] = [firstName, lastName, email, password, 0]
    print('**** Account Creation Successful! ****')
    print('=== === === === === === === === === ===')
    print('This is your Account Nunber: %d' % accountNumber)
    print('Please keep this number safe!')
    
    login()


def bankOperation(user):
    print('Welcome %s %s' % (user[0], user[1]))
    print('What would you like to do?')
    selectedOption = int(input('1.Deposit   2.  Withdrawal  3.   Logout   4.  Exit  \n'))

    if (selectedOption == 1):
        deposit(user)
    elif(selectedOption == 2):
        withdrawal(user)
    elif (selectedOption == 3):
         logout()
    elif (selectedOption == 4):
         exit()
    else:
        print('*** Invalid option selected! ***')
        bankOperation(user)


def generateAccountNumber():
    return random.randrange(1111111111, 9999999999)

def setCurrentBalace(user, balance):
    user[4] = balance

def getCurrentBalace(user):
    return user[4] 

def withdrawal(user):
     amount = int(input('Please enter withdrawal anount \n'))
     
     if (user[4] >= amount):
        withdrawn = user[4] - amount 
        print ('Transaction Sucessful!')
        print('Your current balance is : %d' % withdrawn)
        print ('Thank You!')
        bankOperation(user)
     else:
        print('**** Insuficient Funds ****')
        print('Make a Deposit')

        bankOperation(user)


def deposit(user):
    amount = int(input('Please enter amount to be deposited \n'))
    deposit = user[4] + amount
    print ('Transaction Sucessful!')
    print('Your current balance is : %d' % deposit)
    print ('Thank You!')
    bankOperation(user)

def logout():
    print('***** LOGGED OUT *****')
    init()
####ACTUAL BANKING SYSTEM####
init()
#print(getCurrentBalace(user))