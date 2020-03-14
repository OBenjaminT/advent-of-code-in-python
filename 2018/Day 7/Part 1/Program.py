In = [['X', 'Q'], ['Y', 'P'], ['U', 'F'], ['V', 'S'], ['G', 'R'], ['T', 'P'], ['O', 'D'], ['R', 'I'], ['M', 'F'], ['L', 'C'], ['K', 'H'], ['D', 'H'], ['I', 'W'], ['S', 'C'], ['J', 'Z'], ['B', 'A'], ['A', 'W'], ['W', 'F'], ['P', 'E'], ['C', 'Q'], ['E', 'Z'], ['Q', 'F'], ['Z', 'F'], ['N', 'H'], ['H', 'F'], ['N', 'F'], ['K', 'D'], ['P', 'F'], ['Q', 'Z'], ['G', 'W'], ['E', 'N'], ['R', 'Z'], ['V', 'R'], ['Q', 'N'], ['U', 'L'], ['P', 'N'], ['S', 'Q'], ['G', 'S'], ['U', 'E'], ['M', 'I'], ['A', 'N'], ['W', 'H'], ['J', 'A'], ['M', 'S'], ['T', 'I'], ['E', 'Q'], ['C', 'Z'], ['B', 'H'], ['J', 'F'], ['G', 'E'], ['Q', 'H'], ['T', 'B'], ['V', 'B'], ['R', 'F'], ['V', 'H'], ['K', 'N'], ['A', 'H'], ['S', 'E'], ['I', 'N'], ['V', 'I'], ['M', 'E'], ['U', 'G'], ['J', 'N'], ['T', 'K'], ['D', 'N'], ['L', 'S'], ['P', 'Z'], ['X', 'S'], ['B', 'W'], ['R', 'M'], ['W', 'Q'], ['A', 'Z'], ['A', 'F'], ['G', 'T'], ['S', 'A'], ['J', 'E'], ['Y', 'N'], ['D', 'J'], ['D', 'S'], ['M', 'W'], ['U', 'T'], ['E', 'H'], ['S', 'W'], ['T', 'C'], ['A', 'P'], ['U', 'V'], ['U', 'J'], ['L', 'B'], ['L', 'N'], ['J', 'C'], ['L', 'Q'], ['K', 'B'], ['G', 'H'], ['W', 'Z'], ['C', 'E'], ['B', 'Q'], ['O', 'Z'], ['L', 'J'], ['R', 'N'], ['J', 'P'], ['Y', 'F']]
alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
InNew = [['A'],['B'],['C'],['D'],['E'],['F'],['G'],['H'],['I'],['J'],['K'],['L'],['M'],['N'],['O'],['P'],['Q'],['R'],['S'],['T'],['U'],['V'],['W'],['X'],['Y'],['Z']]
for item in In:
    InNew[alphabet.index(item[1])].append(item[0])
print(InNew)
instruction = []
completed = True
while completed is True:
    completed = False
    for item in InNew:
        if item[0] in instruction:
            pass
        elif len(item) == 1:
            instruction.append(item[0])
            for thing in InNew:
                if thing == item:
                    pass
                else:
                    for part in thing:
                        if part == item[0]:
                            print(InNew)
                            del InNew[InNew.index(thing)][InNew[InNew.index(thing)].index(part)]
            item = None
            completed = True
print(''.join(instruction))
