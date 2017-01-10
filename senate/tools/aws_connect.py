#!/usr/in/python3

import boto3

def connect_ec2():
	client = boto3.client('ec2')
	return client

def connect_cloudwatch():
	client = boto3.client('cloudwatch')	
	return client