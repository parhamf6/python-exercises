# https://www.codewars.com/kata/59727ff285281a44e3000011/python
def band_name_generator(name):
    if name[0] == name[-1]:
        return name.capitalize() + name[1:]
    else:
        return f"The {name.capitalize()}"