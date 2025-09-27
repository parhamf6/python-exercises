# https://www.codewars.com/kata/555086d53eac039a2a000083
def lovefunc( flower1, flower2 ):
    if flower1%2==0:
        if flower2%2!=0:
            return True
        else:
            return False
    if flower1%2!=2:
        if flower2%2==0:
            return True
        else:
            return False