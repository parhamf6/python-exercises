# https://www.codewars.com/kata/514a024011ea4fb54200004b/python
import re 

def domain_name(url):
    return re.search(r'(?:https?://)?(?:www\.)?([^./]+)', url).group(1)
    
