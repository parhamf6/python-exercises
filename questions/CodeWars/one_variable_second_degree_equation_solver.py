# https://www.codewars.com/kata/560ae2027dc9033b5e0000c2/python
import math
def sec_deg_solver(a, b, c):
    def format_float(x):
        x = round(x, 10)
        if abs(x) < 1e-10:
            return "0.0"
        if float(x).is_integer():
            return f"{int(x)}.0"
        s = f"{x:.10f}".rstrip("0").rstrip(".")
        return s
    delta = (b**2)-4*(a*c)
    if a==0:
        if b!=0 and c!=0:
            x = -c/b
            return f"It is a first degree equation. Solution: {x}"
        elif b==0 and c==0:
            return "The equation is indeterminate"
        elif b==0 and c!=0:
            return "Impossible situation. Wrong entries"
        elif b!=0 and c==0:
            return "It is a first degree equation. Solution: 0.0"
    else:
        if delta<0:
            return ("There are no real solutions")
        elif delta==0:
            x = (-1*(b)/2*(a))
            return f"It has one double solution: {x}"
        elif delta>0:
            xm = (-1*(b)-(math.sqrt(delta)))/(2*a)
            xp = (-1*(b)+(math.sqrt(delta)))/(2*a)
            ans = [xm,xp]
            ans.sort()
            return f"Two solutions: {format_float(ans[0])}, {format_float(ans[-1])}"