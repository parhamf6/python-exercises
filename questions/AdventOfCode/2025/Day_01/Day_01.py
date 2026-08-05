

def parse_file(file_path):
    """
    Parses a text file with lines like 'L68', 'R30' and returns a list of tuples.
    Each tuple is (direction, value), e.g., ('L', 68)
    """
    instructions = []

    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()  # Remove trailing newline and spaces
            if not line:
                continue  # Skip empty lines
            direction = line[0]  # 'L' or 'R'
            try:
                value = int(line[1:])  # Convert the rest to integer
            except ValueError:
                print(f"Warning: could not parse line: {line}")
                continue
            instructions.append((direction, value))
    
    return instructions
    

file_path = "Day_1.txt"
instructions = parse_file(file_path)
start = [50, 0]
count_zero_v1 = 0
count_zero_v2 =0
    
def calculate_rotation(rotation , data):
    start = data[0]
    rotation_pass = 0
    old = start
    if rotation[0]== 'L':
        start -= rotation[1]
        rotation_pass = (old - 1) // 100 - ((old - rotation[1]) // 100)
    elif rotation[0]== 'R':
        start += rotation[1]
        rotation_pass = (old + rotation[1] - 1) // 100 - old // 100
    start = start % 100
    
    # print(start)
    return [start , rotation_pass]
    

for i in range(len(instructions)):
    
    start  = calculate_rotation(instructions[i], start)
    if start[0]==0:
        count_zero_v1+=1
    count_zero_v2+=start[1]
print(count_zero_v1 , count_zero_v1+count_zero_v2)