#!/bin/bash
# Author: Harter-Liang
# Date: 2021/01/20
# Usage: Transmitting the pictures to the cloud-Server
# Version: 1.0
# Description: You can choose the commented sentences for different usage(For local-use or remote-backup etc.)
step=17
# Time for sleeping
for((i=0;i<51;i=(i+step) ));do
	# We can change the step for different time of sleeping
	echo "[+] At the time $(date)"
	echo "[+] Processing for the Picture$i"
	$(/usr/bin/python3 '/home/pi/picTest/drawGraph.py')
	# Processing the python script for generating pictures
	# echo "[+] Transmitting for Picture$i..."
	echo "Moving the Picture$i to destination!"
	eval "sudo mv TestFig.png /var/www/html/img/TestFig$i.png"
	# Moving the picture to the source destination of the server Document
	# eval "sshpass -p ["destination server password"] scp ["source directory"] ["destination server directory"]"
	# Transmitting the generated picture to the server, we can change the server as we want.
	# By the way, the usage of sshpass is in order to solve the problem of requirment of password during the scp procession
	echo "[+] The No.$i Picture successfully transmitted!"
	sleep $step
	# Wait for the next step of the whole process
done
# End of all the process
# echo "[+] All pictures has been generated and transmitted to the remote-server!"
echo "[+] All pictures has been generated and transmitted to the server-directory!"
exit 0
