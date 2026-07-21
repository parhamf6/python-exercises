import time

current_space = 0
indent_increasing = True

colors = [
    "\033[31m",  # red
    "\033[33m",  # yellow
    "\033[32m",  # green
    "\033[36m",  # cyan
    "\033[34m",  # blue
    "\033[35m",  # magenta
]

reset = "\033[0m"
color_index = 0

try:
    while True:
        max_space = 20
        min_space = 0
    
        if current_space == min_space:
            indent_increasing = True
        if current_space == max_space:
            indent_increasing = False
    
        if indent_increasing:
            current_space += 1
        else:
            current_space -= 1
    
        color = colors[color_index % len(colors)]
        color_index += 1
    
        print(f'{" " * current_space}{color}############{reset}')
        time.sleep(0.05)
except KeyboardInterrupt:
    print("\nGoodBye")