digits = {
    "0": [" _ ",
          "| |",
          "|_|"],

    "1": ["   ",
          "  |",
          "  |"],

    "2": [" _ ",
          " _|",
          "|_ "],

    "3": [" _ ",
          " _|",
          " _|"],

    "4": ["   ",
          "|_|",
          "  |"],

    "5": [" _ ",
          "|_ ",
          " _|"],

    "6": [" _ ",
          "|_ ",
          "|_|"],

    "7": [" _ ",
          "  |",
          "  |"],

    "8": [" _ ",
          "|_|",
          "|_|"],

    "9": [" _ ",
          "|_|",
          " _|"]
}


def seven_segment(number):
    number = str(number)

    for row in range(3):
        line = ""
        for digit in number:
            line += digits[digit][row] + " "
        print(line)


num = int(input())
seven_segment(num)
