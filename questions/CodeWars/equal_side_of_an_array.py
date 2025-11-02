# https://www.codewars.com/kata/5679aa472b8f57fb8c000047/python
def find_even_index(arr):
    for i in range(len(arr)):
        befarr = arr[0:i]
        aftarr = arr[i+1:]
        if sum(befarr)==sum(aftarr):
            return i
        elif i==len(arr)-1:
            return -1