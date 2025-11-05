# https://www.codewars.com/kata/5420fc9bb5b2c7fd57000004/python
def highest_rank(arr):
    res = {
        arr[0]:arr.count(arr[0])
    }
    for i in arr[1::]:
        if i not in res:
            res[i]=arr.count(i)
    sorted_items = sorted(res.items(), key=lambda x: (x[1], x[0]), reverse=True)
    return sorted_items[0][0]