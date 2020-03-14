Input = open("Input.txt", "r")
inputsplit = []
for line in Input:
    inputsplit.append(line.split(" "))
Input.close()
print(inputsplit)
print(len(inputsplit))

inputsub = []
for item in inputsplit:
    for thing in item:
        for char in ' ':
            inputsub.append(thing.replace(char, ''))
print(inputsub)
print(len(inputsub))

inputextract = []
inputext = []
for x in range(0, 4932, 4):
    inputext = [inputsub[x + 2], inputsub[x + 3]]
    inputextract.append(inputext)
print(inputextract)
print(len(inputextract))

inputre = []
for x in range(0, len(inputextract)):
    inputrex = [inputextract[x][0][:len(inputextract[x][0]) - 1], inputextract[x][1][:len(inputextract[x][1])]]
    inputre.append(inputrex)
print(inputre)
print(len(inputre))

inputfinal = []
for x in range(0, len(inputre)):
    inputfin = [inputre[x][0].split(','), inputre[x][1].split('x')]
    inputfina = [[int(inputfin[0][0])], [int(inputfin[0][1])], [int(inputfin[1][0])], [int(inputfin[1][1])]]
    inputfinal.append(inputfina)
print(inputfinal)
print(len(inputfinal))

inputfinal2 = []
for item in inputfinal:
    inputfinal3 = [item[0][0], item[1][0], item[2][0], item[3][0]]
    inputfinal2.append(inputfinal3)
print(inputfinal2)
print(len(inputfinal2))