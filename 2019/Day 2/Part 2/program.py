

def intcode(intArr):
    i = 0
    current = 0
    while i != 99:
        if intArr[current] == 1:
            intArr[intArr[current+3]] = intArr[intArr[current+1]] + intArr[intArr[current+2]]
        elif intArr[current] == 2:
            intArr[intArr[current + 3]] = intArr[intArr[current + 1]] * intArr[intArr[current + 2]]
        current += 4
        if current > len(intArr):
            return intArr

noun = None
verb = None
for i in range(100):
    for l in range(100):
        input = open("input.txt", "r")
        inputArrStr = input.read().split(",")
        inputArr = []
        for item in inputArrStr:
            inputArr.append(int(item))
        inputArr[1] = i
        inputArr[2] = l
        if intcode(inputArr)[0] == 19690720:
            noun = i
            verb = l
            print((noun * 100) + verb)
            quit(1)