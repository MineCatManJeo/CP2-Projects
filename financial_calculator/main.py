# Gabriel Crozier, Financial Calculator
def check_float(input_text):
    for i in range(5):
        inputed_value = input(input_text)
        try:
            inputed_value = float(inputed_value)
            break
        except:
            print('\nThat was not a number, please try again.')
    else:
        inputed_value = 0
        print('\nError too many attempts, defaulted to 0.')
    return inputed_value
            
def savings():
    print('This calculator is designed to calculate when you will reach a savings goal.')
    startMoney = check_float('How much money are you starting with? --->  ')
    timeFrame = input("""How frequently are you depositing your money?
Day, Week, Month, or Year (You can choose a more exact amount of time later)
    --->  """)
    NumTimeFrame = int(check_float(f'How many {timeFrame.lower()}s between each deposit? --->  '))
    depositAmount = check_float('How much money are you depositing each time? --->  ')
    if depositAmount <= 0: depositAmount = 1
    finalGoal = check_float('How much money are you saving for? --->  ')
    if NumTimeFrame < 1: NumTimeFrame = 1
    if NumTimeFrame == 1:
        print(f'\nWith a starting cash amount of ${startMoney:.2f} you added ${depositAmount:.2f} each {timeFrame.lower()} with the end goal of ${finalGoal:.2f}')
    else:
        print(f'\nWith a starting cash amount of ${startMoney:.2f} you added ${depositAmount:.2f} every {NumTimeFrame} {timeFrame.lower()}s with the end goal of ${finalGoal:.2f}')
    amount = int(((finalGoal - startMoney) / depositAmount)-0.001) + 1
    print(f'It will take you {amount*NumTimeFrame} {timeFrame.lower()}s to reach ${finalGoal:.2f} with ${(amount*depositAmount)+startMoney-finalGoal} left over.')
    
def compound():
    print('This is a compound intrest calculator\n')
    startMoney = check_float('How much money are you starting with? --->  ')
    intrest = check_float('What is the intrest rate? Ex: __% --->  ')/100
    timeFrame = check_float("""How frequently are you compounding this?
Day = 365, Week = 52, Month = 12, Year = 1
  --->  """)
    if timeFrame <= 0: timeFrame = 1
    yearCount = check_float('How many years will you be compounding this money? --->  ')
    compoundedMoney = round(startMoney*(1+(intrest/timeFrame))**(timeFrame*yearCount),2)
    if compoundedMoney < 1e10:
        compoundedMoney = f'{compoundedMoney:,}'
    else:
        compoundedMoney = f'{compoundedMoney:g}'
    print(f'After {int(yearCount)} years you will have ${compoundedMoney}')

def budget():
    print('This is a budget allocator calculator')
    money = check_float('How much money are you allocating? --->  ')
    budgetGroups = {}
    for i in range(10):
        spend_category = input('What are you spending money on? (Hit enter if you are done) --->  ').lower()
        if spend_category == '': break
        percent = check_float('What percentage of this would you like to allocate to your money? Ex: __% --->  ')
        budgetGroups[spend_category] = percent
        sumOfPercent = sum(budgetGroups.values())
        if sumOfPercent > 100: 
            budgetGroups[spend_category] = 100 - (sumOfPercent-percent)
            break
        if sumOfPercent == 100: break
        print(f'\nTotal percent: {sumOfPercent}%')
    print('\033cAllocations:')
    for group in budgetGroups:
        print(f'{group.upper()}: ${int(round(money*(budgetGroups[group]/100),0)):,} ({budgetGroups[group]:.1f}%)')

def sale_price():
    print('This calculates the price of a discounted item.\n')
    itemPrice = check_float('What is the items origional price? --->  ')
    discount = check_float('What is the disount for the item? Ex: __% --->  ')/100
    if discount >= 1:
        discount = 0.99
        print(f'You cannot have more than a 100% discount, defaulted to 99%.\n')
    print(f'The item you are trying to buy now costs ${itemPrice*(1-discount)}.')

def tip_calc():
    print('This calculates tips.')
    origional_price = check_float('What is the origional price? --->  ')
    tip = check_float('What is the tip? Ex: __% --->  ')/100
    print(f'The item now costs ${origional_price*(1+tip)}.')

def main():
    print('\033c')
    while True:
        options = input("""
What would you like to do?:
1. Savings Calculator
2. Compound Interest Calculator
3. Budget Calculator
4. Sale Price Calculator
5. Tip Calculator
6. Exit Calculator
Input the number corresponding to the option you would like to choose: 
    --->  """)
        if options.isdigit():
            options = int(options)
            print('\033c')
        else: 
            options = 0
            print('\033c')
        if options == 1:
            savings()
        elif options == 2:
            compound()
        elif options == 3:
            budget()
        elif options == 4:
            sale_price()
        elif options == 5:
            tip_calc()
        elif options == 6:
            print('\033c')
            print('Thank you for using this calculator!\n')
            break
        else:
            leaveQue = input('Your option was not valid, would you like to leave the calculator (y/n) --->  ')
            if leaveQue == 'y' or leaveQue == '':
                print('\033c')
                print('Thank you for using this calculator!\n')
                break

main()