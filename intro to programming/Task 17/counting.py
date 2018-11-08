words = "Hi my name is burger"
wordic = {}

for char in words:
    if char in wordic:
        wordic[char] += 1
    else:
        wordic[char] = 1
    print(char)

print(wordic)
