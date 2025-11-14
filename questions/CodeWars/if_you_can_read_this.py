# https://www.codewars.com/kata/586538146b56991861000293/python
from preloaded import NATO # NATO['A'] == 'Alfa', etc

def to_nato(words : str) -> str:
    res = []
    for i in words:
        if i!=" ":
            if i in [".",",","!","?"]:
                res.append(i)
            else:
                res.append(NATO[f'{i.upper()}'])
    return " ".join(res)