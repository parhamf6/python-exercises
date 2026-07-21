
while True:
    response = (input("Enter the starting number (e.g. 0) > "))
    if response=="":
        response = "0"
        break
    if response.isdecimal():
        break
    print("Pkeaser enter a number greater or equal to 0.")
starting_number = int(response)

while True:
    response = (input("Enter how many numbers to display (e.g. 1000) > "))
    if response=="":
        response = "1000"
        break
    if response.isdecimal():
        break
    print("Pkeaser enter a number.")
numbers_range = int(response)

for i in range(starting_number, starting_number+numbers_range):
    dec = i
    hex_val = hex(i)[2:].upper()
    bin_val = bin(i)[2:]
    print(f"DEC: {dec}  HEX: {hex_val}  BIN: {bin_val}")