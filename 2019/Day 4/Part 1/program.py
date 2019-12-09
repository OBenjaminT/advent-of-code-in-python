# 156218-652527
passcount = 0
for i in range(156218, 652528):
    i = str(i)
    double = False
    increase = False
    if i[0] == i[1] or i[1] == i[2] or i[2] == i[3] or i[3] == i[4] or i[4] == i[5]:
        double = True
    if int(i[0]) <= int(i[1]) and int(i[1]) <= int(i[2]) and int(i[2]) <= int(i[3]) and int(i[3]) <= int(i[4]) and int(i[4]) <= int(i[5]) :
        increase = True
    if double and increase:
        passcount += 1
print(passcount)