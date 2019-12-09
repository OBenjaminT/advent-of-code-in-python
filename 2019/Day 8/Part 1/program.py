input = open("input.txt", "r")
input = input.read()
print(len(input))


def imgSplitter(img, width, height):
    imgArrLayers = []
    for l in range(int(len(input)/(width*height))):
        imgArr = []
        for i in range(height):
            imgArr.append(str(str(img)[l*i*width+(i*width):l*i*width+((i+1)*width)]))
        imgArrLayers.append(imgArr)
    return imgArrLayers

image = imgSplitter(input, 25, 6)

zeroCount = 0
oneTimesTwo = 0
print(image)
for layer in image:
    print(layer)
    localZeroCount = 0
    localOneCount = 0
    localTwoCount = 0
    for line in layer:
        print(line)
        localZeroCount += str(line).count("0")
        localOneCount += str(line).count("1")
        localTwoCount += str(line).count("2")
    localOneTimesTwo = localOneCount * localTwoCount
    if zeroCount == 0:
        oneTimesTwo = localOneTimesTwo
        zeroCount = localZeroCount
    elif localZeroCount < zeroCount:
        oneTimesTwo = localOneTimesTwo
        zeroCount = localZeroCount
    print(localZeroCount, localOneTimesTwo, zeroCount, oneTimesTwo)

print(oneTimesTwo)