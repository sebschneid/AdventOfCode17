import itertools as it
result = 0
with open('./input2.txt') as f:
    for line in f.readlines():
        n_even = 0
        line = line.rstrip('\n').split()
        numbers = [int(x) for x in line]
        for comb in it.combinations(numbers, 2):
            high = max(comb)
            low = min(comb)
            if high % low == 0:
                n_even += 1 
                result += high / low
print(result)