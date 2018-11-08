
removel_list = []

sentence = input("Please enter a centence. ")


removal = input("would you like to remove a character y/n")

while removal == "y":
    char = input("Please enter character you want to remove")
    removel_list.append(char)
    removal = input("would you like to remove a character y/n")

for i in removel_list:
    sentence = sentence.replace(i,"")


print(sentence)
