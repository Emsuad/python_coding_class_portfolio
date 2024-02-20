def usd_to_euro(amount):
    return amount *0.92

def euro_to_usd (amount):
    return amount / 1.08

def usd_to_gbp (amount):
    return amount *0.79

def gbp_to_usd(amount):
    return amount / 1.27

def usd_to_NGN(amount):
    return amount * 1606

def NGN_to_usd(amount):
    return amount /1606

def main():
    print('Welcome to your currency converter \n Enter any number below to state your conversion:')
    print ('1. for USD to Euro')
    print ('2. for Euro to USD')
    print ('3. for USD to GBP')
    print ('4. for GBP to USD')
    print ('5. for USD to NGN')
    print ('6. for NGN to USD')

    choice = int(input('Enter your choice number:'))

    amount = float(input('Enter the amount for concersion:'))

    if choice ==1:
        print(f' ${amount} is {usd_to_euro(amount)} Euro') 
    elif choice ==2:
        print (f' {amount} Euro is ${euro_to_usd (amount)}')
    elif choice ==3:
        print (f' ${amount} is {usd_to_gbp (amount)} GBP')
    elif choice ==4:
        print (f' {amount} GBP is ${euro_to_usd (amount)}')
    elif choice ==5:
        print (f' ${amount} is #{usd_to_NGN(amount)} ')
    elif choice ==6:
        print (f'#{amount} is ${NGN_to_usd(amount)}')
    else:
        print('Invalid entry')

if __name__=='__main__':
    main()

