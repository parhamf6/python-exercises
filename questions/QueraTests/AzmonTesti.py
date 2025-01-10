# آزمون تستی
# https://quera.org/problemset/148640
n = int(input())
s = str(input())
k = int(input())
for ki in range(k):
    correct = 0
    false = 0
    skipped = 0
    for ni in range(n):
        us = str(input())
        if us.count("#")==1:
            pos = us.find("#")
            char = ""
            if pos==0:
                char="A"
            elif pos==1:
                char = "B"
            elif pos==2:
                char = "C"
            elif pos==3:
                char = "D"
            if s[ni]==char:
                correct+=1
            else:
                false+=1
        if us.count("#")==0:
            skipped+=1
        if us.count("#")>1:
            false+=1
    score = (3*correct)-false
    print(score)