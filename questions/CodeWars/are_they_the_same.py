# https://www.codewars.com/kata/550498447451fbbd7600041c/python
def comp(array1, array2):
    if array2 is not None and array1 is not None:
        for i in array1:
            if i**2 in array2:
                array2.remove(i**2)
        if len(array2)==0:
            return True
        else:
            return False
    else:
        return False