# https://www.codewars.com/kata/52de553ebb55d1fca3000371/python
def find_missing(sequence):
    n = len(sequence) + 1
    diff = (sequence[-1] - sequence[0]) // (n - 1)
    for i in range(len(sequence) - 1):
        current_diff = sequence[i + 1] - sequence[i]
        if current_diff != diff:
            return sequence[i] + diff