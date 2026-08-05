def parse_file(file_path):
    seat_layout = []
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            seat_layout.append(list(line))
    return seat_layout

puzzle_input = parse_file("Day_11.txt")


def new_layout_func(current_layout):
    new_layout = []
    for row in current_layout:
        new_layout.append(row[:])
    return new_layout
    
    
def find_the_seat_part1(seat_layout):
    neighbor_directions = [
        (-1, -1), (-1, 0), (-1, 1),  # top-left, top, top-right
        (0, -1),           (0, 1),    # left, right
        (1, -1),  (1, 0),  (1, 1)     # bottom-left, bottom, bottom-right
    ]
    current_layout = seat_layout
    total_rows = len(seat_layout)
    total_cols = len(seat_layout[0])
    
    while True:
        new_layout = new_layout_func(current_layout)
        layout_changed = False
        
        for row in range(total_rows):
            for col in range(total_cols):
                current_position = current_layout[row][col]
                
                if current_position == '.':
                    continue
                
                occupied_neighbors = 0
                for direction_row, direction_col in neighbor_directions:
                    neighbor_row = row + direction_row
                    neighbor_col = col + direction_col
                    
                    if 0 <= neighbor_row < total_rows and 0 <= neighbor_col < total_cols:
                        if current_layout[neighbor_row][neighbor_col] == '#':
                            occupied_neighbors += 1
                
                if current_position == 'L' and occupied_neighbors == 0:
                    new_layout[row][col] = '#'
                    layout_changed = True
                
                elif current_position == '#' and occupied_neighbors >= 4:
                    new_layout[row][col] = 'L'
                    layout_changed = True
        
        if not layout_changed:
            break
        
        current_layout = new_layout
    
    occupied_count = 0
    for row in current_layout:
        for seat in row:
            if seat == '#':
                occupied_count += 1
                
    return occupied_count


def find_the_seat_part2(seat_layout):
    sight_directions = [
        (-1, -1), (-1, 0), (-1, 1),  # top-left, top, top-right
        (0, -1),           (0, 1),    # left, right
        (1, -1),  (1, 0),  (1, 1)     # bottom-left, bottom, bottom-right
    ]
    current_layout = seat_layout
    total_rows = len(seat_layout)
    total_cols = len(seat_layout[0])
    
    while True:
        new_layout = new_layout_func(current_layout)
        layout_changed = False
        
        for row in range(total_rows):
            for col in range(total_cols):
                current_position = current_layout[row][col]
                
                if current_position == '.':
                    continue

                visible_occupied_seats = 0
                
                for direction_row, direction_col in sight_directions:

                    steps = 1
                    while True:
                        look_row = row + (direction_row * steps)
                        look_col = col + (direction_col * steps)
                        
                        if not (0 <= look_row < total_rows and 0 <= look_col < total_cols):
                            break
                        
                        position_in_sight = current_layout[look_row][look_col]
                        
                        if position_in_sight == '#':
                            visible_occupied_seats += 1
                            break
                        
                        elif position_in_sight == 'L':
                            break
                        
                        steps += 1
                
                if current_position == 'L' and visible_occupied_seats == 0:
                    new_layout[row][col] = '#'
                    layout_changed = True
                
                elif current_position == '#' and visible_occupied_seats >= 5:
                    new_layout[row][col] = 'L'
                    layout_changed = True
        
        if not layout_changed:
            break
        
        current_layout = new_layout
    
    occupied_count = 0
    for row in current_layout:
        for seat in row:
            if seat == '#':
                occupied_count += 1
                
    return occupied_count


part1 = find_the_seat_part1(puzzle_input)
part2 = find_the_seat_part2(puzzle_input)
print(part1, part2)