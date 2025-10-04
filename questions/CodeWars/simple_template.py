# https://www.codewars.com/kata/56ae72854d005c7447000023/python
import re
def create_template(template):
    pattern = re.compile(r"\{\{(.*?)\}\}")
    def filler(**kwargs):
        return pattern.sub(lambda match: str(kwargs.get(match.group(1), "")), template)
    return filler