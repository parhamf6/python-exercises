def count_smileys(arr):
    r = 0
    for i in arr:
        if len(i)<3:
            if i[0] in [";",":"]:
                if i[-1] in [")" , "D"]:
                    r+=1
        else:
            if i[0] in [";",":"]:
                if i[1] in ["-","~"]:
                    if i[-1] in [")" , "D"]:
                        r+=1
    return r