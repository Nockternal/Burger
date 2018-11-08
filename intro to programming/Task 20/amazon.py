maximum = None
minimum = None
average = None
output = open("output.txt","w+")
with open("input.txt","r") as f:
    f_read = f.readlines()
    for line in f_read:
        if "min" in line:
            num = line.split(":")
            numbers = num[1]
            nums = numbers.split(",")
            minimum = str(min(nums))
            minwr = str(line)+ " is "+ str(minimum)+"\n"
            output.write(minwr)
        elif "max" in line:
            num = line.split(":")
            numbers = num[1]
            nums = numbers.split(",")
            maximum = str(max(nums))
            maxwr = str(line)+ " is "+ str(maximum)+"\n"
            output.write(maxwr)
        elif "avg" in line:
            num = line.split(":")
            numbers = num[1]
            nums = numbers.split(",")
            lenthx = len(nums)
            total = 0
            for i in nums:
                total = total + int(i)
            average = total/lenthx
            avgwr = str(line)+ " is "+ str(average)+"\n"
            output.write(avgwr)
output.close()

