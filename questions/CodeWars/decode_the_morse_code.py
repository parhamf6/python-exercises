# https://www.codewars.com/kata/54b724efac3d5402db00065e/python
from preloaded import MORSE_CODE

def decode_morse(morse_code):
    morse_code = morse_code.strip()
    res = []
    words = morse_code.split("   ")
    for w in words:
        letters = w.split(" ")
        decoded_letters = [MORSE_CODE[char] for char in letters if char != ""]
        res.append("".join(decoded_letters))
    return " ".join(res)