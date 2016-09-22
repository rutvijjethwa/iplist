#!/usr/bin/python3
import subprocess , re
ipconfigCmd = str(subprocess.check_output("arp -a"))
ipconfigCmdReg = re.compile(r'(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})')
outputx = ipconfigCmdReg.findall(ipconfigCmd)
ipList = []
for i in range(len(outputx)):
    if int(outputx[i][3]) == 255:
        continue
    elif int(outputx[i][0]) < 224:
        ipList.append((str('.'.join(outputx[i]))))
print("List of active IP's in your network :")
for i in ipList:
    print(i)
