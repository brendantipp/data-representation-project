# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gmail_quickstart]
from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import json
import csv
from xlwt import *

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    
        # Call the Gmail API
    service = build('gmail', 'v1', credentials=creds)
    response = service.users().messages().list(userId='me').execute()
    #print (results)
    #print (response)



    messages = []
    if 'messages' in response:
        messages.extend(response['messages'])

    while 'nextPageToken' in response:
        page_token = response['nextPageToken']
        response = service.users().messages().list(userId='me', pageToken=page_token).execute()
        messages.extend(response['messages'])

    for message in messages:
        #print(message['id'])
        completeMessage = service.users().messages().get(userId='me', id = message['id']).execute()
        #print(completeMessage['snippet'])
        headers = completeMessage['payload']['headers']
        #print (headers)
        snippet = completeMessage['snippet']
        subject = list(filter(lambda h: h['name']=='Subject',headers))[0]['value']
        
        massageTo = list(filter(lambda h: h['name']=='To',headers))[0]['value']
        messageFrom = list(filter(lambda h: h['name']=='From',headers))[0]['value']
        print (messageFrom)
        # you can put this information into an excel spreadsheet here
        

        with open('aMessage.json', 'w') as f:
            json.dump(completeMessage, f, indent=4)

        rowNumber = 1

        with open('test.csv', 'w') as e:
            writer = csv.writer(e)
            #writer.writerow(id,messageFrom,subject)
            writer.writerow(messageFrom)
            rowNumber += 1
            


    #except HttpError as error:
        #TODO(developer) - Handle errors from gmail API.
        #print(f'An error occurred: {error}')


if __name__ == '__main__':
    main()
# [END gmail_quickstart]