number = int(input("Please enter number of students."))
datalist = []

for i in range(1,(number+1)):
    idnumber = input("Please enter the students ID number")
    datalist.append(idnumber)

f = open("RegForm.txt","w+")
for i in datalist:
    f.write(i+"\n")
f.close()
