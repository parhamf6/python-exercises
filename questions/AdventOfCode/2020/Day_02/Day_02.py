def parse_file(file_path):
    database = []

    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            x = line.split(":")
            password_policy = x[0]
            password = x[1]
            data_line = [password_policy.split(" "), password.strip() ]
            database.append(data_line)
            
    return database


puzzle_input = parse_file("Day_2.txt")

def check_password_v1():
    count = 0
    for i in range(len(puzzle_input)):
        policy_n = puzzle_input[i][0][0].split("-")
        policy_char = puzzle_input[i][0][1]
        password = puzzle_input[i][1]
        char_in_password = password.count(policy_char)
        if char_in_password<=int(policy_n[1]) and char_in_password>=int(policy_n[0]):
            count+=1
    return count
    

def check_password_v2():
    count = 0
    for i in range(len(puzzle_input)):
        policy_n = puzzle_input[i][0][0].split("-")
        policy_char = puzzle_input[i][0][1]
        password = puzzle_input[i][1]
        if password[int(policy_n[0])-1]==policy_char and password[int(policy_n[1])-1]!=policy_char:
            count+=1
        elif password[int(policy_n[0])-1]!=policy_char and password[int(policy_n[1])-1]==policy_char:
            count+=1
    return count
    

v1 = check_password_v1()
v2 = check_password_v2()
print(v1, v2)