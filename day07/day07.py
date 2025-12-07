import numpy as np
import timeit

def read_file(file_path):
    with open(file_path, "r") as file:
        data = file.read()
        return data
    
def move(map, location):
    if map[(location[0]+1, location[1])] == "1":
        map[(location[0]+1, location[1]-1)] = "S"
        map[(location[0]+1, location[1]+1)] = "S"
        return 1
    else:
        map[(location[0]+1, location[1])] = "S"
        return 0


def problem_one(data):
    total = 0
    start = ()
    map = []
    for line in data.splitlines():
        row = []
        for item in line:
            if item == "S":
                row.append("S")
            elif item == "^":
                row.append(1)
            else:
                row.append(0)
        map.append(row)
    map = np.array(map)

    for key, value in np.ndenumerate(map):
        if key[0] == map.shape[0] - 1:
            break
        if value == "S":
            total += move(map, key)
    return total

def problem_two(data):
    #for line in data.splitlines():
    return 0


if __name__ == "__main__":
    data01 = read_file("day07/1.txt")
    data02 = read_file("day07/example.txt")
    start_1 = timeit.default_timer()
    answer_1 = problem_one(data01)
    print(f"Part 1: {answer_1}")
    stop_1 = timeit.default_timer()
    print(f"Func took {round(stop_1 - start_1,4)*1000} milliseconds")
    start_2 = timeit.default_timer()
    answer_2 = problem_two(data02)
    print(f"Part 2: {answer_2}")
    stop_2 = timeit.default_timer()
    print(f"Func took {round(stop_2 - start_2,4)*1000} milliseconds")
