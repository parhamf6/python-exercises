def parse_file(file_path):
    rules = []
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            rules.append(line)
    return rules


puzzle_input = parse_file("Day_7.txt")
our_bag = "shiny gold"


def find_bags_path_part1():
    bags = [our_bag]
    changed = True
    while changed:
        changed = False
        for rule in puzzle_input:
            parent = " ".join(rule.split(" ")[:2])
            for bag in bags:
                if bag in rule and parent not in bags:
                    bags.append(parent)
                    changed = True
    return len(bags) - 1
    

def parse_rules_to_dict(rules):
    contains = {}
    for rule in rules:
        if not rule:
            continue
        parts = rule.split(" contain ")
        parent_raw = parts[0].strip()
        parent = " ".join(parent_raw.split()[:2])
        contains[parent] = []
        contents_raw = parts[1].strip().rstrip(".")
        if contents_raw == "no other bags":
            continue
        items = contents_raw.split(", ")
        for item in items:
            item = item.strip()
            words = item.split()
            count = int(words[0])
            child_color = words[1] + " " + words[2]
            contains[parent].append((child_color, count))
    return contains


def count_total_bags_inside(bag_color, contains, memo):
    if bag_color in memo:
        return memo[bag_color]
    total = 0
    children = contains.get(bag_color, [])
    for child_color, count in children:
        inner_count = count_total_bags_inside(child_color, contains, memo)
        total += count * (1 + inner_count)
    memo[bag_color] = total
    return total


def find_bags_path_part2():
    rules_dict = parse_rules_to_dict(puzzle_input)
    memo = {}
    return count_total_bags_inside(our_bag, rules_dict, memo)


part1 = find_bags_path_part1()
part2 = find_bags_path_part2()
print(part1, part2)