def longest_consec(strarr, k):
    longest_length = 0
    longest_item = ""
    if k > len(strarr) or k <= 0 or strarr == []:
        return ""
    else:
        for i in range(len(strarr)):
            sliced = strarr[i:i+k]
            created = "".join(sliced)
            created_lenght = len(created)
            if created_lenght > longest_length :
                longest_length = created_lenght
                longest_item = created
    return longest_item