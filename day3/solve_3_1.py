import math

def get_values_for_degree(deg_numb_dict, degree):
    for key, value in deg_numb_dict.items():
        for deg, number in value.items():
            if deg == degree:
                print(key, number)

def get_n(number):
    for n in range(int(math.sqrt(number))):
        if number > (2*n+1)**2 and number <= (2*(n+1)+1)**2:
            return n
        
def get_degree(deg_numb_dict, n, number):
    for key, val in deg_numb_dict[n].items():
        if val == number:
            return key

def get_difference(deg_numb_dict, number):
    n = get_n(number)
    degree = get_degree(deg_numb_dict, n, number)
    frac = int(degree/90)
    diff = min(abs(frac * 90 - degree), abs((frac + 1)*90 - degree))
    n_diff = diff / (45/(n+1))
    return 2*n - n_diff + 2       

def calc_manhattan_distance(number):
    n = get_n(number) + 1
    deg_diff = 45
    max_deg = 360
    degree_and_numbers = {}
    stable_degrees = list(range(0, max_deg, deg_diff))

    for n in range(n):
        degrees = stable_degrees.copy()
        for start, stop in zip(range(0, max_deg - deg_diff + 1, deg_diff), range(deg_diff, max_deg+1, deg_diff)):
            partials = [start + (stop - start)/(n+1) * (i+1) for i in range(n)]
            degrees.extend(partials)
            #print(partials)
        degrees.sort()
        degrees_new = degrees[1:]
        degrees_new.append(degrees[0])
        numbers = [(2*n+1)**2+i+1 for i in range(len(degrees_new))]
        degree_and_numbers[n] = {deg: number for deg, number in zip(degrees_new, numbers)}
        
    steps = get_difference(degree_and_numbers, number)
    return steps

calc_manhattan_distance(riddle)