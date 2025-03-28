def coin_change(amount,currency):
    coin = []
    
    def add_coin(): # Eh figure out later
        while True:
            sum_ = sum(coin)
            currency_ = [x for x in currency if x + sum_ <= amount]
            try: coin.append(currency_[-1])
            except: 
                if amount - sum_ > 0:
                    print(f"With the currency provided there is an unavoidable remainder of ${amount-sum_}")
                return
    add_coin()
    return coin