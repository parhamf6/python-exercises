# سیکل گرفتن در برره
# https://quera.org/problemset/10166
n = int(input())
s = str(input())
keyvoon_answers = "331122"*int(n/6)+"331122"
nezam_answers = "123"*int(n/3)+"123"
shirfarhad_answers = "2123"*int(n/4)+"2123"
keyvoon_res, nezam_res, shirfarhad_res = 0, 0, 0
for i in range(n):
    answer = s[i]
    if keyvoon_answers[i]==answer:
        keyvoon_res+=1
    if nezam_answers[i]==answer:
        nezam_res+=1
    if shirfarhad_answers[i]==answer:
        shirfarhad_res+=1
scores = [keyvoon_res, nezam_res, shirfarhad_res]
scores.sort()
top = []
if keyvoon_res==scores[-1]:
    top.append("keyvoon")
if nezam_res==scores[-1]:
    top.append("nezam")
if shirfarhad_res==scores[-1]:
    top.append("shir farhad")
top.sort()

print(scores[-1])
for ii in top:
    print(ii)