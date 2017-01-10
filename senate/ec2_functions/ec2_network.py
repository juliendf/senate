#!/usr/in/python3

import boto3
from datetime import datetime, timedelta

# doc http://boto3.readthedocs.io/en/latest/reference/services/cloudwatch.html?highlight=cloudwatch#CloudWatch.Client.get_metric_statistics


def instance_network_traffic(clientCloudwatch, instance_id):
	"""
	print clientCloudwatch.list_metrics(Namespace="AWS/EC2", MetricName="NetworkIn")
	u'MetricName': 'NetworkIn'}, {u'Namespace': 'AWS/EC2', u'Dimensions': [{u'Name': 'InstanceId', u'Value': 'i-86c22a10'}], u'MetricName': 'NetworkIn'}], 
	"""
	dayPeriod = 14
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
	print "\n#### Cloudwatch metric : Network In ####"
	resultNetworkTrafficIn = 0
	for idx, data in enumerate(NetworkTrafficIn["Datapoints"]):
		resultNetworkTrafficIn = resultNetworkTrafficIn + int(data["Average"])
		
	print "Average NetworkIn per hour for the period : " + str(resultNetworkTrafficIn / idx) + " Bytes"


	print "\n#### Cloudwatch metric : Network Out ####"
	resultNetworkTrafficOut = 0
	for idx, data in enumerate(NetworkTrafficOut["Datapoints"]):
		resultNetworkTrafficOut = resultNetworkTrafficOut + int(data["Average"])
		
	print "Average NetworkOut for the period : " + str(resultNetworkTrafficOut / idx) + " Bytes"

	# Should it be 5MB /day or 5MB /hour ?
	print "Total Traffic : " + str(int((resultNetworkTrafficIn + resultNetworkTrafficOut)/1024)/dayPeriod) + " MB per day"