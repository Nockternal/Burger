
print ('the Criteria for a strong password is more than 6 characters with uppercase, lowercase and numbers in it')


password = input ('type your password    ....')

upcase = False
lowcase = False
passlenth = False
havenum = False

if len(password) >= 6 :
    passlenth = True
else:
    pass

for char in password:
    if char == (char.upper()):
        upcase = True
        break
    else:
        pass
for charx in password:
    if charx == (charx.lower()):
        lowcase = True
        break
    else:
        pass
for chary in password:
    if chary.isdigit():
        havenum = True
        break
    else:
        pass

if upcase and lowcase and passlenth == True:
    print("You have a strong enough password")

elif upcase and passlenth and havenum == True:
    print("You have a strong enough password")

elif upcase and lowcase and havenum == True:
    print("You have a strong enough password")

elif lowcase and passlenth and havenum == True:
    print("You have a strong enough password")

else:
    print("You have a weak password...")
