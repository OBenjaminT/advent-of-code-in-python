# 156218-652527

def checkIfPass(i):
    i = str(i)
    double = False
    increase = False
    if i[1] == i[2] and i[0] != i[1] and i[2] != i[3]:
        double = True
    elif i[2] == i[3] and i[1] != i[2] and i[3] != i[4]:
        double = True
    elif i[3] == i[4] and i[2] != i[3] and i[4] != i[5]:
        double = True
    elif i[0] == i[1] and i[1] != i[2]:
        double = True
    elif i[4] == i[5] and i[4] != i[3]:
        double = True
    if int(i[0]) <= int(i[1]) and int(i[1]) <= int(i[2]) and int(i[2]) <= int(i[3]) and int(i[3]) <= int(i[4]) and int(
            i[4]) <= int(i[5]):
        increase = True
    if double and increase:
        return True
    else:
        return False





passcount = 0
for l in range(156218, 652528):
    if checkIfPass(l):
        passcount += 1

print(passcount)
