input = open("input.txt", "r")
input = input.read()
print(len(input))


def imgSplitter(img, width, height):
    imgArrLayers = []
    for l in range(int(len(input)/(width*height))):
        imgArr = []
        for i in range(height):
            imgArr.append(list(str(str(img)[l*i*width+(i*width):l*i*width+((i+1)*width)])))
        imgArrLayers.append(imgArr)
    print(len(imgArrLayers))
    print((len(img)/width)/height)
    return imgArrLayers

def imgDoubleCheck(pixelArr, pixelList):
    same = True
    pixelArrToList = ""
    for i in range(len(pixelArr)):
        for l in range(len(pixelArr[i])):
            for r in range(len(pixelArr[i][l])):
                pixelArrToList += pixelArr[i][l][r]
    if pixelArrToList != pixelList:
        same = False
    print(same)

def imgSplitter(img, width, height):
    imgArrLayers = []
    for l in range(0, len(img), width*height):
        imgArrLayers.append(img[l:l+(width*height)])
    imgArrLines = []
    for layer in imgArrLayers:
        imgArrLine = []
        for l in range(0, len(layer), width):
            imgArrLine.append(layer[l:l+width])
        imgArrLines.append(imgArrLine)
    imgArrPixels = []
    for layer in imgArrLines:
        imgArrPixel = []
        for line in layer:
            imgArrPixel.append(list(line))
        imgArrPixels.append(imgArrPixel)
    return imgArrPixels


image = imgSplitter(input, 25, 6)
print(image)
topLayer = image[0]
for i in range(6):
    for l in range(25):
        layerNum = 0
        while topLayer[i][l] == "2" and layerNum < len(image):
            topLayer[i][l] = image[layerNum][i][l]
            layerNum += 1
for line in topLayer:
    print("".join(line))

imgDoubleCheck(imgSplitter(input, 25, 6), input)

#0110001100111100110011110
#1001010010100001001010000
#1000010000111001000011100
#1000010110100001011010000
#1001010010100001001010000
#0110001110111100111011110