import os
import json

def firewall_delete(project_name,channelID):
	firewall_delete ={
						"displayName": "Firewall-Delete",
						"combiner": "OR",
						"conditions": [
						  {
							"displayName": "Metric Threshold on Log Metrics",
							"conditionThreshold": {
							   "aggregations": [
								 {
								   "alignmentPeriod": "60s",
								   "perSeriesAligner": "ALIGN_RATE",
								 }],
							  "comparison": "COMPARISON_GT",
							  "duration": "60s",
							  "filter": "metric.type=\"logging.googleapis.com/user/alert-firewall-delete\" AND resource.type=\"global\"",
							  "thresholdValue": 0,
							  "trigger": {
								"count": 1
							   }
							}
						  }
						],
						"notificationChannels": [
                            "projects/"+project_name+"/notificationChannels/"+channelID
						]
					}
	f = open("firewall_delete.json", "w")
	f.write(json.dumps(firewall_delete))
	f.close()

	os.system("gcloud alpha monitoring policies create --policy-from-file=./firewall_delete.json")
	os.system("rm ./firewall_delete.json")
	print('[+] Created Monitoring Policy for Firewall-Delete')

def firewall_insert(project_name, channelID):
	firewall_insert ={
						"displayName": "Firewall-Insert",
						"combiner": "OR",
						"conditions": [
						  {
							"displayName": "Metric Threshold on Log Metrics",
							"conditionThreshold": {
							   "aggregations": [
								 {
								   "alignmentPeriod": "60s",
								   "perSeriesAligner": "ALIGN_RATE",
								 }],
							  "comparison": "COMPARISON_GT",
							  "duration": "60s",
							  "filter": "metric.type=\"logging.googleapis.com/user/alert-firewall-insert\" AND resource.type=\"global\"",
							  "thresholdValue": 0,
							  "trigger": {
								"count": 1
							   }
							}
						  }
						],
						"notificationChannels": [
							"projects/"+project_name+"/notificationChannels/"+channelID
						]
					  }
	f = open("firewall_insert.json", "w")
	f.write(json.dumps(firewall_insert))
	f.close()

	os.system("gcloud alpha monitoring policies create --policy-from-file=./firewall_insert.json")
	os.system("rm ./firewall_insert.json")
	print('[+] Created Monitoring Policy for Firewall-Insert')

def firewall_patch(project_name,channelID):
	firewall_patch = {
						"displayName": "Firewall-Patch",
						"combiner": "OR",
						"conditions": [
						  {
							"displayName": "Metric Threshold on Log Metrics",
							"conditionThreshold": {
							   "aggregations": [
								 {
								   "alignmentPeriod": "60s",
								   "perSeriesAligner": "ALIGN_RATE",
								 }],
							  "comparison": "COMPARISON_GT",
							  "duration": "60s",
							  "filter": "metric.type=\"logging.googleapis.com/user/alert-firewall-patch\" AND resource.type=\"global\"",
							  "thresholdValue": 0,
							  "trigger": {
								"count": 1
							   }
							}
						  }
						],
						"notificationChannels": [
							"projects/"+project_name+"/notificationChannels/"+channelID
						]
					  }
	f = open("firewall_patch.json", "w")
	f.write(json.dumps(firewall_patch))
	f.close()

	os.system("gcloud alpha monitoring policies create --policy-from-file=./firewall_patch.json")
	os.system("rm ./firewall_patch.json")
	print('[+] Created Monitoring Policy for Firewall-Patch')

def serviceAccount_create(project_name,channelID):
	serviceAccount_create ={
						"displayName": "serviceAccount-create",
						"combiner": "OR",
						"conditions": [
						  {
							"displayName": "Metric Threshold on Log Metrics",
							"conditionThreshold": {
							   "aggregations": [
								 {
								   "alignmentPeriod": "60s",
								   "perSeriesAligner": "ALIGN_RATE",
								 }],
							  "comparison": "COMPARISON_GT",
							  "duration": "60s",
							  "filter": "metric.type=\"logging.googleapis.com/user/alert-serviceAccount-create\" AND resource.type=\"global\"",
							  "thresholdValue": 0,
							  "trigger": {
								"count": 1
							   }
							}
						  }
						],
						"notificationChannels": [
							"projects/"+project_name+"/notificationChannels/"+channelID
						]
					  }
	f = open("serviceAccount_create.json", "w")
	f.write(json.dumps(serviceAccount_create))
	f.close()

	os.system("gcloud alpha monitoring policies create --policy-from-file=./serviceAccount_create.json")
	os.system("rm ./serviceAccount_create.json")

