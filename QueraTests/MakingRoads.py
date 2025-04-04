def max_parts(n):
    # Calculate the number of vertical and horizontal lines
    v = n // 2  # Floor division for vertical lines
    h = n - v   # Remaining lines for horizontal lines
    
    # Calculate the maximum parts
    max_parts = (v + 1) * (h + 1)
    
    return max_parts

# Example usage
n = int(input())
print(max_parts(n))