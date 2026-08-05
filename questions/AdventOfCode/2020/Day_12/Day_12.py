def parse_file(file_path):
    with open(file_path, 'r') as f:
        return [line.strip() for line in f]


puzzle_input = parse_file("Day_12.txt")


def find_manhattan_distance_part1():
    """Calculate Manhattan distance with ship rotation logic."""
    x, y = 0, 0
    facing_degrees = 0  # 0=E, 90=N, 180=W, 270=S
    
    direction_map = {
        0: 'E',
        90: 'N',
        180: 'W',
        270: 'S',
    }
    
    for instruction in puzzle_input:
        action = instruction[0]
        value = int(instruction[1:])
        
        if action == 'N':
            y += value
        elif action == 'S':
            y -= value
        elif action == 'E':
            x += value
        elif action == 'W':
            x -= value
        elif action == 'R':
            facing_degrees = (facing_degrees - value) % 360
        elif action == 'L':
            facing_degrees = (facing_degrees + value) % 360
        elif action == 'F':
            direction = direction_map[facing_degrees]
            if direction == 'E':
                x += value
            elif direction == 'W':
                x -= value
            elif direction == 'N':
                y += value
            elif direction == 'S':
                y -= value
    
    return abs(x) + abs(y)

def find_manhattan_distance_part2():
    """Calculate Manhattan distance with waypoint logic."""
    waypoint_x, waypoint_y = 10, 1  # Waypoint relative to ship
    ship_x, ship_y = 0, 0
    
    for instruction in puzzle_input:
        action = instruction[0]
        value = int(instruction[1:])
        
        if action == 'N':
            waypoint_y += value
        elif action == 'S':
            waypoint_y -= value
        elif action == 'E':
            waypoint_x += value
        elif action == 'W':
            waypoint_x -= value
        elif action == 'R':
            # Rotate waypoint clockwise around ship
            for _ in range(value // 90):
                waypoint_x, waypoint_y = waypoint_y, -waypoint_x
        elif action == 'L':
            # Rotate waypoint counter-clockwise around ship
            for _ in range(value // 90):
                waypoint_x, waypoint_y = -waypoint_y, waypoint_x
        elif action == 'F':
            # Move ship toward waypoint
            ship_x += waypoint_x * value
            ship_y += waypoint_y * value
    
    return abs(ship_x) + abs(ship_y)


part1 = find_manhattan_distance_part1()
part2 = find_manhattan_distance_part2()
print(part1, part2)