def getCode():
    input = open("input.txt", "r")
    inputArrStr = input.read().split(",")
    inputArr = []
    for item in inputArrStr:
        inputArr.append(int(item))
    return inputArr


def intcode(intArr):
    current = 0
    while True:
        instruction = int(str(intArr[current])[-2:])
        parameterModes = str(intArr[current])[:-2]
        while len(parameterModes) < 2:
            parameterModes = "0" + parameterModes
        print(instruction, parameterModes, current, intArr[current:current+4], len(intArr))
        if instruction == 1:
            if parameterModes == "00":
                intArr[intArr[current+3]] = intArr[intArr[current+1]] + intArr[intArr[current+2]]
            elif parameterModes == "01":
                intArr[intArr[current+3]] = intArr[current+1] + intArr[intArr[current+2]]
            elif parameterModes == "10":
                intArr[intArr[current+3]] = intArr[intArr[current+1]] + intArr[current+2]
            elif parameterModes == "11":
                intArr[intArr[current+3]] = intArr[current+1] + intArr[current+2]
            current += 4
        elif instruction == 2:
            if parameterModes == "00":
                intArr[intArr[current+3]] = intArr[intArr[current+1]] * intArr[intArr[current+2]]
            elif parameterModes == "01":
                intArr[intArr[current+3]] = intArr[current+1] * intArr[intArr[current+2]]
            elif parameterModes == "10":
                intArr[intArr[current+3]] = intArr[intArr[current+1]] * intArr[current+2]
            elif parameterModes == "11":
                intArr[intArr[current+3]] = intArr[current+1] * intArr[current+2]
            current += 4
        elif instruction == 3:
            intArr[intArr[current + 1]] = int(input("input: "))
            current += 2
        elif instruction == 4:
            print(intArr[intArr[current+1]])
            current += 2
        elif instruction == 5:
            if parameterModes == "00" or parameterModes == "01":
                if intArr[current + 1] != 0:
                    if parameterModes == "00":
                        current = intArr[intArr[current + 2]]
                    elif parameterModes == "01":
                        current = intArr[current + 2]
            elif parameterModes == "10" or parameterModes == "11":
                if intArr[intArr[current + 1]] != 0:
                    if parameterModes == "10":
                        current = intArr[intArr[current + 2]]
                    elif parameterModes == "11":
                        current = intArr[current + 2]
        elif instruction == 6:
            if parameterModes == "00" or parameterModes == "01":
                if intArr[current + 1] == 0:
                    if parameterModes == "00":
                        current = intArr[intArr[current + 2]]
                    elif parameterModes == "01":
                        current = intArr[current + 2]
            elif parameterModes == "10" or parameterModes == "11":
                if intArr[intArr[current + 1]] == 0:
                    if parameterModes == "10":
                        current = intArr[intArr[current + 2]]
                    elif parameterModes == "11":
                        current = intArr[current + 2]
        elif instruction == 7:
            if parameterModes == "00":
                if intArr[intArr[current+1]] < intArr[intArr[current+2]]:
                    intArr[intArr[current+3]] = 1
                else:
                    intArr[intArr[current+3]] = 0
            elif parameterModes == "01":
                if intArr[current+1] < intArr[intArr[current+2]]:
                    intArr[intArr[current+3]] = 1
                else:
                    intArr[intArr[current+3]] = 0
            elif parameterModes == "10":
                if intArr[intArr[current+1]] < intArr[current+2]:
                    intArr[intArr[current+3]] = 1
                else:
                    intArr[intArr[current+3]] = 0
            elif parameterModes == "11":
                if intArr[current+1] < intArr[current+2]:
                    intArr[intArr[current+3]] = 1
                else:
                    intArr[intArr[current+3]] = 0
            current += 4
        elif instruction == 8:
            if parameterModes == "00":
                if intArr[intArr[current+1]] == intArr[intArr[current+2]]:
                    intArr[intArr[current+3]] = 1
                else:
                    intArr[intArr[current+3]] = 0
            elif parameterModes == "01":
                if intArr[current+1] == intArr[intArr[current+2]]:
                    intArr[intArr[current+3]] = 1
                else:
                    intArr[intArr[current+3]] = 0
            elif parameterModes == "10":
                if intArr[intArr[current+1]] == intArr[current+2]:
                    intArr[intArr[current+3]] = 1
                else:
                    intArr[intArr[current+3]] = 0
            elif parameterModes == "11":
                if intArr[current+1] == intArr[current+2]:
                    intArr[intArr[current+3]] = 1
                else:
                    intArr[intArr[current+3]] = 0
            current += 4
        elif instruction == 99:
            return intArr
        if current > len(intArr):
            return intArr

intcode(getCode())
