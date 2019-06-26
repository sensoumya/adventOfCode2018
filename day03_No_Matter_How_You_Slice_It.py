from collections import defaultdict

fabric_inch = defaultdict(int)

with open('Data\\day03.txt','r') as f:
    for line in f.read().split('\n'):
        left, top = map(int,line.split(' ')[2][:-1].split(','))
        x, y = map(int,line.split(' ')[3].split('x'))
        # print(left,top,x,y)
        for i in range(top,top+y):
            for j in range(left,left+x):
                fabric_inch[(i,j)] += 1

print(sum(1 for i in fabric_inch.values() if i>1))