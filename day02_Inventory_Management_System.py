from collections import Counter

# twice = 0
# thrice = 0

# def repeat_check(txt):
#     global twice
#     global thrice
#     counts = set(Counter(txt).values())
#     if 2 in counts:
#         twice+=1
#     if 3 in counts:
#         thrice+=1

# with open('Data\\day02.txt','r') as f:
#     for line in f:
#         repeat_check(line.strip())

# print(twice, thrice, twice*thrice)

#######################################################
#Part-2    %timeit - 42.3 ms ± 4.25 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)
def diff_finder(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if sum(1 for k in range(len(arr[i])) if arr[i][k]!=arr[j][k]) == 1:
                k = [k for k in range(len(arr[i])) if arr[i][k]!=arr[j][k]][0]
                return arr[i][:k]+arr[i][k+1:]

with open('Data\\day02.txt','r') as f:
    lines = f.read().split('\n')

print(diff_finder(lines))

#Alternative-Part-2   %timeit - 15.8 ms ± 325 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
def characters_in_common(ids):
    leave_one_outs = Counter()

    for box_id in ids:
        for i in range(len(box_id)):
            leave_one_out = tuple(box_id[:i] + "_" + box_id[(i+1):])
            leave_one_outs[leave_one_out] += 1
    print(''.join(leave_one_outs.most_common(2)[0][0]).replace('_',''))


with open('Data\\day02.txt','r') as f:
    ids = [line.strip() for line in f]

characters_in_common(ids)