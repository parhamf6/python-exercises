def parse_file(file_path):
    expense = []

    with open(file_path, 'r') as f:
        for line in f:
            expense.append(int(line.strip()))
            
    return expense


puzzle_input = parse_file("Day_1.txt")
puzzle_input.sort()
target = 2020


def find_2sum(expenses , target_1):
    left_pointer = 0
    right_pointer = len(expenses)-1
    output = 0
    while left_pointer < right_pointer:
        left_number = int(expenses[left_pointer])
        right_number = int(expenses[right_pointer])
        # print(left_number, right_number)
        if left_number+right_number==target_1:
            output =  (left_number*right_number)
            return output
        elif left_number+right_number<target_1:
            left_pointer+=1
        elif left_number+right_number>target_1:
            right_pointer-=1
    return output


def find_3sum(expenses , target_2):
    for i in range(len(expenses)):
        target_1 = target_2-expenses[i]
        input_2sum = expenses[i+1:]
        output_2sum = find_2sum(input_2sum, target_1)
        if output_2sum!=0:
            return output_2sum*expenses[i]


find_v1 = find_2sum(puzzle_input, target)
find_v2 = find_3sum(puzzle_input, target)
print(find_v1, find_v2)