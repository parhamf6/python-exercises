import random
import time
start = 1
total_time = 0
all_quastions = []
while start!=0:
    number_of_quastions = int(input("Please input How many quastions you want to answer : "))
    chose_range = input("Please input The range of numbers : format(n-n) start from 1  : ")
    chose_operation = input("Please chose the type of quastion : + OR - OR * OR ** OR / : ")
    chose_range_list = chose_range.rsplit("-")
    open_range = int(chose_range_list[0])
    close_range = int(chose_range_list[1])

    correct_answers = 0
    timer_start1 = 0
    timer_end1 = 0
    q_t_s = 0
    q_t_e = 0

    def timer_start():
        global timer_start1
        timer_start1 = time.time()
        return timer_start1
    def timer_end():
        global timer_end1
        timer_end1 = time.time()
        return timer_end1
    def q_time_s():
        global q_t_s
        q_t_s = time.time()
        return q_t_s
    def q_time_e():
        global q_t_e
        q_t_e = time.time()
        return q_t_e
    for i in range(number_of_quastions):
        if i==0:
            timer_start()
        firste_number = random.randint(open_range, close_range)
        second_number = random.randint(open_range, close_range)
        if chose_operation=="*":
                quastion = firste_number * second_number
                x = (f"{firste_number}*{second_number}")
        elif chose_operation=="**":
                quastion = firste_number ** second_number
                x = (f"{firste_number}**{second_number}")
        elif chose_operation=="+":
                quastion = firste_number + second_number
                x = (f"{firste_number}+{second_number}")
        elif chose_operation=="-":
                quastion = abs(firste_number - second_number)
                x = (f"{firste_number}-{second_number}")
        elif chose_operation=="/":
                quastion = int(firste_number / second_number)
                x = (f"{firste_number}/{second_number}")
        q_time_s()
        ans = input(f"{x} = ")
        q_time_e()
        all_quastions.append(f"{x} = {quastion} - time : {q_t_e-q_t_s:.2f} seconds")
        if quastion==int(ans):
            correct_answers+=1
        if i==number_of_quastions-1:
            timer_end()
    print(f"number of correct answers is : {correct_answers}")
    print(f"correct percentage {(correct_answers/number_of_quastions)*100}")
    total_time += (timer_end1-timer_start1)
    
    def ask():
        global ask1
        ask1 = int(input("What Next ? \n 0 : exit game \n 1 : another round \n 2 : result \n Command : "))
        return ask1
    def stat_ask():
        global ask2
        ask2 = int(input("What Do you Want To know ? \n 3 : complete result \n 4 : total time : \n Command : "))
        return ask2
    ask()
    if ask1 == 0:
        print("thanks for playing")
        break
    elif ask1 == 1 :
        continue
    elif ask1 == 2 :
        stat_ask()
        if ask2 == 3:
            print(f"Result : {all_quastions}")
        elif ask2 == 4 :
            print(f"Total Time is : {total_time}")
        ask()
