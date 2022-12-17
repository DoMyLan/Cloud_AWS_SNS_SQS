import json
import boto3

print('Loading function')


def publish_msg(message):
	sqs = boto3.client('sqs')
	response  = sqs.send_message(
            QueueUrl='https://sqs.us-east-1.amazonaws.com/567384302075/sqstosns' ,
            MessageBody= message
        )
	return response


def lambda_handler(event, context):
	print('------------------------')
	print(event)
	publish_msg("helllo")
	try:
		for record in event['Records']:
			if record['eventName'] == 'MODIFY':
				MODIFY_FUNC(record)
		
		return "Success!"
	except Exception as e: 
		return "Error"


	
def MODIFY_FUNC(record):
	print("Handling MODIFY Event")

	oldImage = record['dynamodb']['OldImage']
	oldbalance = oldImage['Account balance']['S']
	
	newImage = record['dynamodb']['NewImage']
	newbalance = newImage['Account balance']['S']

# 	change = int(newbalance) - int(oldbalance)
#     print(change)
	message = 'Biến động số dư : '+oldbalance  +" to  " + newbalance
	publish_msg(message)
	if oldbalance != newbalance:
		message = 'Biến động số dư : '+ oldbalance +" to  " + newbalance
		print(message)
		publish_msg(message)

	print("Done handling MODIFY Event")