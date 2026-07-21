# more advance version that shows time
import time

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
          " _|"],

    ".": ["   ",
          "   ",
          " . "],

    ":": ["   ",
          " . ",
          " . "],
}


def seven_segment(text):
    text = str(text)

    for row in range(3):
        line = ""
        for char in text:
            line += digits[char][row] + " "
        print(line)


def main():
    current_time = time.strftime("%H:%M:%S")
    seven_segment(current_time)
    time.sleep(1)

while True:
    try:
        main()
    except KeyboardInterrupt:
        print("\nGoodBye")
        break