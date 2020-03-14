def oneIteration():
    output = int(0)
    input = open("Input.txt", "r")
    for line in input:
        output = output + int(line)
    print('Solution to day 1 part 1: ', output)
    input.close()


def inputReformating():
    input = open("Input.txt", "r")
    inputV2 = ''
    for line in input:
        inputV2 = inputV2 + line
    reformatedInput = inputV2.split('\n')
    reformatedInputV2 = []
    for item in reformatedInput:
        reformatedInputV2.append(int(item))
    input.close()
    return reformatedInputV2


def muchIterations():
    output = int(0)
    previousOutputs = set()
    input = inputReformating()
    while True:
        for item in input:
            output = output + int(item)
            if output in previousOutputs:
                print(output)
                quit(2)
            else:
                previousOutputs.add(output)

'''
\r~W:&+:&mgq&h}1&:&mp|
\1WIE0|&
'''


oneIteration()
muchIterations()