input = open("input.txt", "r")
fuelCounterUpper = 0
for line in input:
    fuelCounterUpper += int(int(line)/3) - 2
print(fuelCounterUpper)