def cakes(recipe, available):
    possible = []
    for i in recipe:
        if i in available:
            have = available[i]
            need = recipe[i]
            count = have//need
            possible.append(count)
        else:
            return 0
    return min(possible)