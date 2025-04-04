import math
n = str(input())
nlist = n.rsplit(" ")
x = int(nlist[0])
z = int(nlist[-1])
large = math.gcd(x,z)
least = math.lcm(x,z)
print(large,least)