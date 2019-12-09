input = open("input.txt", "r")
inputArrStr = input.read().split(",")
inputArr = []
for item in inputArrStr:
    inputArr.append(int(item))
inputArr[1] = 12
inputArr[2] = 2

def intcode(intArr):
    i = 0
    current = 0
    print(intArr)
    while i != 99:
        if intArr[current] == 1:
            intArr[intArr[current+3]] = intArr[intArr[current+1]] + intArr[intArr[current+2]]
        elif intArr[current] == 2:
            intArr[intArr[current + 3]] = intArr[intArr[current + 1]] * intArr[intArr[current + 2]]
        current += 4
        if current > len(intArr):
            return intArr

print(intcode(inputArr)[0])
