# https://www.codewars.com/kata/51fc12de24a9d8cb0e000001
def valid_ISBN10(isbn): 
    if len(isbn)==10:
        c = isbn[0:8]
        check_digit = c.isdigit()
        if check_digit:
            if isbn[9].isdigit() or isbn[9]=="X":
                x = 0
                for z in range(0,10):
                    if isbn[z]=="X":
                        x = x + 100
                    else:
                        i = isbn[z]
                        x = x + ((int(i))*(z+1))
                if x%11==0:
                    return(True) 
                else:
                    return(False)
            else:
                return(False)
        else:
            return(False)
    else:
        return(False)