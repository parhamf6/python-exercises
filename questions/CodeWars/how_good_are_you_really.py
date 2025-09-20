# https://www.codewars.com/kata/5601409514fc93442500010b
def better_than_average(class_points, your_points):
    sum = 0
    num = len(class_points)
    for i in class_points:
        sum = sum + i
    avg = sum/num
    if float(your_points)>avg:
        return True
    else:
        return False