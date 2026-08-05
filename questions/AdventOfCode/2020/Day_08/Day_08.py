def parse_file(file_path):
    instructions = []
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            instructions.append(line)
    return instructions
    
puzzle_input = parse_file("Day_8.txt")


def find_the_accumulator_value_part1():
    visited_indexes = []
    current_index = 0
    accumulator_value = 0
    
    while True:
        if current_index not in visited_indexes:
            visited_indexes.append(current_index)
            current_instruction = puzzle_input[current_index]
            instruction, argument = current_instruction.split()
            if instruction=="nop":
                current_index+=1
            elif instruction=="acc":
                accumulator_value+=int(argument)
                current_index+=1
            elif instruction=="jmp":
                current_index+=int(argument)
        elif current_index in visited_indexes:
            break
    return accumulator_value
    
def find_the_accumulator_value_part2():
    for change_index in range(len(puzzle_input)):
        current_instruction = puzzle_input[change_index]
        instruction, argument = current_instruction.split()

        if instruction not in ["jmp", "nop"]:
            continue
        
        modified_instructions = puzzle_input.copy()
        if instruction == "jmp":
            modified_instructions[change_index] = f"nop {argument}"
        elif instruction == "nop":
            modified_instructions[change_index] = f"jmp {argument}"
        
        visited_indexes = []
        current_index = 0
        accumulator_value = 0
        program_terminated = False
        
        while True:
            if current_index == len(modified_instructions):
                program_terminated = True
                break
            
            if current_index in visited_indexes:
                break

            visited_indexes.append(current_index)
            instruction_line = modified_instructions[current_index]
            instruction, argument = instruction_line.split()
            
            if instruction == "nop":
                current_index += 1
            elif instruction == "acc":
                accumulator_value += int(argument)
                current_index += 1
            elif instruction == "jmp":
                current_index += int(argument)
        
        if program_terminated:
            return accumulator_value
    
    return None

    
part1 = find_the_accumulator_value_part1()
part2 = find_the_accumulator_value_part2()
print(part1, part2)