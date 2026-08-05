def parse_file(file_path):
    passess = []
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            passess.append(line)
    return passess
    
puzzle_input = parse_file("Day_5.txt")

def seat_id_part1():
    highest = 0
    all_seats_id = []
    for seat in puzzle_input:
        row_related = seat[:7]
        col_related = seat[7:]
        row_down , row_up = 0 , 127
        col_left , col_right = 0 , 7
        for rr in row_related:
            middle = int((row_down + row_up)/2)
            if rr=="B":
                row_down = middle+1
            elif rr=="F":
                row_up = middle
        for cr in col_related:
            middle = int((col_left + col_right)/2)
            if cr=="R":
                col_left = middle+1
            elif cr=="L":
                col_right = middle
        seat_id = (row_down*8)+col_left
        all_seats_id.append(seat_id)
        if seat_id>highest:
            highest=seat_id
    return [highest, all_seats_id]


        
            
part1 , all_seats_id = seat_id_part1()

all_seats_id.sort()
def seat_id_part2():
    for i in range(len(all_seats_id) - 1):
        if all_seats_id[i + 1] != all_seats_id[i] + 1:
            return all_seats_id[i] + 1

part2 = seat_id_part2()

print(part1, part2)