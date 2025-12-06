import math
import timeit

def read_file(file_path):
    with open(file_path, "r") as file:
        data = file.read()
        return data

def problem_one(data):
    problems = []
    total = 0
    for line in data.splitlines():
        problem = line.split(" ")
        cleaned = []
        for item in problem:
            if item != "":
                try:
                    cleaned.append(int(item))
                except:
                    cleaned.append(item)
        problems.append(cleaned)
    for x in range(len(problems[0])):
        problem_total = 0
        match problems[-1][x]:
            case "*":
                problem_set = []
                for item in range(len(problems) - 1):
                    problem_set.append(problems[item][x])
                problem_total = math.prod(problem_set)
            case "+":
                problem_total = 0
                for item in range(len(problems) - 1):
                    problem_total += problems[item][x]
        total += problem_total
    return total

def problem_two(data):
    cleaned = []
    problems = []
    problem_sets = []
    problem_symbol = []
    total = 0
    for line in data.splitlines():
        problems.append(list(line))
    for x in range(len(problems[0])):
        problem = []
        if problems[-1][x] != ' ':
            problem_symbol.append(problems[-1][x])
        for i in range(len(problems[:-1])):
            problem.append(problems[i][x])
        cleaned.append(problem)
    current_spot = 0
    current_set = []
    for item in cleaned:
        if all(x == ' ' for x in item):
            current_set.append(problem_symbol[current_spot])
            problem_sets.append(current_set)
            current_set = []
            current_spot += 1
        else:
            current_set.append(int("".join(item)))
    current_set.append(problem_symbol[current_spot])
    problem_sets.append(current_set)
    for x in range(len(problem_sets)):
        problem_total = 0
        match problem_sets[x][-1]:
            case "*":
                problem_set = []
                for item in range(len(problem_sets[x]) - 1):
                    problem_set.append(problem_sets[x][item])
                problem_total = math.prod(problem_set)
            case "+":
                problem_total = 0
                for item in range(len(problem_sets[x]) - 1):
                    problem_total += problem_sets[x][item]
        total += problem_total
    return total



if __name__ == "__main__":
    data01 = read_file("day06/1.txt")
    data02 = read_file("day06/example.txt")
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
