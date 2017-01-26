#!/usr/in/python3

import boto3
from datetime import datetime, timedelta

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


	#from datetime import datetime, timedelta
	dayPeriod = 14 # Period for calcul in days
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
	datapointLessThan10 = 0
	#Calculate the number of time, the CPU utilisation chart is under 10%. Analyse each datapoint, if <= 10% increase datapointLessThan10
	for idx, data in enumerate(CPUusage["Datapoints"]):
		result = result + float(data["Average"])
		#print int(data["Average"])
		# Check if CPU usage if under 10%
		if int(data["Average"]) <= 10:
			datapointLessThan10 += 1

	print ("Unuseddays : " + str(int(datapointLessThan10/24)))
	if int(datapointLessThan10/24) > 4:
		print ("warning")

	print ("Average CPU Utilisation for the period : " + str(result / idx) + " Pourcent")