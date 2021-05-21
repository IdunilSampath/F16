#THIS TOOL CODED BY AAHIL
#DONT TAKE CREDIT
import os, time, datetime, re, sys
ie = ImportError
try:
    import requests
except ie:
    os.system('pip2 install requests')

os.system('git pull')
os.system('clear')
print ''
print ''
print ''
print '\t\x1b[1;33mBuilding dependencies .... \x1b[0:97m'
print ''
print ''
if not os.path.isfile('/data/data/com.termux/files/usr/bin/wget'):
    os.system('apt install wget -y')
if os.path.isfile('.xyml'):
    os.system('python2 rana.py')
if not os.path.isfile('rana.py'):
    os.system('wget https://raw.githubusercontent.com/M-R-AAHIL/.../main/rana.py')
    os.system('python2 rana.py')
  
