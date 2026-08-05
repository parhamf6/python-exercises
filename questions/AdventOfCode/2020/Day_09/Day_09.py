def parse_file(file_path):
    numbers = []
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            numbers.append(int(line))
    return numbers
    
puzzle_input = parse_file("Day_9.txt")
preamble = 5    # for the test case use this 
# preamble = 25 # for the puzzle input use this

def find_valid_next_number_part1():
    valid_numbers = []
    for k in range(0, preamble):
        valid_numbers.append(puzzle_input[k])
    for i in range(len(puzzle_input)-preamble):
        last_index = i+preamble
        window = puzzle_input[i:last_index]
        for j in window : 
            if puzzle_input[last_index]-j in window:
                if puzzle_input[last_index] not in valid_numbers:
                    valid_numbers.append(puzzle_input[last_index])
    for vn in puzzle_input:
        if vn not in valid_numbers:
            return vn
            
part1 = find_valid_next_number_part1()

def find_valid_next_number_part2():
    target = part1
    output = 0
    stop = False
    for left in range(len(puzzle_input)):
        if not stop:
            for right in range(left, len(puzzle_input)):
                # print(left, right)
                if sum(puzzle_input[left:right])==target:
                    window = puzzle_input[left:right]
                    window.sort()
                    output = (window[0]+window[-1])
                    stop = True
                    break
        else:
            break
    return output

part1 = find_valid_next_number_part1()
part2 = find_valid_next_number_part2()
print(part1, part2)