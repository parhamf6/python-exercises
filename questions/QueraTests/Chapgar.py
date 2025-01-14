# چاپگر
# https://quera.org/problemset/64434
nm = str(input()).split(" ")
n, m = int(nm[0]), int(nm[1])
x_por = f"{"X"*m}"
d_por = f"{"."*m}"
line_odd = True

def odd_lines():
    for i in range(1,n+1):
        line = []
        box_odd = True
        for ii in range(1,(3*m)+1,m):
            if box_odd:
                box_odd = False
                line.append(x_por)
            elif not box_odd:
                box_odd = True
                line.append(d_por)     
        print("".join(line))
def even_lines():
    for i in range(1,n+1):
        line = []
        box_odd = True
        for ii in range(1,(3*m)+1,m):
            if box_odd:
                box_odd = False
                line.append(d_por)
            elif not box_odd:
                box_odd = True
                line.append(x_por)    
        print("".join(line))
            
for ni in range(1,(3*n)+1,n):
    if line_odd:
        line_odd = False
        odd_lines()
    elif not line_odd:
        line_odd = True
        even_lines()