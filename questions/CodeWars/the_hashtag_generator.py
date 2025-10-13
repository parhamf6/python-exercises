# https://www.codewars.com/kata/52449b062fb80683ec000024/python
def generate_hashtag(s):
    if len(s)>0:
        sl = s.split()
        cap = list(map(str.capitalize, sl))
        res = "#"+"".join(cap)
        if len(res)<=140:
            return res
        else:
            return False
    else:
        return False