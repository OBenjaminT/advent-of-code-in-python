def getCode():
    input = open("input.txt", "r")
    inputArrStr = input.read().split(",")
    inputArr = []
    for item in inputArrStr:
        inputArr.append(int(item))
    return inputArr


def intcode(intArr, input):
    current = 0
    while True:
        instruction = int(str(intArr[current])[-2:])
        parameterModes = str(intArr[current])[:-2]
        while len(parameterModes) < 3:
            parameterModes = "0" + parameterModes
        c0 = current
        c1 = current + 1
        c2 = current + 2
        c3 = current + 3
        ic0 = intArr[c0]
        ic1 = intArr[c1]
        ic2 = intArr[c2]
        ic3 = intArr[c3]
        try:
            pic1 = intArr[ic1]
        except:
            pass
        try:
            pic2 = intArr[ic2]
        except:
            pass
        try:
            pic3 = intArr[ic3]
        except:
            pass
        #if parameterModes[0] == 0:
        destination = ic3
        #else:
            #destination = c3
        # print(instruction, parameterModes, current, intArr[current:current+4], len(intArr))
        print(current, ic0, ic1, ic2, ic3, pic1, pic2)
        if instruction == 1:
            if parameterModes[-2:] == "00":
                intArr[destination] = pic1 + pic2
            elif parameterModes[-2:] == "01":
                intArr[destination] = ic1 + pic2
            elif parameterModes[-2:] == "10":
                intArr[destination] = pic1 + ic2
            elif parameterModes[-2:] == "11":
                intArr[destination] = ic1 + ic2
            current += 4
        elif instruction == 2:
            if parameterModes[-2:] == "00":
                intArr[destination] = pic1 * pic2
            elif parameterModes[-2:] == "01":
                intArr[destination] = ic1 * pic2
            elif parameterModes[-2:] == "10":
                intArr[destination] = pic1 * ic2
            elif parameterModes[-2:] == "11":
                intArr[destination] = ic1 * ic2
            current += 4
        elif instruction == 3:
            intArr[ic1] = int(input)
            current += 2
        elif instruction == 4:
            if parameterModes[-1] == "0":
                print(pic1)
            elif parameterModes[-1] == "1":
                print(ic1)
            current += 2
        elif instruction == 5:
            if parameterModes[-2] == "0":
                if pic1 != 0:
                    if parameterModes[-1] == "0":
                        current = pic2
                    elif parameterModes[-1] == "1":
                        current = ic2
                else:
                    current += 3
            elif parameterModes[-2] == "1":
                if ic1 != 0:
                    if parameterModes[-1] == "0":
                        current = pic2
                    elif parameterModes[-1] == "1":
                        current = ic2
                else:
                    current += 3
        elif instruction == 6:
            if parameterModes[-2] == "0":
                if pic1 == 0:
                    if parameterModes[-1] == "0":
                        current = pic2
                    elif parameterModes[-1] == "1":
                        current = ic2
                else:
                    current += 3
            elif parameterModes[-2] == "1":
                if ic1 == 0:
                    if parameterModes[-1] == "0":
                        current = pic2
                    elif parameterModes[-1] == "1":
                        current = ic2
                else:
                    current += 3
        elif instruction == 7:
            if parameterModes[-2:] == "00":
                if pic1 < pic2:
                    intArr[destination] = 1
                else:
                    intArr[destination] = 0
            elif parameterModes[-2:] == "01":
                if pic1 < ic2:
                    intArr[destination] = 1
                else:
                    intArr[destination] = 0
            elif parameterModes[-2:] == "10":
                if ic1 < pic2:
                    intArr[destination] = 1
                else:
                    intArr[destination] = 0
            elif parameterModes[-2:] == "11":
                if ic1 < ic2:
                    intArr[destination] = 1
                else:
                    intArr[destination] = 0
            current += 4
        elif instruction == 8:
            if parameterModes[-2:] == "00":
                if pic1 == pic2:
                    intArr[destination] = 1
                else:
                    intArr[destination] = 0
            elif parameterModes[-2:] == "01":
                if pic1 == ic2:
                    intArr[destination] = 1
                else:
                    intArr[destination] = 0
            elif parameterModes[-2:] == "10":
                if ic1 == pic2:
                    intArr[destination] = 1
                else:
                    intArr[destination] = 0
            elif parameterModes[-2:] == "11":
                if ic1 == ic2:
                    intArr[destination] = 1
                else:
                    intArr[destination] = 0
            current += 4
        elif instruction == 99:
            return intArr
        if current > len(intArr):
            return intArr


intcode(getCode(), 5)
