input = open("input.txt", "r")
inputArr = []
from math import atan

def viewCount(asteroids, station):
	visibleAsteroids = []
	for asteroid in asteroids:
		x = station[0]-asteroid[0]
		y = station[1]-asteroid[1]
		if x != 0 and y != 0:
			if any(atan(y/x) not in a for a in visibleAsteroids):
				visibleAsteroids.append([asteroid[0], asteroid[1], atan(y/x)])
		else:
			if any(0 not in a for a in visibleAsteroids):
				visibleAsteroids.append([asteroid[0], asteroid[1], 0])
	return len(visibleAsteroids)



for line in input:
	inputArr.append(list(line[:-1]))
asteroids = []
for l in range(len(inputArr)):
	for i in range(len(inputArr[l])):
		if inputArr[l][i] == '#':
			asteroids.append([l, i])
print(asteroids)
maxView = 0
maxViewStation = []
for asteroid in asteroids:
	viewcount = viewCount(asteroids, asteroid)
	if viewcount > maxView:
		maxView = viewcount
		maxViewStation = asteroid

print(maxView)
print(maxViewStation)