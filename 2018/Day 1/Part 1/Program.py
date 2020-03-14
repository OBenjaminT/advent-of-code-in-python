output = int(0)
input = open("Input.txt", "r")
for line in input:
    output = output + int(line)
print(output)
input.close()