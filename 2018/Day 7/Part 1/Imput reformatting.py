Input = open('Input.txt', 'r')
in2 = []
for item in Input:
    in2.append(item.split(' '))
print(in2)

in3 = []
for item in in2:
    in4 = []
    in4.append(item[1])
    in4.append(item[7])
    in3.append(in4)
print(in3)

