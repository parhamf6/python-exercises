# https://www.codewars.com/kata/51e000d070fe4414000003f0/python
def solution(hour):
    hour = str(hour)
    if len(hour)>4 or len(hour)<3 :
        raise Exception("Function should raise an exception")
    else:
        min = hour[-2:]
        if len(hour)==3:
            h = hour[0]
            return f"{h}:{min}"
        else:
            h = hour[0:2]
            return f"{h}:{min}"