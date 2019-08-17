from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pandas as pd
import json


# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1xkLohYmwZLjFySDVYMj4AGDsWvnRaMzmvFaUPqsStL8'

def getSheetService():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
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
                './app/credentials.json', SCOPES)
            
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    service = build('sheets', 'v4', credentials=creds)
    return service

def getBudget(service,SAMPLE_RANGE_NAME='A15:H22'):
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])
    print('getting Sheet')
    records = []
    if not values:
        print('No data found.')
    else:
        try:
            for row in values:
                records.append(row)
        except IndexError:
            print('end of rows')
        print('values loaded')
    filter_rec = [i for i in records if len(i) > 1]
    fd = pd.DataFrame(filter_rec)
    print(fd.loc[0].values  .tolist())
    fd.columns = fd.loc[0].values
    fd.drop(0,inplace=True)
    fd['month'] = fd.timeline.apply(lambda x: x.split('-')[0])
    fd['years'] = fd.timeline.apply(lambda x: x.split('-')[1])
    print('transforming')
    result_json = fd.values.tolist()
    return result_json

def getUtility(service,SAMPLE_RANGE_NAME='Utility!A14:H21'):
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()
    print('loading util sheet')
    values = result.get('values', [])
    records = []
    if not values:
        print('No data found.')
    else:
        try:
            for row in values:
                records.append(row)
        except IndexError:
            print('end of rows')
        print('loaded values')
    filter_rec = [i for i in records if len(i) > 1]
    fd = pd.DataFrame(filter_rec)
    
    fd.columns = fd.loc[0].values
    fd.drop(0,inplace=True)
    fd['month'] = fd.timeline.apply(lambda x: x.split('-')[0])
    fd['years'] = fd.timeline.apply(lambda x: x.split('-')[1])
    result_json = fd.values.tolist()
    print('transformation done')
    return result_json
    

def getMonthlyLoans(service,SAMPLE_RANGE_NAME='MonthlyLoans!A19:B26'):
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()
    print('loaded monthly loans')
    values = result.get('values', [])
    records = []
    if not values:
        print('No data found.')
    else:
        try:
            for row in values:
                records.append(row)
        except IndexError:
            print('end of rows')
        print('loaded values')
    filter_rec = [i for i in records if len(i) > 1]
    fd = pd.DataFrame(filter_rec)
    fd.columns = fd.loc[0].values
    fd.drop(0,inplace=True)
    fd['month'] = fd.year.apply(lambda x: x.split('-')[0])
    fd['years'] = fd.year.apply(lambda x: x.split('-')[1])
    result_json = fd.values.tolist()
    print('transformation done')
    return result_json


def getDocuments(service,SAMPLE_RANGE_NAME='Documents!A2:C9'):
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()
    print('loaded documents')
    values = result.get('values', [])
    records = []
    if not values:
        print('No data found.')
    else:
        try:
            for row in values:
                records.append(row)
        except IndexError:
            print('end of rows')
        print('loaded data')
    filter_rec = [i for i in records if len(i) > 1]
    fd = pd.DataFrame(filter_rec)
    fd.columns = fd.loc[0].values
    print(fd.columns.values.tolist())
    fd.drop(0,inplace=True)
    fd['month'] = fd.year.apply(lambda x: x.split('-')[0])
    fd['years'] = fd.year.apply(lambda x: x.split('-')[1])
    result_json = fd.values.tolist()
    print('trandformation done')
    return result_json


def to_son(data,key):    
    lis=[]
    for i in data:        
        dic = {}           
        for k in range(len(key)):
            dic[key[k]]=i[k]
        lis.append(dic)
    return lis  