s1 = str(input())
s2 = str(input())
s1list = s1.rsplit(" ")
s2list = s2.rsplit(" ")
read = 0
eye = 0
while (read<len(s1list)):
    if int(s1list[read])==int(s2list[read])==1:
            eye = eye +1
    read = read +1
print(eye)