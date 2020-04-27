
from __future__ import print_function
import pickle
import logging
import os.path
import requests

from google.auth.transport.requests import Request
from flow import InstalledAppFlow

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['drive']

logging.basicConfig(level=logging.DEBUG)

def main():
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.

    flow = InstalledAppFlow.from_client_secrets_file(
        "credentials.json", SCOPES)

    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds = flow.refresh_token(creds.refresh_token)
        else:
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    api_call_headers = {'Authorization': 'Bearer ' + creds.token}
    api_call_response = requests.get("https://cloud-ens.index-education.local/index-cloud-portal-ens-ws/rest/Drive.content", headers=api_call_headers, verify=False)


    print(api_call_response.text)


if __name__ == '__main__':
    main()