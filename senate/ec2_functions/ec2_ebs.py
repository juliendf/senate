#!/usr/in/python3

import boto3

def list_unused_ebs_vol(client):
	print ("\n#### Unused EBS ####")
	notAttachedVolume = 0
	ebs_list = []

	for ebs_volume in client.describe_volumes()["Volumes"]:

		if len(ebs_volume["Attachments"]) == 0 :
			#print("Not attached")
			notAttachedVolume +=1
			ebs_list.append(str(ebs_volume["VolumeId"]))


		#else:
			#print ("Attached to : " + str(x["Attachments"][0]["InstanceId"]))
	print ("Total number of volumes : " + str(len(client.describe_volumes()["Volumes"])))
	print ("Total number of not attached volumes : " + str(notAttachedVolume))

	return ebs_list