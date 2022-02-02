import os

ramUsageValues = []
kbInGb = 0.00000095367431640625

with open('/home/lol/server/minecraft-backend-server/ramUsage.txt') as file:
    for line in file:
        ramUsageValues.append(line.strip())

freeMemArr = os.popen('vmstat -s | grep -i "used memory"').read().split(' ')
currFreeMem = freeMemArr[6] # 6 is because thers 6 spaces in the output

ramUsageValues.pop(0)
num = round(kbInGb * float(int(freeMemArr[6])), 1)
ramUsageValues.append(num) # new values to be written 


with open('/home/lol/server/minecraft-backend-server/ramUsage.txt', 'w') as file:
    for value in ramUsageValues:
        file.write(str(value)+'\n')