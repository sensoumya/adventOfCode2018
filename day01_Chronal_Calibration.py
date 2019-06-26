with open('Data\\day01.txt', 'r') as f:
    nums = [int(line.strip()) for line in f]
    print(sum(nums))

def freq(nums):
    frequency = 0
    seen = set()
    while True:
        for num in nums:
            frequency += num
            if frequency in seen:
                return frequency
            seen.add(frequency)

print(freq(nums))