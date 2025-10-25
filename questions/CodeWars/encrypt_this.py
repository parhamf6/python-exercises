# https://www.codewars.com/kata/5848565e273af816fb000449/python
def encrypt_this(text):
    if not text:
        return ""

    result = []
    for word in text.split():
        if len(word) == 1:
            result.append(str(ord(word[0])))
        elif len(word) == 2:
            result.append(str(ord(word[0])) + word[1])
        else:
            encrypted = str(ord(word[0])) + word[-1] + word[2:-1] + word[1]
            result.append(encrypted)

    return " ".join(result)