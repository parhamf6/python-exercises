# https://www.codewars.com/kata/54b72c16cd7f5154e9000457/python
import re
from preloaded import MORSE_CODE
def decode_bits(bits):

    bits = bits.strip('0')

    if not bits:
        return ''
    

    sequences = re.findall(r'1+|0+', bits)
    

    time_unit = min(len(seq) for seq in sequences)
    

    morse = bits
    

    morse = re.sub('1' * (3 * time_unit) + '+', '-', morse)  # Dash
    morse = re.sub('1' * time_unit, '.', morse)              # Dot
    morse = re.sub('0' * (7 * time_unit) + '+', '   ', morse) # Word space
    morse = re.sub('0' * (3 * time_unit), ' ', morse)        # Character space
    morse = re.sub('0' * time_unit, '', morse)               # Intra-character pause
    
    return morse


def decode_morse(morse_code):

    morse_code = morse_code.strip()
    

    if not morse_code:
        return ''
    
    res = []

    words = morse_code.split("   ")
    
    for w in words:
        letters = w.split(" ")
        decoded_letters = [MORSE_CODE[char] for char in letters if char != ""]
        res.append("".join(decoded_letters))
    
    return " ".join(res)