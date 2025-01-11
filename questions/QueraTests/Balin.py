# بالین
# https://quera.org/problemset/175884
def calculate_floor(string):
    current_floor = 0
    for i in string:
        if i=="U":
            current_floor+=1
        else:
            current_floor-=1
    return current_floor