def coin_change(amount,currency):
    coin = []
    
    def AddCoin(): # Eh figure out later
        print(f"{coin}CUHHHHHHHHHHH")
        sum_ = sum(coin)
        print(f"{sum_}BUHHHHHHHHHHHHH")
        currency_ = [x for x in currency if x + sum_ <= amount]
        if sum_ < amount: AddCoin()
        coin.append(currency_[-1])
        
    coin = AddCoin()

coin_change(100,[1,5,10,25,50,100])