import itertools
import timeit

def read_file(file_path):
    with open(file_path, "r") as file:
        data = file.read()
        return data

def problem_one(data):
    voltage = 0
    for line in data.splitlines():
        first_digit = 0
        first_place = 0
        second_digit = 0
        for i in range(len(str(line))):
            if int(line[i]) > first_digit and i < (len(str(line)) - 1):
                first_digit = int(line[i])
                first_place = i
        for i in range(len(str(line))):
            if int(line[i]) > second_digit and i > first_place:
                second_digit = int(line[i])
        voltage += int(str(first_digit) + str(second_digit))
    return voltage

def problem_two(data):
    voltage = 0
    for line in data.splitlines():
        volts = ""
        last_spot = 0
        for i in range(12):
            current_digit = 0
            current_spot = i
            for x in range(len(str(line))):
                current_spot = x
                if int(line[x]) > current_digit and x <= (len(str(line)) - 12 + i) and x >= last_spot:
                    current_digit = int(line[x])
                    last_spot = current_spot + 1
            volts += str(current_digit)
        voltage += int(volts)
    return voltage


if __name__ == "__main__":
    data01 = read_file("day03/1.txt")
    data02 = read_file("day03/example.txt")
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
