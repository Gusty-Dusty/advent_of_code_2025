import timeit

def read_file(file_path):
    with open(file_path, "r") as file:
        data = file.read()
        return data

def problem_one(data):
    invalid_ids = 0
    id_ranges = []
    for line in data.splitlines():
        for group in line.split(","):
            id_range = group.split("-")
            id_ranges.append(id_range)
    for id_range in id_ranges:
        for id in range(int(id_range[0]), int(id_range[1])+1):
            id = str(id)
            id_1, id_2 = id[:len(id)//2], id[len(id)//2:]
            if id_1 == id_2:
                invalid_ids += int(id)
    return invalid_ids

def problem_two(data):
    invalid_ids = set()
    total_sum = 0
    id_ranges = []
    for line in data.splitlines():
        for group in line.split(","):
            id_range = group.split("-")
            id_ranges.append(id_range)
    for id_range in id_ranges:
        for id in range(int(id_range[0]), int(id_range[1])+1):
            id = str(id)
            for option in range(len(id)//2):
                if len(id) % (option + 1) == 0:
                    pattern = id[:option + 1]
                    if pattern * (len(id) // (option + 1)) == id:
                        invalid_ids.add(id)
    for id in invalid_ids:
        total_sum += int(id)
    return total_sum


if __name__ == "__main__":
    data01 = read_file("day02/1.txt")
    data02 = read_file("day02/example.txt")
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
