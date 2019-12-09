input = open("input.txt", "r")
def fuelsFuelCounterUpper(mass):
    fuelsFuel = 0
    if int(int(mass) / 3) - 2 > 0:
        fuelsFuel += int(int(mass) / 3) - 2
        fuelsFuel += fuelsFuelCounterUpper(int(int(mass) / 3) - 2)
    return fuelsFuel


fuelCounterUpper = 0
for line in input:
    fuelCounterUpper += int(int(line)/3) - 2
    fuelCounterUpper += fuelsFuelCounterUpper(int(int(line)/3) - 2)

print(fuelCounterUpper)