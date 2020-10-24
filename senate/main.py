#!/usr/in/python3

import boto3

import ec2_functions
from tools.aws_connect import *
from ec2_functions.ec2_general import *
from ec2_functions.ec2_ebs import *
from ec2_functions.ec2_cpu import *
from ec2_functions.ec2_network import *

###
# Main
###

if __name__ == "__main__":
	try:

		client_ec2 = connect_ec2()
		clientCloudwatch = connect_cloudwatch()
		print (" \n################################ \
				 \nUn-used EBS \
			     \n################################"\
		)
		list_unused_ebs_vol(client_ec2)
		instance_list = list_ec2_instances(client_ec2)
		if instance_list == []:
			print ("#### No running instances ####")
		else:
			for instanceID in instance_list:
				print (" \n################################ \
						 \nData for : " + str(instanceID)+" \
				 		 \n################################"\
					  )
				instance_cpu_usage(clientCloudwatch,instanceID)
				instance_network_traffic(clientCloudwatch,instanceID)
		

##
#Analyse CPU credit. If low advice to change machine type	

#
# Analyse Disk Write and Read. If close to max IOPS,  advice to change 
		
	except Exception as err:
		print(err)