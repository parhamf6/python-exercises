from itertools import combinations
from functools import reduce
import operator


def parse_boxes(file_path):
    boxes = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for raw in f:
            line = raw.strip()
            if not line:
                continue
            x, y, z = line.split(",")
            boxes.append((int(x), int(y), int(z)))
    return boxes


def compute_all_pairs_sorted_by_squared_distance(coord_list):
    pairs = []
    n = len(coord_list)
    for i, j in combinations(range(n), 2):
        x0, y0, z0 = coord_list[i]
        x1, y1, z1 = coord_list[j]
        d2 = (x0 - x1)**2 + (y0 - y1)**2 + (z0 - z1)**2
        pairs.append((d2, i, j))
    pairs.sort(key=lambda t: t[0])
    return pairs


def find_root(parent_list, node):
    while parent_list[node] != node:
        parent_list[node] = parent_list[parent_list[node]]
        node = parent_list[node]
    return node


def union_nodes(parent_list, size_list, node_a, node_b):
    root_a = find_root(parent_list, node_a)
    root_b = find_root(parent_list, node_b)
    if root_a == root_b:
        return False
    # attach smaller to larger
    if size_list[root_a] < size_list[root_b]:
        root_a, root_b = root_b, root_a
    parent_list[root_b] = root_a
    size_list[root_a] += size_list[root_b]
    return True


def compute_circuit_sizes(parent_list):
    root_counts = {}
    for node in range(len(parent_list)):
        r = find_root(parent_list, node)
        root_counts[r] = root_counts.get(r, 0) + 1
    return sorted(root_counts.values(), reverse=True)


def process_first_k_connection_attempts_return_top3_product(coord_list, pairs_sorted, k_attempts):
    n = len(coord_list)
    parent = list(range(n))
    size = [1] * n

    attempts = 0
    max_attempts = min(k_attempts, len(pairs_sorted))  # safe guard
    pair_index = 0

    while attempts < max_attempts and pair_index < len(pairs_sorted):
        _, i, j = pairs_sorted[pair_index]
        union_nodes(parent, size, i, j)
        attempts += 1
        pair_index += 1

    sizes = compute_circuit_sizes(parent)
    top3 = sizes[:3] + [1] * max(0, 3 - len(sizes))
    product_top3 = reduce(operator.mul, top3, 1)
    return top3, product_top3


def process_until_all_connected_return_last_merged_pair(coord_list, pairs_sorted):
    n = len(coord_list)
    if n <= 1:
        return None, None

    parent = list(range(n))
    size = [1] * n
    components_remaining = n
    last_merged_pair = (None, None)

    for _, i, j in pairs_sorted:
        merged = union_nodes(parent, size, i, j)
        if merged:
            last_merged_pair = (i, j)
            components_remaining -= 1
            if components_remaining == 1:
                break

    return last_merged_pair


box_coordinates = parse_boxes("Day_8.txt")
sorted_pairs = compute_all_pairs_sorted_by_squared_distance(box_coordinates)


ATTEMPTS_PART1 = 1000
top3_sizes_part1, product_top3_part1 = process_first_k_connection_attempts_return_top3_product(
     box_coordinates, sorted_pairs, ATTEMPTS_PART1
)


last_i, last_j = process_until_all_connected_return_last_merged_pair(box_coordinates, sorted_pairs)
product_x_coords = box_coordinates[last_i][0] * box_coordinates[last_j][0]


print(product_top3_part1)
print(product_x_coords)