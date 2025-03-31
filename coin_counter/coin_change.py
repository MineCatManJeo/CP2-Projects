def coin_change(amount,currency):
    coin = []
    
    def add_coin(): # Eh figure out later
        while True:
            sum_ = sum(coin) # Gets the sum of the current solution
            currency_ = [x for x in currency if x + sum_ <= amount] # Gets the currency value deliminators and if added to sum > amount then dont use it
            try: coin.append(currency_[-1]) # Tries to append it, sometimes there may not be a currency
            except: 
                if amount - sum_ > 0:
                    print(f"With the currency provided there is an unavoidable remainder of ${amount-sum_}") # Checks if there is a remainder (there shouldn't be but just in case)
                return
    add_coin()
    return coin