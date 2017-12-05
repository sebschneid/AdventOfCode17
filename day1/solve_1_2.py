with open('input.txt') as f:
    riddle = f.readline()
    n = len(riddle)
    count = 0
    for i, s in enumerate(riddle[:n//2]):
        if s == riddle[i+n//2]:
            count += 2*int(s)

print(count)