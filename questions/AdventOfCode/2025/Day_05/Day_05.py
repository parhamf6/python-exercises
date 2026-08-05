def parse_file(path: str):
    ranges = []
    ids = []
    seen_blank = False

    with open(path, 'r', encoding='utf-8') as f:
        for raw in f:
            line = raw.strip()
            if line == '':
                seen_blank = True
                continue
            if not seen_blank:
                left, right = line.split('-', 1)
                a = int(left.strip())
                b = int(right.strip())
                if a > b:
                    a, b = b, a
                ranges.append((a, b))
            else:
                ids.append(int(line))

    return ranges, ids

ranges,ids = parse_file("Day_5.txt")
def find_fresh_count_v1(ranges,ids):
    fresh_count = 0
    for id in ids:
        for r in ranges:
            if r[0]<=id<=r[1]:
                fresh_count+=1
                break
    return fresh_count
def find_fresh_count_v2(ranges):
    fresh_count = 0
    ranges.sort(key=lambda r: r[0])
    merged = [ranges[0]]
    for s, e in ranges[1:]:
        last_s, last_e = merged[-1]
        if s <= last_e + 1:
            merged[-1] = (last_s, max(last_e, e))
        else:
            merged.append((s, e))
    for r in merged:
        range_memebers = (r[1]-r[0])+1
        fresh_count+=range_memebers
    return fresh_count
    
    
    
fresh_count_v1 = find_fresh_count_v1(ranges,ids)
fresh_count_v2 = find_fresh_count_v2(ranges)

print(fresh_count_v1, fresh_count_v2)