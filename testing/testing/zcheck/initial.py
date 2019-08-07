#!/usr/bin/env python3

import subprocess
import paramiko
import re

output = []

nmap_command_output = subprocess.check_output("sudo nmap -Pn -p 22 -sS 172.25.0.2-254 | grep open -C 3 | grep -E -o '([0-9]{1,3}[\.]){3}[0-9]{1,3}'", shell=True)

ip_addr = nmap_command_output.rstrip().decode('ascii')

info_file = open("/home/ubuntu/details.txt", "w+")
info_file.write(ip_addr + '\n')

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.MissingHostKeyPolicy())

client.connect(ip_addr, 22, username='ubuntu', password='ubuntu')

commands = [
    'cat my_passwd',
    'cat my_fwllrule'
]

for command in commands:   
    stdin, stdout, stderr = client.exec_command(command)
    stdin.close()
    
    command_output = stdout.readlines()
    if len(command_output) > 0:
        output.append(command_output)

    stdout.close()
    stderr.close()

for eachline in output:
	for each in eachline:
		info_file.write(str(each))


port_command = 'grep telnet /etc/services'
stdin, stdout, stderr = client.exec_command(port_command)
stdin.close()
port_command_output = stdout.readlines()[0]
port_command_output = re.findall("(\d+){1,5}", port_command_output)[0]
info_file.write(port_command_output)
stdout.close()
stderr.close()

info_file.close()

client.close
