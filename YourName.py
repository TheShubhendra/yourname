import os
if os.path.exists("/data/data/com.termux/files/usr/etc/motd"):
  os.remove("/data/data/com.termux/files/usr/etc/motd")
fname = input("please enter your first name:")
if fname = "" :
  print("Don't Leave it blank")
lname = input("Please enter your last name:")
file = open("/data/data/com.termux/files/usr/etc/bash.bashrc","w")
code1 ="if  [ -x /data/data/com.termux/files/usr/libexec/termux/command-not-found ]; then\n    command_not_found_handle(){\n /data/data/com.termux/files/usr/libexec/termux/command-not-found ' $1'\n}\nfi\nPS1='\$'"
code2 = "\nclear\necho -e '\e[1;31m' \nfiglet "+fname+"\necho -e '\e[1;33m'\ntoilet --filter border --metal "+lname+"\n echo -e '\e[1;32m' hello!! welcome "+fname+" "+lname
file.write(code1+code2)
file.close()
##This code is written by THE GENIUS HACKER. ALL RIGHTS ARE RESERVED https://fb.me/TheGeniusHacker 
