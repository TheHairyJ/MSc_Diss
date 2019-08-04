import subprocess
import paramiko
import re
from termcolor import colored

info_file = open("/etc/details.txt", "r")
info_file_lines = info_file.readlines()
info_file.close()

addr = info_file_lines[0].strip()
pswd = info_file_lines[1].strip()
fwll = info_file_lines[2].strip()
port = info_file_lines[3].strip()

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.MissingHostKeyPolicy())
client.connect(addr, 22, username='ubuntu', password='ubuntu')

# Input to check for the correct port
usr_input = input("On which port is the telnet service located?")
if port in usr_input:
	print('Successfully identified the telnet service: ' + colored('CHECK', 'green'))
else:
	print('Successfully identified the telnet service: ' + colored('CHECK', 'red'))


# Check for a login as Boris
login_command = 'who | grep boris'
stdin, stdout, stderr = client.exec_command(login_command)
stdin.close()

login_output = stdout.readlines()
if len(login_output) > 0:
	print('Successfully login as the user boris: ' + colored('CHECK', 'green'))
else:
	print('Successfully login as the user boris: ' + colored('CHECK', 'red'))

stdout.close()
stderr.close()

# Check for backdoor_details as Boris
cat_command = 'sudo tail -10 /var/log/auth.log'
stdin, stdout, stderr = client.exec_command(cat_command)
stdin.close()

cat_output = stdout.readlines()

cat_log = False

for log_output in cat_output:
	if 'COMMAND=/bin/cat backdoor_details.txt' in log_output:
		cat_log = True
if cat_log:
	print('Successfully read suspicious file: ' + colored('CHECK', 'green'))
else:
	print('Successfully read suspicious file: ' + colored('CHECK', 'red'))

stdout.close()
stderr.close()

client.close
