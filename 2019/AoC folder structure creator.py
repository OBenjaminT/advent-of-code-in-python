import os
for i in range(2015, 2019):
    filePath = "C:/Users/TURNERO/PycharmProjects/Advent of code"
    os.makedirs(filePath + "/" + str(i))
    filePath = filePath + "/" + str(i)
    for i in range(1, 26):
        for r in range(1, 3):
            os.makedirs(filePath + "/Day " + str(i) + "/Part " + str(r))
            file = open(filePath + "/Day " + str(i) + "/Part " + str(r) + "/input.txt", "w+")
            file.close()
            file = open(filePath + "/Day " + str(i) + "/Part " + str(r) + "/program.py", "w+")
            file.close()
