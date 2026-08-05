def parse_file(file_path):
    groups = []
    group = []
    with open(file_path, 'r') as f:
        for line in f:
            line = line.rstrip('\n')

            if line == "":
                groups.append(" ".join(group))
                group = []
            else:
                group.append(line)
        if group:
            groups.append(" ".join(group))
    return groups


puzzle_input = parse_file("Day_6.txt")

def find_unique_values(i):
    seen = []
    for j in i:
        if j not in seen and j!=" ":
            seen.append(j)
    return seen


def yes_questions_count_part1():
    group_yes_questions_count = 0
    for i in puzzle_input:
        unique_values = find_unique_values(i)
        group_yes_questions_count+=len(unique_values)
    return group_yes_questions_count


def yes_questions_count_part2():
    group_yes_questions_count = 0
    for i in puzzle_input:
        unique_values = find_unique_values(i)
        group_memebers_count = i.split(" ")
        for j in unique_values:
            if i.count(j)==len(group_memebers_count):
                group_yes_questions_count+=1
    return group_yes_questions_count
        

part1 = yes_questions_count_part1()
part2 = yes_questions_count_part2()

print(part1,part2)