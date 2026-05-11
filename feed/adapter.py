
# first send request to 3rd party api
# get the data and extract relevant info
# store it in a dict and return
import json
import requests
import uuid

def fetch_data():
    reqres = 'https://reqres.in/api'
    url = 'https://reqres.in/api/users'
    headers  = {
        'x-api-key': 'reqres-free-v1'
    }
    response = requests.get(url,headers=headers)
    response.raise_for_status()
    data = response.json()
    return data
# def normalize_reqres(data):
#     resultData = data.get('data',{})[0]
#     first_name = resultData.get('first_name','')
#     last_name = resultData.get('first_name','')
#     return {
#         'user_id': str(uuid.uuid4()),
#         'full_name': first_name + '' + last_name,
#         'email':resultData.get('email',''),
#         'country':resultData.get('country',''),
#         'profile_picture':resultData.get('avatar',''),
#         'source' :'reqres'

#     }
import random
def normalize_reqres(data):
    resultData = data.get('data',[])
    # print(resultData)
    lens = random.randint(1,len(resultData)-1)
    results=  data.get('data',[])[lens]
    

    first_name = results.get('first_name','')
    last_name = results.get('last_name','')
    return {
            'user_id': str(uuid.uuid4()),
            'full_name': first_name + '' + last_name,
            'email':results.get('email',''),
            'country':results.get('country',''),
            'profile_picture':results.get('avatar',''),
            'source' :'resreq'

        }
