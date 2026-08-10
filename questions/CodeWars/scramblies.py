def scramble(s1, s2):
    fs1 = [0] * 26
    fs2 = [0] * 26
    for i1 in s1:
        p = ord(i1)-ord('a')
        fs1[p]+=1
            
    for i2 in s2:
        p = ord(i2)-ord('a')
        fs2[p]+=1

    for c in range(26):
        if fs2[c]> fs1[c]:
            return False
    return True

print(scramble('cedewaraaossoqqyt', 'codewars'))