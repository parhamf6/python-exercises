def parse_file(file_path):
    tree_map = []
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            tree_map.append(line)
    return tree_map

puzzle_input = parse_file("Day_3.txt")

def count_trees_on_slope(right, down):
    trees_encountered = 0
    x_position = 0
    map_width = len(puzzle_input[0])
    
    for row in range(0, len(puzzle_input), down):
        current_spot = puzzle_input[row][x_position % map_width]
        if current_spot == '#':
            trees_encountered += 1
        x_position += right
    
    return trees_encountered

def check_all_slopes():
    slope_right_3_down_1 = count_trees_on_slope(3, 1)
    slope_right_1_down_1 = count_trees_on_slope(1, 1)
    slope_right_5_down_1 = count_trees_on_slope(5, 1)
    slope_right_7_down_1 = count_trees_on_slope(7, 1)
    slope_right_1_down_2 = count_trees_on_slope(1, 2)
    
    product = slope_right_3_down_1 * slope_right_1_down_1 * slope_right_5_down_1 * slope_right_7_down_1 * slope_right_1_down_2
    
    return slope_right_3_down_1, product

part1, part2 = check_all_slopes()
print(part1, part2)