"""Adds ability to download new users file from google drive account."""

from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from apiclient import errors

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

def get_service():
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return build('drive', 'v3', credentials=creds)


def print_file_content(service, file_id):
    """Print a file's content.

    Args:
    service: Drive API service instance.
    file_id: ID of the file.

    Returns:
    File's content if successful, None otherwise.
    """
    try:
        return service.files().get_media(fileId=file_id).execute()
        
    except errors.HttpError as error:
        print(f'An error occurred: {error}')


def mock_print_file_content(service, file_id):
    return b'Activity Date,Distance in Miles,Activity Type\r\n2021-02-02,1.15,Walk\r\n2021-02-02,14.74,Ride\r\n2021-02-02,0.71,Walk\r\n2021-02-02,0.7,Ride\r\n2021-02-02,4.27,Walk\r\n2021-02-02,0.7,Ride\r\n2021-02-02,3.42,Walk\r\n2021-02-02,5.57,Ride\r\n2021-02-02,2.64,Walk\r\n2021-02-02,0.47,Walk\r\n'

if __name__ == '__main__':
    file_id = "1UJQnlz7IxJ27hqvnPYXl4jm-oWjr2Zo4"
    service = get_service()
    print_file_content(service, file_id)