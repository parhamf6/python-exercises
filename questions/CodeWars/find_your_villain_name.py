# https://www.codewars.com/kata/536c00e21da4dc0a0700128b/python
def get_villain_name(birthdate): 
    first = [ "The Evil","The Vile","The Cruel", "The Trashy","The Despicable", "The Embarrassing", "The Disreputable","The Atrocious", "The Twirling",  "The Orange","The Terrifying", "The Awkward"]
    last = ["Mustache", "Pickle", "Hood Ornament", "Raisin", "Recycling Bin", "Potato", "Tomato", "House Cat", "Teaspoon", "Laundry Basket"]
    month = birthdate.month
    day = str(birthdate.day)
    return (f"{first[month-1]} {last[int(day[-1])]}")