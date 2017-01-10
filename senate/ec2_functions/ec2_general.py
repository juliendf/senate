#!/usr/in/python3

import boto3

def list_ec2_instances(client):
	# List alll instances ID
	instance_list = []
	for idx, data in enumerate(client.describe_instances()["Reservations"]):
		instance_list.append(str(data["Instances"][0]["InstanceId"]))

	return instance_list