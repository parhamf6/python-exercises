# https://www.codewars.com/kata/57814d79a56c88e3e0000786/python
def decrypt(encrypted_text, n):
    if encrypted_text is None or encrypted_text == "" or n <= 0:
        return encrypted_text
    else:
        st = [encrypted_text]
        half = len(st[-1])//2
        for i in range(n):
            odd_half = st[-1][:half]
            even_half = st[-1][half:]
            rebuild = []
            for r in range(len(st[-1])):
                if r%2==0:
                    rebuild.append(even_half[r//2])
                else:
                    rebuild.append(odd_half[r//2])
            st.append("".join(rebuild))
        return st[-1]


def encrypt(text, n):
    if text is None or text == "" or n <= 0:
        return text
    else:
        st = [text]
        for i in range(n):
            odd = []
            even = []
            for e in range(len(st[-1])):
                if e%2==0:
                    even.append(st[-1][e])
                else:
                    odd.append(st[-1][e])
            st.append("".join(odd+even))
        return st[-1]