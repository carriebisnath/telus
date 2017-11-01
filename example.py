# https://developers.google.com/api-client-library/python/
# Copyright 2017 Google Inc. All Rights Reserved.
__author__ = [
  'jonrburns@google.com (Jon Burns)'
]

# PPrint Output
import pprint

# API Import
from apiclient import discovery

# Oauth Import
from oauth2client.client import AccessTokenCredentials

def get_user_profile_ids(auth_https):
  """
  Get list of user profiles
  Args    
    auth_https: Oauth Authenticated HTTP Handler
  :return:  list of user profiles  
  """

  # Create Service
  service = discovery.build("dfareporting", "v2.8", http=auth_https)

  # Make Request - https://developers.google.com/apis-explorer/#p/dfareporting/v2.8/dfareporting.userProfiles.list
  profiles = service.userProfiles().list()
  result = profiles.execute()

  # Return result
  return result


def get_dcm_reports(profile_id, auth_https):
  """
  Get list of DCM Reports
  Args
    profile_id: DCM Profile Id
    auth_https: Oauth Authenticated HTTP Handler
  :return: Report Dict
  """

  # Create service
  service = discovery.build("dfareporting", "v2.8", http=auth_https)

  # Make Request - https://developers.google.com/apis-explorer/#p/dfareporting/v2.8/dfareporting.reports.list
  reports = service.reports().list(
      profileId=profile_id,
      sortField='LAST_MODIFIED_TIME',
      sortOrder='DESCENDING',
      fields='items(accountId,fileName,format,id,lastModifiedTime,name,schedule,type)'
  )
  result = reports.execute()

  # Return result
  return result


# Load token.json file
oauth_token_json = open('token.json', 'r')

# Authorize https request
https = discovery.httplib2.Http()
credential = AccessTokenCredentials.new_from_json(oauth_token_json.read())
auth_https = credential.authorize(https)

# Get response
response = get_user_profile_ids(auth_https)

# Print response
pprint.pprint(response)