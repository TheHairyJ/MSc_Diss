#!/usr/bin/env bash
###############

declare -a StringArray=( "a-z" "A-Z" "0-9" "a-zA-Z" "a-z0-9" "A-Z0-9" "a-zA-Z0-9" )
size=${#StringArray[@]}
index=$(($RANDOM % $size))
var1=${StringArray[$index]}

declare -a array=( 3 4 5 )
aoo=${#array[@]}
boo=$(($RANDOM % $aoo))
var2=${array[$boo]}

coo=$(cat /dev/urandom | tr -dc "$var1" | head -c $var2)

echo $coo > /home/ubuntu/my_passwd

echo 'boris:'$coo | chpasswd
