def reactor(data):
    inp_len = len(input)
    output = [data[0]]
    i = 1
    while i<inp_len:
        if len(output) <1:
            output.append(data[i])
            i += 1
        elif data[i]==output[-1].swapcase():
            output.pop()
            i += 1
        else:
            output.append(data[i])
            i += 1
    return len(output)
  
  
def min_poly_len(data):
    unique_units = set(data.lower())
    removed_chars = Counter()
    for char in unique_units:
        new_data = data.replace(char,'').replace(char.upper(),'')
        poly_len = reactor(new_data)
        removed_chars[char] = poly_len
    return removed_chars.most_common()[::-1][0][1]
  
with open('../input/day05.txt'.'r')as f:
    data = f.read()

#part 1
print(reactor(data))


#part 2
print(min_poly_len(data))
