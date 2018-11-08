with open("DOB.txt","r") as f:
    f_line = f.readlines()
    #print(f_line)
    linenumber = 0
    for l in f_line:
        linenumber += 1
        newlist = l.split()
        name = newlist[0]
        initial = name[0]
        surname = newlist[1]
        date = newlist[2] + " " + newlist[3] + " " + newlist[4]
        print("Name")
        print(str(linenumber)+". ",initial,surname)
        print("Birth Date")
        print(str(linenumber)+". ", date)


