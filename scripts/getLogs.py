
with open('/var/minecraft/server/logs/latest.log') as logs:
    with open('/home/lol/server/minecraft-backend-server/logs.txt', 'w') as newLog:
        for line in logs:
            newLog.write(line)
            
