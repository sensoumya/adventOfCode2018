import datetime
from operator import itemgetter
from collections import Counter


def input_getter():
    with open('Data/day04.txt', 'r') as f:
        # i = f.read().split('\n')[0]
        # print(datetime.datetime.strptime(i.split(']')[0][1:], '%Y-%m-%d %H:%M'))
        data = [[datetime.datetime.strptime(l.split(']')[0][1:], '%Y-%m-%d %H:%M'), l.split(']')[1].strip()] for l in f.read().split('\n')]
        data.sort(key=itemgetter(0))
        return data


def most_sleeper(data):
    sleep_time = Counter()
    id = 0
    for row in data:
        if '#' in row[1]:
            id = row[1].split(' ')[1][1:]
        if 'falls' in row[1]:
            start = row[0]
        if 'wakes' in row[1]:
            sleep_time[id] += int(divmod((row[0] - start).total_seconds(), 60)[0])
    return sleep_time.most_common(1)[0][0]


def min_cal(most_sleeper_id):
    most_slept_min = Counter()
    flag = False
    for row in data:
        if '#' in row[1]:
            if most_sleeper_id not in row[1]:
                flag = False
            else:
                flag = True
        if flag==True and 'falls' in row[1]:
            start = row[0].time().minute
        if flag==True and 'wakes' in row[1]:
            end = row[0].time().minute
            for i in range(start, end):
                most_slept_min[i] += 1
    return most_slept_min.most_common(1)[0][0]


data = input_getter()
most_sleeper_id = most_sleeper(data)
most_slept_min = min_cal(most_sleeper_id)
print(most_slept_min * int(most_sleeper_id))
# print(data)



def calc(data):
    min_counter = Counter()
    min_info = defaultdict(lambda: Counter())
    for row in data:
        if '#' in row[1]:
            id = row[1].split(' ')[1].split('#')[1]
        if 'falls' in row[1]:
            start = row[0].time().minute
        if 'wakes' in row[1]:
            end = row[0].time().minute
            for i in range(start, end):
                min_counter[i] += 1
                min_info[i][id]+=1
    min = int(min_counter.most_common(1)[0][0])
    id = int(min_info[min].most_common(1)[0][0])
    return min*id

print(calc(data))
