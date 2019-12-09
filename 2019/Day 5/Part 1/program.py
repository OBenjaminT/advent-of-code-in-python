input = open("input.txt", "r")
inputArrStr = input.read().split(",")
inputArr = []
for item in inputArrStr:
    inputArr.append(int(item))


def intcode(intArr):
    i = 0
    current = 0
    while i != 99:
        instrLen = len(str(intArr[current]))
        if str(intArr[current])[-2: -1] == '01':
            if str(intArr[current])[-3] == '0':
                if str(intArr[current])[-4] == '0':
                    intArr[intArr[current + 3]] = intArr[intArr[current + 1]] + intArr[intArr[current + 2]]
                elif str(intArr[current])[-4] == '1':
                    intArr[intArr[current + 3]] = intArr[intArr[current + 1]] + intArr[current + 2]
            elif str(intArr[current])[-3] == '1':
                if str(intArr[current])[-4] == '0':
                    intArr[intArr[current + 3]] = intArr[current + 1] + intArr[intArr[current + 2]]
                elif str(intArr[current])[-4] == '1':
                    intArr[intArr[current + 3]] = intArr[current + 1] + intArr[current + 2]
        elif str(intArr[current])[-2: -1] == '02':
            if str(intArr[current])[-3] == '0':
                if str(intArr[current])[-4] == '0':
                    intArr[intArr[current + 3]] = intArr[intArr[current + 1]] * intArr[intArr[current + 2]]
                elif str(intArr[current])[-4] == '1':
                    intArr[intArr[current + 3]] = intArr[intArr[current + 1]] * intArr[current + 2]
            elif str(intArr[current])[-3] == '1':
                if str(intArr[current])[-4] == '0':
                    intArr[intArr[current + 3]] = intArr[current + 1] * intArr[intArr[current + 2]]
                elif str(intArr[current])[-4] == '1':
                    intArr[intArr[current + 3]] = intArr[current + 1] * intArr[current + 2]
        elif str(intArr[current])[-2: -1] == '03':
            intArr[intArr[current + 1]] = intArr[intArr[current + 2]]
        elif str(intArr[current])[-2: -1] == '04':
            print(intArr[intArr[current + 1]])
        current += instrLen
        if current >= len(intArr):
            return intArr


intcode(inputArr)
