def get_purchase(): #repeatedly prompt user to input a price or q if invalid input retry prompt
    payment = (input('\nEnter the purchase price (xx.xx) or \'q\' to quit: ')) 
    if (payment) == 'q':
        total = n * 5 + d * 10 + q * 25 + o * 100 + f * 500
        print(f'\nTotal: {int(total/100)} dollars and {total % 100} cents')
        quit()
    else:
        payment = round(float(payment) * 100)
    if (payment) < 0 or (payment) % 5 != 0:
        print('Illegal price: Must be a non-negative multiple of 5 cents.')
        return get_purchase()
    return payment
def selection_menu(payment): #output payment amount owed as well testing input selection is valid
    if payment > 99:
        print(f'Payment due: {int(payment // 100)} dollar(s) and {int((payment)% 100)} cents')
    else:
        print(f'Payment due: {int((payment)% 100)} cents')
   
    selection = (input('Indicate your deposit: '))
    if selection == "n" or selection == "d" or selection == "q" or selection == "o" or selection == "f" or selection == "c":
        payment = stock_deposit(selection, payment, originalPayment) #calls stock deposit
        return (payment)
    else:
        print(f"Illegal selection: {selection}")    
    return selection_menu(payment) #if invalid selection recalls selection menu function again
def stock_deposit(selection, payment, originalPayment): #deduct from payment due and add coins and dollars to stock
    global n
    global d
    global q
    global o
    global f
    if selection == 'n':
        payment = payment - 5
        n += 1
    elif selection == 'd':
        payment = payment - 10
        d += 1
    elif selection == 'q':
        payment = payment - 25
        q += 1
    elif selection =='o':
        payment -= 100
        o += 1    
    elif selection == 'f':
        payment -= 500
        f += 1
    elif selection == 'c':
        return payment - originalPayment          
    else:
        pass
    return payment
def change_calculator(payment): #refund if c is called or user inputs amount over payment due
    global n
    global d
    global q
 
    giveN = 0
    giveD = 0
    giveQ = 0
    manager = False
    print('\nPlease take the change below.')
    payment = abs(payment)
    if payment == 0:
        print('No change due.')
    while payment > 0:
        if payment >= 25 and q > 0:
            giveQ += 1
            q -= 1
            payment -= 25
        elif payment >= 10 and d > 0:
            giveD += 1
            d -= 1
            payment -= 10
        elif payment >= 5 and n > 0:
            giveN += 1
            n -= 1
            payment -= 5
        else:
            manager = True
            break  
    if giveQ > 0:
        print(f"   {giveQ} quarters")
    if giveD > 0:
        print(f"   {giveD} dimes")
    if giveN > 0:
        print(f"   {giveN} nickels")
    if manager == True:
        noChange(payment) #only called if not enough coins in stock
    print()
def noChange(payment): #outputs machine does not have enough change
    if payment > 99:  
        print(f'Machine is out of change.\n'
            f'See store manager for remaining refund.\n'
            f'Amount due is: {int(payment / 100)} dollars and {int(payment % 100)} cents')
    else:
        print(f'Machine is out of change.\n'
            f'See store manager for remaining refund.\n'
            f'Amount due is: {int(payment % 100)} cents')

n = 25 #beginning stock of coins and dollars
d = 25
q = 25
o = 0
f = 0
print('Welcome to the vending machine change maker program \nChange maker initialized.')
while True:
    print(f'Stock contains:'
    f'\n   {n} nickels'
    f'\n   {d} dimes'
    f'\n   {q} quarters'
    f'\n   {o} ones'
    f'\n   {f} fives') #outputs stock
    payment = get_purchase() #price of item
    originalPayment = payment
    print('\n Menu for deposits:'
    '\n  \'n\' - deposit a nickel'
    '\n  \'d\' - deposit a dime'
    '\n  \'q\' - deposit a quarter'
    '\n  \'o\' - deposit a one dollar bill'
    '\n  \'f\' - deposit a five dollar bill'
    '\n  \'c\' - cancel the purchase \n') #menu for coin/bill depositing   
    while payment > 0: #repeats as long as the payment due is over 0
        payment = selection_menu(payment)
    change_calculator(payment)