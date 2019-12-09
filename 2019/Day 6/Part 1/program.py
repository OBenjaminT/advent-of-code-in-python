from anytree import Node

input = open("input.txt", "r")
orbitMap = []
for line in input:
    orbitMap.append(line[:-1].split(")"))
COM = Node("COM")
while len(orbitMap) > 0:
    orbitMapRemoved = []
    for item in orbitMap:
        print(len(orbitMapRemoved))
        print(item[0], COM.children)
        if item[0] in COM.children[-3:]:
            exec(item[1] + " = " + "Node(" + item[1] + ", parent=" + item[0] + ")")
        elif item[0] == COM:
            exec(item[1] + " = " + "Node(" + item[1] + ", parent=" + item[0] + ")")
        else:
            orbitMapRemoved.append(item)
    orbitMap = orbitMapRemoved
print(COM.children)