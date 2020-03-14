Input = open("Input.txt", "r")
input1 = []
for item in Input:
    input1.append(item.split(' '))
print(input1)

input2 = []
for item in input1:
    input21 = [item[0][1:], item[1][:5], item[2:]]
    input2.append(input21)
print(input2)

input3 = []
for item in input2:
    input31 = [item[0].split("-"), item[1].split(":"), item[2:]]
    input3.append(input31)
print(input3)

def bubleSort(S):
    N = len(S)
    swaped = True
    while swaped is True:
        swaped = False
        for x in range(1, N - 1):
            if int(S[x - 1][1][1]) > int(S[x][1][1]):
                temp = S[x - 1]
                S[x - 1] = S[x]
                S[x] = temp
                swaped = True
    return S


inputbefmid = []
inputaftmid = []
for item in input3:
    if int(item[1][0]) == 23:
        inputbefmid.append(item)
    elif int(item[1][0]) == 00:
        inputaftmid.append(item)
print('inputbefmid: ', inputbefmid)
print('inputaftmid: ', inputaftmid)
fullorder = [bubleSort(inputbefmid), bubleSort(inputaftmid)]
print(fullorder)

reformattedfullorder = []
date = []
time = []
order = []
for thing in fullorder[0]:
    date.append(thing[0][0])
    date.append(thing[0][1])
    date.append(thing[0][2])
    time.append(thing[1][0])
    time.append(thing[1][1])
    order.append(thing[2][0][:])
for thing in fullorder[1]:
    date.append(thing[0][0])
    date.append(thing[0][1])
    date.append(thing[0][2])
    time.append(thing[1][0])
    time.append(thing[1][1])
    order.append(thing[2][0][:])
print(len(date), date)
print(len(time), time)
print(len(order), order)
while len(date) > 0:
    useless = date.pop(0)
    reformatinguseless = []
    reformatinguseless.append(int(date.pop(0)))
    reformatinguseless.append(int(date.pop(0)))
    reformatinguseless.append(int(time.pop(0)))
    reformatinguseless.append(int(time.pop(0)))
    reformatinguseless.append(order.pop(0))
    reformattedfullorder.append(reformatinguseless)
print(len(reformattedfullorder))
print(reformattedfullorder)
