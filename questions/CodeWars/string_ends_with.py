# https://www.codewars.com/kata/51f2d1cafc9c0f745c00037d
def solution(text, ending):
    fi = -1 - (len(ending))
    if ((text[fi+1:]))==ending:
        return True
    else:
        return False