#!/bin/bash

#---------------------------------------------------------------------#
#TCPDUMP Options
#---------------------------------------------------------------------#

#https://superuser.com/questions/904786/tcpdump-rotate-capture-files-using-g-w-and-c

#https://unix.stackexchange.com/questions/29367/tcpdump-packets-captured-vs-packets-received-by-filter
#https://superuser.com/questions/964903/tcpdump-not-capturing-any-packets

#https://unix.stackexchange.com/questions/15989/how-to-process-pipe-tcpdumps-output-in-realtime
#https://unix.stackexchange.com/questions/229327/sniffing-packets-realtime/229336
#https://superuser.com/questions/1313554/how-do-i-read-output-from-tcpdump-as-quickly-as-it-prints-it-to-the-terminal

#sudo tcpdump -i $1 -G $2 -w $3-%H-%M-%S.pcap &

#sudo tcpdump -l --immediate-mode -i $1 -G $2 -w $3-%H-%M-%S.pcap &

#sudo tcpdump -l --immediate-mode -i $1 tcp -w $3-$4.pcap &

#sudo tcpdump -U -i $1 -w $3.pcap -G $2 -W 5 -C 5 &

#sudo tcpdump -U --immediate-mode -i $1 -G $2 -w $3-%H-%M-%S.pcap &

sudo tcpdump -Z root -U -i $1 -G $2 -w $3-%H-%M-%S.pcap &	#Not using immediate mode resulted in no packet loss
