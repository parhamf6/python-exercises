def parse_file(path: str):
    # Just read all lines as they are, keeping spaces
    lines = []
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.rstrip('\n')  # only remove newline, keep spaces
            lines.append(line)
    return lines

math_worksheet = parse_file("Day_6.txt")

def solve_math_homework_v1():
    # First, process the data for part 1
    processed_data = []
    ope = ["+", "*"]
    
    for line in math_worksheet:
        items = []
        line_parts = line.split(" ")
        for part in line_parts:
            if part.isnumeric() or part in ope:
                items.append(part)
        processed_data.append(items)
    
    # Now solve it
    items_len = len(processed_data[0])
    worksheet_len = len(processed_data)
    
    sum = 0
    for i in range(items_len):
        operation = processed_data[-1][i]
        sum_items = 0
        multiplication_items = 1
        
        for ii in range(worksheet_len - 1):
            if operation == "+":
                sum_items += int(processed_data[ii][i])
            else:
                multiplication_items = multiplication_items * int(processed_data[ii][i])
        
        if operation == "+":
            sum += sum_items
        else:
            sum += multiplication_items
    
    return sum
    


def solve_math_homework_v2():
    
    rows = len(math_worksheet)
    max_len = len(math_worksheet[0])

    matrix = []
    for r in range(rows):
        row_chars = []
        line = math_worksheet[r]
        # append characters and pad with spaces to max_len
        for c in range(max_len):
            if c < len(line):
                row_chars.append(line[c])
            else:
                row_chars.append(" ")
        matrix.append(row_chars)

    separator_cols = []
    for c in range(max_len):
        all_space = True
        for r in range(rows):
            if matrix[r][c] != " ":
                all_space = False
                break
        if all_space:
            separator_cols.append(c)

    groups = []
    c = 0
    while c < max_len:
        if c in separator_cols:
            c += 1
            continue

        start = c

        while c < max_len and c not in separator_cols:
            c += 1
        end = c

        
        group_cols = []
        col_idx = start
        while col_idx < end:
            group_cols.append(col_idx)
            col_idx += 1

        groups.append(group_cols)

    
    grand_total = 0
    for group in groups:
        
        leftmost_col = group[0]
        operator = matrix[rows - 1][leftmost_col]

        
        numbers = []
        
        g_index = len(group) - 1
        while g_index >= 0:
            col = group[g_index]

            
            digit_chars = ""
            r = 0
            while r < rows - 1:  # exclude last row (operators)
                digit_chars += matrix[r][col]
                r += 1

            i = 0
            while i < len(digit_chars) and digit_chars[i] == " ":
                i += 1
            trimmed = digit_chars[i:]

            if trimmed == "":
                value = 0
            else:
                value = int(trimmed)

            numbers.append(value)
            g_index -= 1

        if operator == "+":
            total_for_problem = 0
            idx = 0
            while idx < len(numbers):
                total_for_problem += numbers[idx]
                idx += 1
        else:
            total_for_problem = 1
            idx = 0
            while idx < len(numbers):
                total_for_problem *= numbers[idx]
                idx += 1
        
        grand_total += total_for_problem

    return grand_total


math_homework_v1 = solve_math_homework_v1()
math_homework_v2 = solve_math_homework_v2()

print(math_homework_v1 , math_homework_v2)