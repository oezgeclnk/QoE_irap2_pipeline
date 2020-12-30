import os
import time

#This script uses tc-tool to limit the uplink and downlink traffic between the chosen limits (e.g 3Mbit-500Kbit), and reduce the rate (as chosen) during a time interval.
###########################################################
#User Settings:
bandwidth_max=8000 #Set maximum bandwidth (kbit/s)
bandwidth_min=500 #Set minimum bandwidth (kbit/s)
t=5  #Set waiting time(seconds) between each change 
reduce_rate=2000 # Set how much bandwidth to reduce per t
timer=60*60 #Set total timer (seconds)
interface_downlink="wlp1s0" # Set the name of downlink interace
interface_uplink="enp0s31f6" #Set the name of uplink interface
###########################################################
#Start applying rules
t_end = time.time() + timer
bandwidth=bandwidth_max #sets initial bandwidth to maximum
try:
	while time.time() < t_end:
		if bandwidth >=bandwidth_min:
			print("applying new rule\n")
			os.system("tc qdisc add dev " +interface_downlink+ " root netem rate " + str(bandwidth)+ "kbit") #Insert tc ruleset for downlink
			os.system("tc qdisc add dev " +interface_uplink+ " root netem rate " + str(bandwidth)+ "kbit") #Insert tc ruleset for uplink
			print("Currently active rule for downlink:\n")
			os.system("tc qdisc show dev "+ interface_downlink)
			print("\n")
			print("Currently active rule for uplink:\n")
			os.system("tc qdisc show dev "+ interface_uplink)
			time.sleep(t)
			os.system("tc qdisc del dev "+ interface_downlink + " root") #Delete current rules
			os.system("tc qdisc del dev "+ interface_uplink + " root") #Delete current rules
			bandwidth-=reduce_rate #reduce bandwidth
		else:
			bandwidth=bandwidth_max #set bandwidth back to maximum		
except KeyboardInterrupt:
	#Delete current rules with keyboard interrupt (CTRL+C)
	os.system("tc qdisc del dev "+ interface_downlink +" root") 
	os.system("tc qdisc del dev "+ interface_uplink +" root")
	print('\nNetwork emulation finished, rules are deleted\n')
	time.sleep(1)
#Delete rules when the time is up
os.system("tc qdisc del dev "+ interface_downlink +" root") #Delete current rules
os.system("tc qdisc del dev "+ interface_uplink +" root") #Delete current rules
print("Script finished.")
time.sleep(1)
