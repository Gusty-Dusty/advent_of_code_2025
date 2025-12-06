import timeit

def read_file(file_path):
    with open(file_path, "r") as file:
        data = file.read()
        return data
    
def check_ingredient(groups, item):
    for group in groups:
        if item >= group[0] and item <= group[1]:
            return 1
    return 0

def problem_one(data):
    groups = []
    available = 0
    total = 0
    for line in data.splitlines():
        if line == "":
            available = 1
            continue
        if available == 1:
            total += check_ingredient(groups, int(line))

        if available == 0:
            item = [int(line.split("-")[0]), int(line.split("-")[1])]
            groups.append(item)

    return total

def problem_two(data):
    groups = []
    total = 0
    for line in data.splitlines():
        if line == "":
            break
        else:
            item = [int(line.split("-")[0]), int(line.split("-")[1])]
            groups.append(item)
    prev_group_end = 0
    for group in sorted(groups):
        if group[0] > prev_group_end:
            total += group[1] - group[0] + 1
        elif group[1] > prev_group_end:
            total += group[1] - prev_group_end
        prev_group_end = max(prev_group_end, group[1])

    return total


if __name__ == "__main__":
    data01 = read_file("day05/1.txt")
    data02 = read_file("day05/example.txt")
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
