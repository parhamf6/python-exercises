# https://www.codewars.com/kata/5418a1dd6d8216e18a0012b2/python
def validate(n):
    r = []
    n = str(n)
    def calc_n(c):
        cc = int(c)*2
        if cc>9:
            ccs = 0
            for i in str(cc):
                ccs+=int(i)
            r.append(ccs)
        else:
            r.append(cc)
    if len(str(n))%2==0:
        for i in range(len(str(n))):
            if i%2==0:
                calc_n(n[i])
            else:
                r.append(int(n[i]))
    else:
        for i in range(len(str(n))):
            if i%2!=0:
                calc_n(n[i])
            else:
                r.append(int(n[i]))
    if sum(r)%10==0:
        return True
    else:
        return False