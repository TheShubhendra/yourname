if [ $(dpkg-query -W -f='${Status}' figlet 2>/dev/null | grep -c "ok installed") -eq 0 ];
then
  echo "Instaling Figlet"
  apt-get install -y figlet
fi
if [ $(dpkg-query -W -f='${Status}' toilet 2>/dev/null | grep -c "ok installed") -eq 0 ];
then
  echo "Installing Toilet"
  apt-get -y toilet
fi
echo "Please enter your first name : "
read fname
echo "Please enter your last name : "
read lname
if [ -e /data/data/com.termux/files/user/etc/motd ]
then
   rm -f /data/data/com.termux/files/user/etc/motd 
fi
cat > /data/data/com.termux/files/usr/etc/bash.bashrc <<EOL
PS1='\$ '
clear
echo -e '\e[1;31m'
figlet $fname
echo -e '\e[1;33m'
toilet --filter border --metal $lname
echo -e '\e[1;32m'
echo Hello! Welcome $fname $lname 
echo -e '\e[m'
EOL
