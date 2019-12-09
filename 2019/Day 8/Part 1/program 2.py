input = open("input.txt", "r")
input = input.read()
print(len(input))


def imgSplitter(img, width, height):
    imgArrLayers = []
    for l in range(int(len(input)/(width*height))-1):
        imgArrLayers.append(str(str(img)[height*width+(l*height*width):height*width+((l+1)*height*width)]))
    return imgArrLayers

image = imgSplitter(input, 25, 6)

zeroCount = 0
oneTimesTwo = 0
print(image)
for layer in image:
    localZeroCount = str(layer).count("0")
    localOneTimesTwo = str(layer).count("1") * str(layer).count("2")
    if zeroCount == 0:
        oneTimesTwo = localOneTimesTwo
        zeroCount = localZeroCount
    elif localZeroCount < zeroCount:
        oneTimesTwo = localOneTimesTwo
        zeroCount = localZeroCount
    print(localZeroCount, localOneTimesTwo, zeroCount, oneTimesTwo)

print(oneTimesTwo)