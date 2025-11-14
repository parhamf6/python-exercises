# https://www.codewars.com/kata/58223370aef9fc03fd000071/python
def dashatize(n):
    ns = str(abs(n))
    if len(ns)==1:
        return ns
    else:
        res = []
        for i in range(len(ns)):
            if i==0 and int(ns[i])%2==1:
                res.append(f"{ns[i]}-")
            elif i==0:
                res.append(ns[i])
            elif i==len(ns)-1 and int(ns[i])%2==1:
                if res[-1][-1]=="-":
                    res.append(f"{ns[i]}")
                else:
                    res.append(f"-{ns[i]}")
            elif int(ns[i])%2==1:
                if res[-1][-1]=="-":
                    res.append(f"{ns[i]}-")
                else:
                    res.append(f"-{ns[i]}-")
            else:
                res.append(ns[i])
        return "".join(res)