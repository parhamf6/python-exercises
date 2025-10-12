# https://www.codewars.com/kata/5e16ffb7297fe00001114824/python
def top3(products, amounts, prices):
    revenue_list = [(amounts[i] * prices[i], i, products[i]) for i in range(len(products))]
    revenue_list.sort(key=lambda x: (-x[0], x[1]))
    return [item[2] for item in revenue_list[:3]]