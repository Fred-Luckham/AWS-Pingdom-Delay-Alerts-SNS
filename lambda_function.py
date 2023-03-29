import json
import boto3
import os

def lambda_handler(event, context):
   client = boto3.client('sns')
   new_line = '\n'
   if event['current_state'] == "UP" and event['pass_on'] == False:
      time_difference_text = f"Site was down for: {event['time_difference']}{new_line}"
   else:
      time_difference_text = ""
   response = client.publish (
      TopicArn = os.environ['TopicARN'],
      Subject= f"{event['full_url']} has an alert",
      Message = f"{time_difference_text}Site: {event['full_url']}{new_line}Check Type: {event['check_type']}{new_line}Check Name: {event['check_name']}{new_line}Description: {event['long_description']}{new_line}Current State: {event['current_state']}{new_line}State Changed: {event['state_changed_utc_time']}"
   )
   print(response)
   return {
      'statusCode': 200,
      'body': json.dumps(response)
   }
