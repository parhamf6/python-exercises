# https://www.codewars.com/kata/581e014b55f2c52bb00000f8/python
def decipher_this(text):
    if not text:
        return ""

    result = []
    for word in text.split():
        num = ""
        for ch in word:
            if ch.isdigit():
                num += ch
            else:
                break
        rest = word[len(num):]
        first_letter = chr(int(num))

        if len(rest) == 0:
            decoded = first_letter
        elif len(rest) == 1:
            decoded = first_letter + rest
        else:
            rest = list(rest)
            rest[0], rest[-1] = rest[-1], rest[0]
            decoded = first_letter + "".join(rest)

        result.append(decoded)

    return " ".join(result)