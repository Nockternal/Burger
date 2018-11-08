location = {"johannesburg":100,"durban":600,"capetown":1200}
products = {"apples":10,"pears":12,"bananas":9}
cart = []
cost = 0

def locations_list():
    print("__________________________________________________________")
    for k, v in location.items():
        print(k,"- ", v,"Km")
    print("__________________________________________________________")

def prod_list():
    print("__________________________________________________________")
    for k, v in products.items():
        print(k,"- R", v)
    print("__________________________________________________________")

def distance(x):
    cart.append(location[x])

def travel_cost_air(y):
    cart.append(y * 0.36)

def travel_cost_freight(z):
    cart.append(z * 0.25)

def gift():
    cart.append(15)

def full_insure():
    cart.append(50)

def limit_insure():
    cart.append(25)

def priority():
    cart.append(100)

def standard():
    cart.append(20)

adding = "n"
print(prod_list())
print(locations_list())

destination = input("what city to you need delivery in (johannesburg,durban,capetown) ")
adding = input("would you like to add an item (y/n) ")

while adding == "y":
    item = input("please enter what item you would like to add from the list {} ".format(prod_list()))
    quantity = int(input("How many would you like to add"))
    cart.append(products[item] * quantity)
    adding = input("would you like to add an item (y/n) ")

travel_method = input("will you be sending good via air,freight ")
gift_question = input("would you like to add a gift y/n")
insurance = input("what type of insurance do you need limited/full")
delivery = input("what prority does your delivery need to have standard/priority")

if travel_method == "air":
    travel_cost_air(location[destination])
else:
    travel_cost_freight(location[destination])

if gift_question == "y":
    gift()
else:
    pass

if insurance == "full":
    full_insure()
else:
    limit_insure()

if delivery == "priority":
    priority()
else:
    standard()

for i in cart:
    cost = cost + i

print("=============================================")
print("your total cost is >  {}".format(cost))
print("=============================================")


