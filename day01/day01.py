import timeit

def read_file(file_path):
    with open(file_path, "r") as file:
        data = file.read()
        return data

def problem_one(data):
    i = 50
    zero_count = 0
    for line in data.splitlines():
        if line[0] == "L":
            i -= int(line[1:])
            while i < 0:
                i = i + 100
            if i == 0:
                zero_count += 1
        if line[0] == "R":
            i += int(line[1:])
            while i > 99:
                i = i - 100
            if i == 0:
                zero_count += 1
    return zero_count

def problem_two(data):
    i = 50
    zero_count = 0
    for line in data.splitlines():
        direction = 1
        if line[0] == "L":
            direction = -1
        move = int(line[1:])
        new_position = i + (move * direction)
        if new_position == 0:
            zero_count += 1
            i = new_position
        elif new_position > 99:
            zero_count += (new_position // 100)
            i = new_position % 100
        elif new_position < 0 and i != 0:
            zero_count += (new_position // -100) + 1 
            i = new_position % 100
        elif new_position < 0 and i == 0:
            zero_count += (new_position // -100)
            i = new_position % 100
        else:
            i = new_position

    return zero_count


if __name__ == "__main__":
    data01 = read_file("day01/1.txt")
    data02 = read_file("day01/example.txt")
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
