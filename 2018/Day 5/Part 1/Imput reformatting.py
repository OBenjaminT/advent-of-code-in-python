Input = open("Input.txt", "r")
input1 = []
for item in Input:
    input1.append(item)
Input.close()
for item in input1:
    input2 = list(item)

print(input2)
print(len(input2))
