n = int(input())
k = int(input())
s = str(input())
alist = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","y","v","w","x","y","z"]
for i in range(k):
    s2 = f"{s[-1]}{s}"
    s3 = s2[:-1]
    print(s3)
    for e in s3:
        if e!="z":
            x = alist.index(e)
            re = int(x)+1
            r = alist[re]
            s3=s3.replace(e,r)
        if e=="z":
            s3=s3.replace(e,"a")

print(s3)











# k = "abc"
# n = f"{k[-1]}{k}"
# x=n[:-1]
# print(x)