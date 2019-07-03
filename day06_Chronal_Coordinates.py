from collections import Counter

with open('Data//day06.txt', 'r') as f:
    new_data = list(map(lambda x: (int(x.split(',')[0]), int(x.split(',')[1])), f.read().replace(' ', '').split('\n')))

#par1
def manhattan_dist(coord, data=new_data):
    distances = Counter()
    for point in new_data:
        dist = abs(point[0] - coord[0]) + abs(point[1] - coord[1])
        distances[point] = dist
    mc = distances.most_common()[::-1][:2]
    return (0, 0) if mc[0][1] == mc[1][1] else mc[0][0]


grid_size = (sorted(new_data, key=lambda x: x[0], reverse=True)[0][0], sorted(new_data, key=lambda x: x[1], reverse=True)[0][1])

coordinates = {}
for i in range(1, grid_size[0] + 1):
    for j in range(1, grid_size[1] + 1):
        coordinates[(i, j)] = manhattan_dist((i, j))

infinite_crd = set()
for i in [1, grid_size[0]]:
    for j in range(1, grid_size[1] + 1):
        infinite_crd.add(coordinates[(i, j)])
for i in [1, grid_size[1]]:
    for j in range(1, grid_size[0] + 1):
        infinite_crd.add(coordinates[(j, i)])

finite_crd = set(coordinates.values()) - infinite_crd

largest_sum = []
for i in finite_crd:
    largest_sum.append(sum(1 for k in coordinates.values() if k == i))

print(max(largest_sum))

# part 2
def tot_dist_calc(coord, data=new_data):
    dist = 0
    for point in new_data:
        dist += abs(point[0] - coord[0]) + abs(point[1] - coord[1])
    return dist

count = 0
for i in range(1, grid_size[0] + 1):
    for j in range(1, grid_size[1] + 1):
        tot_dist = tot_dist_calc((i, j))
        if tot_dist<10000:
            count += 1
print(count)
