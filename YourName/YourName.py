import os
if os.path.exists("/data/data/com.termux/files/usr/etc/motd"):
  os.remove("/data/data/com.termux/files/usr/etc/motd")
fname = input("please enter your first name:")
lname = input("Please enter your last name:")
file = open("/data/data/com.termux/files/usr/etc/bash.bashrc","w")
code1 ="PS1='\$'"
code2 = "\nclear\necho -e '\e[1;31m' \nfiglet "+fname+"\necho -e '\e[1;33m'\ntoilet --filter border --metal "+lname+"\n echo -e '\e[1;32m' hello!! welcome "+fname+" "+lname + " '\e[m'"
file.write(code1+code2)
file.close()
##This code is written by THE GENIUS HACKER. ALL RIGHTS ARE RESERVED https://fb.me/TheGeniusHacker 
