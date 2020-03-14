def inputReformating():
    input = open("Input.txt", "r")
    inputV2 = ''
    for line in input:
        inputV2 = inputV2 + line
    reformatedInput = inputV2.split('\n')
    reformatedInputV2 = []
    for item in reformatedInput:
        reformatedInputV3 = []
        for letter in item:
            reformatedInputV3.append(letter)
        reformatedInputV2.append(reformatedInputV3)
    input.close()
    return reformatedInputV2


def part1():
    import collections
    twoLett = 0
    threeLett = 0
    Input = inputReformating()
    for item in Input:
        counter = collections.Counter(item)
        countervalues = counter.values()
        if 2 in countervalues:
            twoLett += 1
        if 3 in countervalues:
            threeLett += 1
    print(twoLett*threeLett)


def part2():
    Input = inputReformating()
    for i in range(0, len(Input)):
        for r in range(i, len(Input)):
            similarities = 0
            for l in range(0, 26):
                if Input[i][l] == Input[r][l]:
                    similarities += 1
            if similarities == 25:
                # you have to manually copy the correct letters
                print('List 1: ', ('').join(Input[i]), '\nList 2: ', ('').join(Input[r]))


part1()
part2()
