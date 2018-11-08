menu = ["coffee","tea","late","cuppachino"]
stock = {"coffee":12,"tea":10,"late":8,"cuppachino":5}
price = {"coffee":22.0,"tea":18.5,"late":24.0,"cuppachino":25.0}

for ik,iv in stock.items():
    #print(i)
    #print(j)
    for k,v in price.items():
        if ik == k:
            print("Stock worth for",ik,"is",(iv*v))

