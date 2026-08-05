def parse_file(file_path):
    bank = []
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            bank.append(line)
    return bank
    

bank = parse_file("Day_3.txt")


def find_largest_joltage_v1(batteries):
    largest = 0
    for i in range(len(batteries)):
        sliced_batteries = batteries[:i]
        for sb in sliced_batteries:
            if int(sb+batteries[i])>largest:
                largest = int(sb+batteries[i])
    return largest


def find_largest_joltage_v2(batteries):
    k = 12
    n = len(batteries)
    if n <= k:
        return int(batteries)
    rem = n - k
    stack = []
    for ch in batteries:
        while stack and rem > 0 and stack[-1] < ch:
            stack.pop()
            rem -= 1
        stack.append(ch)
    if rem > 0:
        stack = stack[:-rem]
    result_str = ''.join(stack[:k])
    return int(result_str)


joltage_sum_v1 = 0
joltage_sum_v2 = 0


for b in bank:
    joltage_sum_v1+=(find_largest_joltage_v1(b))
    joltage_sum_v2+=(find_largest_joltage_v2(b))
    

print(joltage_sum_v1 , joltage_sum_v2)
    