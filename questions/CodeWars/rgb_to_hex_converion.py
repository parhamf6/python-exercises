# https://www.codewars.com/kata/513e08acc600c94f01000001/python
def rgb(r, g, b):
    tran = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    def clamp(x):
        return max(0, min(255, x))
    ans = ""
    for val in (r, g, b):
        val = clamp(val)
        val0 = val / 16
        val1 = int(val0)
        val2 = int((val0 - val1) * 16)
        ans += f"{tran[val1]}{tran[val2]}"
    return ans