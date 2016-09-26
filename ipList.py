from subprocess import check_output as CO
from re import compile , findall , search
import sys
try:
    from prettytable import PrettyTable as pt #check for module
except ImportError:
    sys.exit("MODULE NOT AVAILABLE")
#Regex to extract IP address and corresponding Mac address from result of arp command
ipconfigCmdReg = compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+([0-9a-fA-F]{2}-[0-9a-fA-F]{2}-[0-9a-fA-F]{2}-[0-9a-fA-F]{2}-[0-9a-fA-F]{2}-[0-9a-fA-F]{2})')
outputx = ipconfigCmdReg.findall(str(CO("arp -a")))
tempRegS , tempRegE = compile(r'\d{3}') , compile(r'255$')
ipListDict = {}
for i in range(len(outputx)):
    c1 = True if int(tempRegS.search(str(outputx[i][0])).group(0)) < 224 else False
    c2 = True if tempRegE.search(str(outputx[i][0])) == None else False
    if c1 and c2:
        ipListDict[outputx[i][0]]= outputx[i][1]
    else:
        continue
x = pt(["IP Address","MAC Address"])
x.align["IP Address"] = "l"
for i in ipListDict:
    x.add_row([i,ipListDict[i]])
print(x)
