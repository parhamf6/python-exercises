# https://www.codewars.com/kata/5202ef17a402dd033c000009/python
def title_case(title, minor_words=''):
    if not title:
        return ''
    
    mw = minor_words.lower().split()
    words = title.lower().split()
    
    result = []
    for i, word in enumerate(words):
        if i == 0 or word not in mw:
            result.append(word.capitalize())
        else:
            result.append(word)
    
    return ' '.join(result)