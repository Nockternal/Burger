
string = "Super Man"

stringupper = string.upper()
split_string = stringupper.split()

new_string_1 = ("^".join(split_string[0]))
new_string_2 = ("^".join(split_string[1]))

print(new_string_1, new_string_2)