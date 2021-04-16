def accountNumberValidation(accountNumber):
    if accountNumber:
        if len(str(accountNumber)) == 10:

            try:
                int(accountNumber)
                return True
            except ValueError:
                print('Invalid Account Number. Account Number must be an integer.')
                return False

        else:
            print('Account Number must have only ten digits')
            return False
            

    else:
        print('This is a required field')
        return False
