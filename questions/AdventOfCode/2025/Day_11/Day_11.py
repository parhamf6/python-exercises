def count_paths_part1(filename):
    """
    Count all paths from 'you' to 'out'
    """
    # Parse the input file into a graph
    graph = {}
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(': ')
            device = parts[0]
            outputs = parts[1].split() if len(parts) > 1 else []
            graph[device] = outputs
    
    def dfs(current, visited_in_path):
        # Base case: reached the destination
        if current == 'out':
            return 1
        
        # Dead end: no outgoing connections
        if current not in graph:
            return 0
        
        total_paths = 0
        for neighbor in graph[current]:
            # Avoid cycles in the current path
            if neighbor not in visited_in_path:
                visited_in_path.add(neighbor)
                total_paths += dfs(neighbor, visited_in_path)
                visited_in_path.remove(neighbor)
        
        return total_paths
    
    # Start DFS from 'you'
    visited = {'you'}
    result = dfs('you', visited)
    return result


def count_paths_part2(filename):
    """
    Count all paths from 'svr' to 'out' that visit BOTH 'dac' and 'fft'
    Assumes the graph is a DAG (no cycles)
    """
    # Parse the input file into a graph
    graph = {}
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(': ')
            device = parts[0]
            outputs = parts[1].split() if len(parts) > 1 else []
            graph[device] = outputs
    
    # Memoization: cache[(node, has_dac, has_fft)] = number of paths
    cache = {}
    
    def dfs(current, visited_dac, visited_fft):
        # Update flags
        if current == 'dac':
            visited_dac = True
        if current == 'fft':
            visited_fft = True
        
        # Base case
        if current == 'out':
            return 1 if (visited_dac and visited_fft) else 0
        
        # Check cache
        cache_key = (current, visited_dac, visited_fft)
        if cache_key in cache:
            return cache[cache_key]
        
        # Dead end
        if current not in graph:
            cache[cache_key] = 0
            return 0
        
        # Explore all neighbors
        total_paths = 0
        for neighbor in graph[current]:
            total_paths += dfs(neighbor, visited_dac, visited_fft)
        
        cache[cache_key] = total_paths
        return total_paths
    
    result = dfs('svr', False, False)
    return result


# Usage:
if __name__ == "__main__":
    # Part 1
    result1 = count_paths_part1('day_11.txt')
    print(f"Part 1: {result1} paths from 'you' to 'out'")
    
    # Part 2
    result2 = count_paths_part2('day_11.txt')
    print(f"Part 2: {result2} paths from 'svr' to 'out' that visit both 'dac' and 'fft'")