# Gabriel Crozier, Financial Calculator

def savings():
    print('\033c')
    print('This calculator is designed to calculate when you will reach a savings goal.\n\
This means you need to input the starting money amount, how frequently you deposit money, and how much you deposit each time.')
    startMoney = input('How much money are you starting with? --->  ')
    timeFrame = input("""How frequently are you depositing your money?
Day, Week, Month, or Year (You can choose the specifics later)
    --->  """)
    timeFrame = input(f'How many {timeFrame.lower() + 's'} between each deposit? --->  ')
    depositAmount = input('How much money are you depositing each time? --->  ')
    

def main():
    while True:
        options = input("""
What would you like to do?:
1. Savings Calculator
2. Compound Interest Calculator
3. Budget Calculator
4. Sale Price Calculator
5. Tip Calculator
Input the number corresponding to the option you would like to choose: 
    --->  """)
        if options.isdigit():
            options = int(options)
        else: options = 0
        if options == 1:
            savings()
        elif options == 2:
            pass
        elif options == 3:
            pass
        elif options == 4:
            pass
        elif options == 5:
            pass
        else:
            leaveQue = input('Your option was not valid, would you like to leave the calculator (y/n) --->  ')
            if leaveQue == 'y':
                break
            elif leaveQue == '':
                break



# Possibly connect numbers together to use in multiple senerios

# Savings Linear:
# Need starting money
# Need weekly / monethly, / other options for the person
# Need add money to account and check how long they plan to save

# Compound interest:
# Start money
# End Goal Time
# Interest Value
# How much per unit of time

# budget calculator:
# 
main()