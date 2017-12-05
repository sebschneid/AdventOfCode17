puzzle = open('./input1.txt').readlines()
count = 0
for line in puzzle:
    numbers = [int(x) for x in line.rstrip('\n').split()]
    diff = max(numbers) - min(numbers)
    count += diff