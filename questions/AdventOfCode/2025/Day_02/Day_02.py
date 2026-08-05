def parse_file(file_path):
    with open(file_path, 'r') as f:
        content = f.read()

    id_ranges = [item.strip() for item in content.split(",") if item.strip()]

    return id_ranges
id_ranges = parse_file("Day_2.txt")


def find_invalid_id_v1(start_range, end_range):
    invalid_id = []
    for id in range(start_range, end_range+1):
        if id<100 and id>10:
            x =  str(id)
            if x[0] == x[1]:
                invalid_id.append(id)
        elif id>100:
            x = str(id)
            half_x = x[:int((len(x)+1)/2)]
            # print(x, half_x)
            if x.count(half_x)>1:
                invalid_id.append(id)
    return invalid_id
    

def find_invalid_id_v2(start_range, end_range):
    invalid_id = []
    for id in range(start_range, end_range+1):
        if id<100 and id>10:
            x =  str(id)
            if x[0] == x[1]:
                invalid_id.append(id)
        elif id>100:
            x = str(id)
            for k in range(1, len(x)//2 + 1):
                if len(x) % k != 0:
                    continue
                part = x[:k]
                if part * (len(x) // k) == x:
                    invalid_id.append(id)
                    break
    return invalid_id
    

invalid_sum_v1 = 0
invalid_sum_v2 = 0


for r in id_ranges:
    sub_range = r.split("-")
    start = int(sub_range[0])
    end = int(sub_range[1])
    values_v1 = find_invalid_id_v1(start, end)
    values_v2 = find_invalid_id_v2(start, end)
    for invalid_v1 in values_v1:
        invalid_sum_v1+=invalid_v1
    for invalid_v2 in values_v2:
        invalid_sum_v2+=invalid_v2
        

print(invalid_sum_v1, invalid_sum_v2)