def serviceAccount_delete(project_name,channelID):
	serviceAccount_delete = {
						"displayName": "serviceAccount-delete",
						"combiner": "OR",
						"conditions": [
						  {
							"displayName": "Metric Threshold on Log Metrics",
							"conditionThreshold": {
							   "aggregations": [
								 {
								   "alignmentPeriod": "60s",
								   "perSeriesAligner": "ALIGN_RATE",
								 }],
							  "comparison": "COMPARISON_GT",
							  "duration": "60s",
							  "filter": "metric.type=\"logging.googleapis.com/user/alert-serviceAccount-delete\" AND resource.type=\"global\"",
							  "thresholdValue": 0,
							  "trigger": {
								"count": 1
							   }
							}
						  }
						],
						"notificationChannels": [
							"projects/"+project_name+"/notificationChannels/"+channelID
						]
					  }
	f = open("serviceAccount_delete.json", "w")
	f.write(json.dumps(serviceAccount_delete))
	f.close()

	os.system("gcloud alpha monitoring policies create --policy-from-file=./serviceAccount_delete.json")
	os.system("rm ./serviceAccount_delete.json")

def serviceAccount_createKey(project_name,channelID):
	serviceAccount_createKey = {
						"displayName": "serviceAccount-createKey",
						"combiner": "OR",
						"conditions": [
						  {
							"displayName": "Metric Threshold on Log Metrics",
							"conditionThreshold": {
							   "aggregations": [
								 {
								   "alignmentPeriod": "60s",
								   "perSeriesAligner": "ALIGN_RATE",
								 }],
							  "comparison": "COMPARISON_GT",
							  "duration": "60s",
							  "filter": "metric.type=\"logging.googleapis.com/user/alert-serviceAccount-createKey\" AND resource.type=\"global\"",
							  "thresholdValue": 0,
							  "trigger": {
								"count": 1
							   }
							}
						  }
						],
						"notificationChannels": [
							"projects/"+project_name+"/notificationChannels/"+channelID
						]
					  }

	f = open("serviceAccount_createKey.json", "w")
	f.write(json.dumps(serviceAccount_createKey))
	f.close()

	os.system("gcloud alpha monitoring policies create --policy-from-file=./serviceAccount_createKey.json")
	os.system("rm ./serviceAccount_createKey.json")

def serviceAccount_deleteKey(project_name, channelID):
	serviceAccount_deleteKey = {
						"displayName": "serviceAccount-deleteKey",
						"combiner": "OR",
						"conditions": [
						  {
							"displayName": "Metric Threshold on Log Metrics",
							"conditionThreshold": {
							   "aggregations": [
								 {
								   "alignmentPeriod": "60s",
								   "perSeriesAligner": "ALIGN_RATE",
								 }],
							  "comparison": "COMPARISON_GT",
							  "duration": "60s",
							  "filter": "metric.type=\"logging.googleapis.com/user/alert-serviceAccount-deleteKey\" AND resource.type=\"global\"",
							  "thresholdValue": 0,
							  "trigger": {
								"count": 1
							   }
							}
						  }
						],
						"notificationChannels": [
							"projects/"+project_name+"/notificationChannels/"+channelID
						]
					  }

	f = open("serviceAccount_deleteKey.json", "w")
	f.write(json.dumps(serviceAccount_deleteKey))
	f.close()

	os.system("gcloud alpha monitoring policies create --policy-from-file=./serviceAccount_deleteKey.json")
	os.system("rm ./serviceAccount_deleteKey.json")

def iamrole(project_name, channelID):
	iamrole = {
		  "displayName": "IAM-role",
		  "combiner": "OR",
		  "conditions": [
			{
			  "displayName": "Metric Threshold on Log Metrics",
			  "conditionThreshold": {
				 "aggregations": [
				   {
					 "alignmentPeriod": "60s",
					 "perSeriesAligner": "ALIGN_RATE",
				   }],
				"comparison": "COMPARISON_GT",
				"duration": "60s",
				"filter": "metric.type=\"logging.googleapis.com/user/alert-iamrole\" AND resource.type=\"global\"",
				"thresholdValue": 0,
				"trigger": {
				  "count": 1
				 }
			  }
			}
		  ],
		  "notificationChannels": [
			  "projects/"+project_name+"/notificationChannels/"+channelID
		  ]
		}

	f = open("iamrole.json", "w")
	f.write(json.dumps(iamrole))
	f.close()

	os.system("gcloud alpha monitoring policies create --policy-from-file=./iamrole.json")
	os.system("rm ./iamrole.json")

def create_slack():
    os.system("gcloud alpha monitoring channels create --channel-content-from-file=./slack_notification.json")