from time import sleep


count = "true"


time = [0, 0, 0,]

while count == "true":
    if time[2] < 60:
        time[2] += 1
    if time[2] == 60:
        time[1] += 1
        time[2] = 0
    if time[1] == 60:
        time[0] += 1
        time[1] = 0
    

    print(time)
    sleep(0.0000)
  

