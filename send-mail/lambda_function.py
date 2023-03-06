import boto3
import requests
import json
import os

def grecaptcha_verify(request):
    print('right --> ', request)
    if request['requestContext']['http']['method'] == 'POST':
        body = json.loads(request['body'])
        print("request body is --> ", body)
        captcha_rs = body['g-recaptcha-response']
        print(captcha_rs)
        url = "https://www.google.com/recaptcha/api/siteverify"
        params = {
            'secret': 'add asecret',
            'response': captcha_rs
        }
        verify_rs = requests.get(url, params=params, verify=True)

        verify_rs = verify_rs.json()
        print(verify_rs)

        return True == verify_rs.get("success", False)
 
ses = boto3.client('ses')

from_email = "faroug@hitpixel.com"


def lambda_handler(event, context):
    if(grecaptcha_verify(event)):
        destination_emails = bytes(os.environ['Destination'], 'utf-8').lower()
        # print(Destination_emails)
        body = json.loads(event['body'])
        mail_body = f"""Hi there. A contact form submission was sent from NetValve.com. Details below: \n \
        \n
        Email: {body['email']}, \n\
        Subject: {body['subject']}, \n\
        Message: {body['message']} \n\
        \n
        Kind Regards \n\
        The NetValve Test Team,"""
        print("the email body is --> ", mail_body)

        email_message = {
            'Body': {
                'Text': {
                    'Charset': 'utf-8',
                        'Data': mail_body
                },
            },
            'Subject': {
                'Charset': 'utf-8',
                'Data': 'NetValve Inquiry' 
            }
        }
        list_of_destination_emails = []
        for emails in destination_emails.decode('utf8').split(' '):
             list_of_destination_emails.append(emails)
             print (emails)
        print(list_of_destination_emails)
        ses_response = ses.send_email(
        Destination = {
            'ToAddresses': list_of_destination_emails
        },
        Message=email_message,
        Source=from_email
        )
        return ses_response['ResponseMetadata']['HTTPStatusCode']
    else:
        return {"statusCode": 401}