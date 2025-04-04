def calculate_nested_sum(nested_structure):
    """
    Calculate and print the sum of all elements in a nested structure.
    """
    total_sum = 0
    for element in nested_structure:
        if isinstance(element, int):  # If the element is a number, add it to the total sum
            total_sum += element
        elif isinstance(element, list):  # If the element is a list, process it recursively
            nested_sum = calculate_nested_sum(element)
            total_sum += nested_sum
    
    print(total_sum)
    return total_sum

def process_input(input_str):
    """
    Convert input string to nested list structure and calculate its sum.
    """
    # Replace curly braces with square brackets for proper evaluation
    nested_structure = eval(input_str.replace('{', '[').replace('}', ']'))
    calculate_nested_sum(nested_structure)

input1 = str(input())
process_input(input1)
