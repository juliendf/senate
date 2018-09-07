#!/usr/in/python3

import boto3
from datetime import datetime, timedelta
from yaml import load, dump

# doc http://boto3.readthedocs.io/en/latest/reference/services/cloudwatch.html?highlight=cloudwatch#CloudWatch.Client.get_metric_statistics


def instance_cpu_usage(clientCloudwatch, instance_id):
	"""
	print clientCloudwatch.list_metrics(Namespace='AWS/EC2')

	All metrcics
	u'MetricName': 'DiskWriteBytes'}, 
	u'MetricName': 'NetworkOut'}, 
	u'MetricName': 'StatusCheckFailed_Instance'}, 
	u'MetricName': 'StatusCheckFailed'},
	u'MetricName': 'NetworkIn'}, 
	u'MetricName': 'DiskReadOps'}, 
	u'MetricName': 'DiskReadBytes'}, 
	u'MetricName': 'StatusCheckFailed_System'},
	u'MetricName': 'CPUCreditBalance'}, 
	u'MetricName': 'DiskWriteOps'},
	u'MetricName': 'NetworkPacketsIn'},
	u'MetricName': 'NetworkPacketsOut'}, 
	u'MetricName': 'CPUCreditUsage'},
	u'MetricName': 'CPUUtilization'},
	"""

	# An instance had 10% or less daily average CPU utilization and 5 MB or less network I/O on at least 4 of the previous 14 days.
	"""
	print clientCloudwatch.list_metrics(Namespace="AWS/EC2", MetricName="CPUUtilization")
	u'MetricName': 'CPUUtilization'}, {u'Namespace': 'AWS/EC2', u'Dimensions': [{u'Name': 'InstanceId', u'Value': 'i-86c22a10'}], u'MetricName': 'CPUUtilization'}], 
	"""

	#Read config file /Users/julien.defreitas/Documents/dev-perso/senate/senate/
	with open('config.yaml', 'r') as f:
		configFile = load(f)

	dayPeriod = configFile["CPU_check"]["dayPeriod"] # Period for calcul in days
	cpuUsageHoursThreshold = configFile["CPU_check"]["cpuUsageHoursThreshold"]
	cpuusageThresholdPourcentage = configFile["CPU_check"]["cpuusageThresholdPourcentage"]




	#from datetime import datetime, timedelta
	endDate = datetime.today() - timedelta(days=dayPeriod)
	#print endDate
	#print datetime.now()
	unuseddays = 0

	CPUusage = clientCloudwatch.get_metric_statistics(Namespace='AWS/EC2',MetricName='CPUUtilization',
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
		Unit='Percent'
	)

	print ("\n#### Cloudwatch metric : CPU Utilisation ####")
	result = 0
	datapointLessThanThreshold = 0
	#Calculate the number of time, the CPU utilisation chart is under 10%. Analyse each datapoint, if <= 10% increase datapointLessThanThreshold
	for idx, data in enumerate(CPUusage["Datapoints"]):
		result = result + float(data["Average"])
		#print int(data["Average"])
		# Check if CPU usage if under 10%
		if int(data["Average"]) <= cpuusageThresholdPourcentage:
			datapointLessThanThreshold += 1

	if idx < cpuUsageHoursThreshold:
		print ("insufficient data points")
	else:
		print ("Unuseddays : " + str(int(datapointLessThanThreshold/24)))
		if int(datapointLessThanThreshold/24) > cpuUsageHoursThreshold:
			print ("warning")
		else:
			print ("Average CPU Utilisation for the period : " + str(result / idx) + " Pourcent")
