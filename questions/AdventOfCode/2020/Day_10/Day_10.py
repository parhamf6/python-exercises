def parse_file(file_path):
    jolts = []
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            jolts.append(int(line))
    return jolts
    
puzzle_input = parse_file("Day_10.txt")


def build_and_count_jolt_chain_part1():
    puzzle_input.sort()
    new = puzzle_input.copy()
    new.append(puzzle_input[-1]+3)
    current_index = 0
    count_ones = 1 # one for 0 to 1
    count_theres = 0
    for i in range(len(new)):
        current_number = new[current_index]
        if current_number+1 in new:
            count_ones+=1
            current_index = new.index(current_number+1)
        elif current_number+2 in new:
            current_index = new.index(current_number+2)
        elif current_number+3 in new:
            count_theres+=1
            current_index = new.index(current_number+3)
    return(count_ones*count_theres)


def build_and_count_jolt_chain_possible_path_part2():
    sorted_adapters = sorted(puzzle_input)
    all_jolts = [0] + sorted_adapters + [sorted_adapters[-1] + 3]
    ways_to_reach = {}
    ways_to_reach[0] = 1
    for current_jolt in all_jolts[1:]:
        total_ways = 0
        for difference in [1, 2, 3]:
            previous_jolt = current_jolt - difference
            if previous_jolt in ways_to_reach:
                total_ways += ways_to_reach[previous_jolt]
        ways_to_reach[current_jolt] = total_ways
    device_jolt = all_jolts[-1]
    return ways_to_reach[device_jolt]


part1 = build_and_count_jolt_chain_part1()
part2 = build_and_count_jolt_chain_possible_path_part2()
print(part1, part2)