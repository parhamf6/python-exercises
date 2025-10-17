# https://www.codewars.com/kata/54dc6f5a224c26032800005c/python
def stock_list(s, c):
    if len(s)>0:
        res = {cat: 0 for cat in c}
        for i in s:
            if i[0] in c:
                val = i.split()
                ov = res.get(i[0])
                nv = ov + int(val[-1])
                res[i[0]]= nv
        ans = " - ".join(f"({k} : {v})" for k, v in res.items())
        return ans
    else:
        return ""