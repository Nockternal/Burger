def weekdays():
    weekdays_list = [
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
                     ]
    for i in weekdays_list:
        print(i)


def helloes(x):
    y = x.split()

    for word in y[::2]:
        id = y.index(word)
        y.insert(id, "Hello")
        y.remove(word)
        z = " ".join(y)

    return z

long_word = "one two three four"
weekdays()
print(helloes(long_word))

