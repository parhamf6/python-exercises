import math
import shutil
import time

width, height = shutil.get_terminal_size()
width-=1

print('(Press Ctrl-C to quit.)')
print(f"What message do you want to display? (Max {width//2} chars")

while True:
    msg = input("> ")
    if 1<= len(msg) <= (width//2):
        break
    else:
        print(f"Message must be 1 to {width//2}, characters long.")

step = 0.0

multiplier = (width - len(msg)) / 2
while True:
    try:
        sin_of_step = math.sin(step)
        padding = ' ' * int((sin_of_step + 1) * multiplier)
        print(padding+msg)
        time.sleep(0.1)
        step += 0.25
    except KeyboardInterrupt:
        print("\nGoodBye")
        break