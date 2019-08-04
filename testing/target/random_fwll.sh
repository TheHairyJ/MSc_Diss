#!/bin/bash

#
# Get $var1
#

declare -a StringArray=( "NONE" "FIN,PSH,URG" "FIN" "SYN" )
size=${#StringArray[@]}
index=$(($RANDOM % $size))
var1=${StringArray[$index]}

echo $var1 > /home/ubuntu/my_fwllrule

#
# IPTABLES
#

IPTABLES=/sbin/iptables

#
# Start and flush
#

$IPTABLES -F
$IPTABLES -t nat -F
$IPTABLES -X

#
#  By default, do not allow any forwarding or accept any traffic
#  destined for the firewall.
#

#$IPTABLES -P FORWARD DROP
#$IPTABLES -P INPUT   DROP 
$IPTABLES -P OUTPUT  ACCEPT

#
# INPUT
#

$IPTABLES -A INPUT -p icmp --icmp-type echo-request -j ACCEPT
$IPTABLES -A INPUT -p tcp --dport 22 -m conntrack --ctstate NEW,ESTABLISHED,RELATED -j ACCEPT
$IPTABLES -A INPUT -p tcp --tcp-flags ALL ACK -m recent --set --name KNOCKING --rsource -j ACCEPT
$IPTABLES -A INPUT -p tcp -m recent --rcheck --hitcount 1 --name KNOCKING --rsource -j ACCEPT 
$IPTABLES -A INPUT -j DROP # Drop all packets that get this far...









