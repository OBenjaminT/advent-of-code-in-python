input = open("Input.txt", "r")
inputV2 = ''
for line in input:
    inputV2 = inputV2 + line
reformatedInput = inputV2.split('\n')
reformatedInputV2 = []
'''
for item in reformatedInput:
    reformatedInputV3 = []
    for letter in item:
        reformatedInputV3.append(letter)
    reformatedInputV2.append(reformatedInputV3)'''
print(reformatedInput)
