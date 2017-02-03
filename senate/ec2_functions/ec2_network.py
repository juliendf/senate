#!/usr/in/python3

import boto3
from datetime import datetime, timedelta
from yaml import load, dump

# doc http://boto3.readthedocs.io/en/latest/reference/services/cloudwatch.html?highlight=cloudwatch#CloudWatch.Client.get_metric_statistics


def instance_network_traffic(clientCloudwatch, instance_id):

	#Read config file /Users/julien.defreitas/Documents/dev-perso/senate/senate/
	with open('/usr/src/app/senate/config.yaml', 'r') as f:
		configFile = load(f)

	dayPeriod = configFile["network_check"]["dayPeriod"] # Period for calcul in days

	"""
	print clientCloudwatch.list_metrics(Namespace="AWS/EC2", MetricName="NetworkIn")
	u'MetricName': 'NetworkIn'}, {u'Namespace': 'AWS/EC2', u'Dimensions': [{u'Name': 'InstanceId', u'Value': 'i-86c22a10'}], u'MetricName': 'NetworkIn'}], 
	"""
	endDate = datetime.today() - timedelta(days=dayPeriod)
	NetworkTrafficIn = clientCloudwatch.get_metric_statistics(Namespace='AWS/EC2',MetricName='NetworkIn',
		Dimensions=[
			{
				'Name': 'InstanceId',
				'Value': instance_id
			},
		],
		StartTime=endDate,
		EndTime=datetime.now(),
		Period=3600,
		Statistics=[
		'Average',
		],
		Unit='Bytes'
	)

	NetworkTrafficOut = clientCloudwatch.get_metric_statistics(Namespace='AWS/EC2',MetricName='NetworkOut',
		Dimensions=[
			{
				'Name': 'InstanceId',
				'Value': instance_id
			},
		],
		StartTime=endDate,
		EndTime=datetime.now(),
		Period=3600,
		Statistics=[
		'Average',
		],
		Unit='Bytes'
	)

### Calculate total network traffic	
	print ("\n#### Cloudwatch metric : Network In ####")
	resultNetworkTrafficIn = 0
	for idx, data in enumerate(NetworkTrafficIn["Datapoints"]):
		resultNetworkTrafficIn = resultNetworkTrafficIn + int(data["Average"])
	
	if idx > 0:	
		print ("Average NetworkIn per hour for the period : " + str(resultNetworkTrafficIn / idx) + " Bytes")
	else :
		print ("insufficient data points")


	print ("\n#### Cloudwatch metric : Network Out ####")
	resultNetworkTrafficOut = 0
	for idx, data in enumerate(NetworkTrafficOut["Datapoints"]):
		resultNetworkTrafficOut = resultNetworkTrafficOut + int(data["Average"])
	
	if idx > 0:
		print ("Average NetworkOut for the period : " + str(resultNetworkTrafficOut / idx) + " Bytes")
	else :
		print ("insufficient data points")

	# Should it be 5MB /day or 5MB /hour ?
	print ("\nTotal Traffic : " + str(int((resultNetworkTrafficIn + resultNetworkTrafficOut)/1024)/dayPeriod) + " MB per day")