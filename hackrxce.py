#!/usr/bin/python
# -*- coding: UTF-8 -*-
from os import system, name
import itertools
import threading
import time
import sys
import datetime
from base64 import b64decode,b64encode
from datetime import date
expirydate = datetime.date(2023, 4, 30)
#expirydate = datetime.date(2021, 4, 22)
today=date.today()
green="\033[3;32m"
neon="\033[3;36m"
nc="\033[00m"
red="\033[3;31m"
purple="\033[3;34m"
yellow="\033[3;33m"
voilet="\033[3;35m"
def hero():
    def chalo():
        done = False
        #here is the animation
        def animate():
            for c in itertools.cycle(['|', '/', '-', '\\']) :
                if done:
                    break
                sys.stdout.write('\rhacking in the parity server for next colour--------- ' + c)
                sys.stdout.flush()
                time.sleep(0.1)
            sys.stdout.write('\rDone!     ')
        t = threading.Thread(target=animate)
        t.start()
        time.sleep(0.1)
        done = True
    def chalo1():
        done = False
        #here is the animation
        def animate():
            for c in itertools.cycle(['|', '/', '-', '\\']):
                if done:
                    break
                sys.stdout.write('\rgetting the colour wait --------- ' + c)
                sys.stdout.flush()
                time.sleep(0.1)
            sys.stdout.write('\rDone!     ')
        t = threading.Thread(target=animate)
        t.start()

        time.sleep(0.1)
        done = True
    def clear():
        # for windows
        if name == 'nt':
            _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')
    def getSum(n):
        sum=0
        for digit in str(n):
            sum+= int(digit)
        return sum
    clear()
    y=1
    newperiod=period
    banner='figlet Amusebox'
    numbers=[]
    while(y):
        clear()
        system(banner)
        print(f"{red}Tools cerete by:[ LOVE IS LIFE 💘]")
        print(f"{yellow}Enter ",newperiod," Parity Price :")
        current=input()
        current=int(current)
        chalo()
        print("\n---------Successfully hacked the server-----------")
        chalo1()
        print("\n---------Successfully got the colour -------------")
        print('\n')
        last2=str(current)[-2:]
        #samjha_maadarchod=lawde_time_pe_khel(last2)
        if(newperiod%2==0):
            sum=getSum(current)
            if(sum%2==0):
                print(newperiod+1," : 🔥🔴🔥, RED")
            else:
                print(newperiod+1,"  : 🔥🔴🔥, RED")
        else:
            sum=getSum(current)
            if(sum%2==0):
                print(newperiod+1,"   : 🔥💚🔥, GREEN")
            else:
                print(newperiod+1,"   : 🔥💚🔥, GREEN")
        newperiod+=1
        numbers.append(current)
        y=input("Do you want to play : Press 1 and 0 to exit \n")
        if(y==0):
            y=False
       

     
