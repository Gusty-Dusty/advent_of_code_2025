import numpy as np
import timeit

def read_file(file_path):
    with open(file_path, "r") as file:
        data = file.read()
        return data
    
def evaluate(data, key, value):
    sides = 0
    for i in range(3):
        for x in range(3):
            move_y = i - 1
            move_x = x - 1
            key_to_check = (key[0] + move_y, key[1] + move_x)
            if key_to_check != key:
                sides += sides_check(data, key_to_check)
    if sides < 4:
        data[key] = 0
        return 1
    else:
        return 0

def sides_check(data, key):
    if key[0] < 0 or key[0] > data.shape[0] or key[1] < 0 or key[1] > data.shape[1]:
        return 0
    try:
        if data[key] == 1:
            return 1
        else:
            return 0
    except:
        return 0

def problem_one(data):
    paper = []
    total = 0
    for line in data.splitlines():
        row = []
        for item in line:
            if item == "@":
                row.append(1)
            else:
                row.append(0)
        paper.append(row)
    warehouse = np.array(paper)
    for key, value in np.ndenumerate(warehouse):
        if value == 0:
            continue
        else:
            total += evaluate(warehouse, key, value)
    return total

def problem_two(data):
    paper = []
    total = 0
    for line in data.splitlines():
        row = []
        for item in line:
            if item == "@":
                row.append(1)
            else:
                row.append(0)
        paper.append(row)
    warehouse = np.array(paper)
    while True:
        loop = 0
        for key, value in np.ndenumerate(warehouse):
            if value == 0:
                continue
            else:
                loop += evaluate(warehouse, key, value)
        total += loop
        if loop == 0:
            break  
    return total


if __name__ == "__main__":
    data01 = read_file("day04/1.txt")
    data02 = read_file("day04/example.txt")
    start_1 = timeit.default_timer()
    answer_1 = problem_one(data01)
    print(f"Part 1: {answer_1}")
    stop_1 = timeit.default_timer()
    print(f"Func took {round(stop_1 - start_1,4)*1000} milliseconds")
    start_2 = timeit.default_timer()
    answer_2 = problem_two(data01)
    print(f"Part 2: {answer_2}")
    stop_2 = timeit.default_timer()
    print(f"Func took {round(stop_2 - start_2,4)*1000} milliseconds")
