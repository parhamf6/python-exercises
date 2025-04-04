from datetime import datetime, timedelta
stratTime = "15:41:30"
endTime = "18:00:00"
t1 = datetime.strptime(stratTime , "%H:%M:%S")
t2 = datetime.strptime(endTime , "%H:%M:%S")
if t2 < t1:
    t2 += timedelta(days=1)
delta = t2 - t1
print(delta)
