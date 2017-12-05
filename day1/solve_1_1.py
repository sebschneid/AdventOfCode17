with open('input.txt') as f:
    riddle = f.readline()
    count = 0
    n = len(riddle)
    for i, s in enumerate(riddle):
        if i < n-1:
            if s == riddle[i+1]:
                count += int(s)
        else:
            if s == riddle[0]:
                count += int(s)
print(count)