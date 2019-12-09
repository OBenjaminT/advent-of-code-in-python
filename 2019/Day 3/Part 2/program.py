input = open("input.txt", "r")
inputArr1 = input.readline().split(",")
inputArr1[-1] = inputArr1[-1][:-1]
inputArr2 = input.readline().split(",")

def directionSplit(arr):
    array = []
    for item in arr:
        direction = [item[0], int(item[1:])]
        array.append(direction)
    return array

inputArr1 = directionSplit(inputArr1)
inputArr2 = directionSplit(inputArr2)

def map(array):
    coords = [[0, 0]]
    for item in array:
        if item[0] == "U":
            for i in range(item[1]):
                coords.append([coords[-1][-2], coords[-1][-1] + 1])
        elif item[0] == "D":
            for i in range(item[1]):
                coords.append([coords[-1][-2], coords[-1][-1] - 1])
        elif item[0] == "R":
            for i in range(item[1]):
                coords.append([coords[-1][-2] + 1, coords[-1][-1]])
        elif item[0] == "L":
            for i in range(item[1]):
                coords.append([coords[-1][-2] - 1, coords[-1][-1]])
    return set(tuple(i) for i in coords)

def minIntersection(c1, c2):
    intersections = cable1.intersection(cable2)
    intersections.remove((0, 0))
    minDist = 0
    for i in intersections:
        if abs(i[0]) + abs(i[1]) < minDist:
            minDist = abs(i[0]) + abs(i[1])
        elif minDist == 0:
            minDist = abs(i[0]) + abs(i[1])
    return minDist

cable1 = map(inputArr1)
cable2 = map(inputArr2)

def findDist(interCoord, cab):
    travel = 0
    coords = [[0, 0]]
    # while coords[-1]!= interCoord and interCoord != [0, 0]:
    for item in cab:
        if item[0] == "U":
            for i in range(item[1]):
                coords.append([coords[-1][-2], coords[-1][-1] + 1])
                travel += 1
                if coords[-1] == interCoord:
                    return travel
        elif item[0] == "D":
            for i in range(item[1]):
                coords.append([coords[-1][-2], coords[-1][-1] - 1])
                travel += 1
                if coords[-1] == interCoord:
                    return travel
        elif item[0] == "R":
            for i in range(item[1]):
                coords.append([coords[-1][-2] + 1, coords[-1][-1]])
                travel += 1
                if coords[-1] == interCoord:
                    return travel
        elif item[0] == "L":
            for i in range(item[1]):
                coords.append([coords[-1][-2] - 1, coords[-1][-1]])
                travel += 1
                if coords[-1] == interCoord:
                    return travel
    quit(1)

minTravel = 0
intersect = cable1.intersection(cable2)
intersect.remove((0, 0))
for i in intersect:
    if findDist(i, cable1) + findDist(i, cable2) < minTravel:
        minTravel = findDist(i, cable1) + findDist(i, cable2)
    elif minTravel == 0:
        minTravel = findDist(i, cable1) + findDist(i, cable2)
print(minTravel)
