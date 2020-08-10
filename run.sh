pkg install -y figlet toilet
echo "Please enter your first name : "
read fname
echo "Please enter your last name : "
read lname
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
