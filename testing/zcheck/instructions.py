#!/usr/bin/env python3
import random

def char_pswd(password1):
    pass_lower = any(p.islower() for p in password1)
    pass_upper = any(q.isupper() for q in password1)
    pass_numeric = any(r.isnumeric() for r in password1)

    cnt_string = " and consists of "

    if pass_lower:
        cnt_string = cnt_string + 'a-z'
    if pass_upper:
        cnt_string = cnt_string + 'A-Z'
    if pass_numeric:
        cnt_string = cnt_string + '0-9'
    
    cnt_string = cnt_string + ' characters.'

    if len(password1) > 4:
        inst_file.write(" \n The password is suspected to be " + str(len(password1)-1) + " characters long, starting with " + password1[:-2] + cnt_string)
    elif len(password1) > 3:
        inst_file.write(" \n The password is suspected to be " + str(len(password1)-1) + " characters long, starting with " + password1[:-2] + cnt_string)
    else:
        inst_file.write(" \n The password is suspected to be " + str(len(password1)-1) + " characters long, starting with " + password1[:-2] + cnt_string)

def prt_rng(port, num):

    searh_rng = []

    lower_rng = port-random.randint(1,num)
    if lower_rng < 0:
        lower_rng = 0
    
    searh_rng.append(lower_rng)

    upper_rng = port+random.randint(1,num)
    
    if upper_rng > 65535:
        upper_rng = 65535

    searh_rng.append(upper_rng)

    return searh_rng



def char_intf(port,rule):

    port = int(port)

    if len(rule) > 5:
        inst_file.write(" \n The telnet service is hidden through port knocking, an obscure TCP flag is required to reveal the service, which is suspected to have a port ranging from " + str(prt_rng(port, 1500)[0]) + " to " + str(prt_rng(port, 1500)[1]))
    elif "NONE" == rule or "ALL" == rule:
        inst_file.write(" \n The telnet service is hidden through port knocking, an obscure TCP flag is required to reveal the service, which is suspected to have a port ranging from " + str(prt_rng(port, 1500)[0]) + " to " + str(prt_rng(port, 1500)[1]))
    else:
        inst_file.write(" \n The telnet service is hidden through port knocking, a common TCP flag is required to reveal the service, which is suspected to have a port ranging from " + str(prt_rng(port, 2500)[0]) + " to " + str(prt_rng(port, 2500)[1]))



info_file = open("/home/ubuntu/details.txt", 'r')
info_file_lines = info_file.readlines()
info_file.close

addr = info_file_lines[0]
pswd = info_file_lines[1]
fwll = info_file_lines[2]
port = info_file_lines[3]

inst_file = open("/home/ubuntu/instructions.txt", 'w+')

inst_file.write(r"""  _____ _____ _       
 |_   _/ ____| |      
   | || |    | |      
   | || |    | |      
  _| || |____| |____  
 |_____\_____|______| 
                      """)

inst_file.write(" \n Welcome to (I)ndividualised (C)ybersecurity (L)abs! \n")

inst_file.write(" \n Activity: Advanced network scanning and password cracking \n")

inst_file.write(" \n In this exercise, you are tasked to identify the suspicious file contents accessible through a backdoor left by a disgruntled former employee boris.")
inst_file.write(" \n \n The backdoor is believed to be a credentialed telnet service on an unusual port somewhere on the " + str(addr) + " host.")

char_intf(port,fwll)

char_pswd(pswd)

inst_file.write(" \n Enter 'check' to recieve immediate feedback and track your progress \n")

inst_file.write(" \n Once complete, feel free to repeat the lab with the command 'labtainer -r testing' and providing another email \n")

inst_file.write(" \n Afterwards could you please fill in the following questionaire: 'https://forms.gle/S52wAQfNppAkp13r7' \n")








inst_file.close
