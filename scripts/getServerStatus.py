import os

status = os.popen("sudo su minecraft -c 'screen -ls' | head -1").read()

if status[:21] == "There is a screen on:":
    os.system("echo 'ON' > ~/scripts/status.txt") #~/scripts because this line get's executed remotely so it'll create a txt file in home directory without this
else:
    os.system("echo 'OFF' > ~/scripts/status.txt")