# https://www.codewars.com/kata/5a39724945ddce2223000800/python
def total_amount_visible(top_num, num_of_sides):
    r = 0
    op = (num_of_sides+1) - top_num
    for i in range(1,num_of_sides+1):
        if i!=op:
            r+=i
    return r