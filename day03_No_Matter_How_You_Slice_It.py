from collections import Counter

fabric_inch = Counter()
rectangles = {}

with open('../input/day03.txt','r') as f:
    for line in f.read().split('\n'):
        items = line.split(' ')
        id = int(items[0][1:])
        left, top = map(int,items[2][:-1].split(','))
        x, y = map(int,items[3].split('x'))
        rectangles[id] = []
        for i in range(top,top+y):
            for j in range(left,left+x):
                fabric_inch[(i,j)] += 1
                rectangles[id].append((i,j))

print('Square inches having 2 or more claim: ', sum(1 for i in fabric_inch.values() if i>1))


for id in rectangles:
    tag = True
    for inch in rectangles[id]:
        if fabric_inch[inch] >1:
            tag = False
            break
    if tag == True:
        print('Id of the claim that doesn\'t have overlap: ',id)
        break
