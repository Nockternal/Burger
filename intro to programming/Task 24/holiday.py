#var is number of days to stay interger
def hotelcost(x):
    price = 1500
    y = x * price
    return y


#var is destination in string
def plane(x):
    jhb = 800
    dur = 1400
    cpt = 2500

    if x == "jhb":
        return jhb
    elif x == "dur":
        return dur
    elif x == cpt:
        return cpt


#var is number of days to rent car interger
def car(x):
    price = 240
    y = x * price
    return y

def holidaycost(h,p,c):
    h = hotelcost(h)
    p = int(plane(p))
    c = car(c)
    y = h+p+c
    return "Total Price is   R{}".format(y)

hotel = int(input("How many night will you stay at Hotel"))
plane_flight = input("Which city are you flying to (jhb/dur/cpt)")
car_rent = int(input("How many days do you need a rental car for"))

print(holidaycost(hotel,plane_flight,car_rent))
