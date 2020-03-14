input = open("Input.txt", "r")
inputV2 = ''
for line in input:
    inputV2 = inputV2 + line
reformatedInput = inputV2.split('\n')
reformatedInputV2 = []
for item in reformatedInput:
    reformatedInputV2.append(int(item))
print(reformatedInputV2)
