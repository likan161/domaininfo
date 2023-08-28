import json
from django.shortcuts import render
import socket
import requests
import re
from datetime import datetime,timedelta
import time

def emailInfoSearch(data, query):
  
    params = (
        ('query', '"{}" AND ("auth failed")'.format(query)),
        ('relative', '1209600'),
        ('fields', 'message'),
        ('width', '1680'),
    )
    auth = ("3mphvu7g4ntka9a8feenue2muai3uvhpudstekg6dvb518potfm", 'token')

    response = requests.get('http://10.216.129.70:12900/search/universal/relative',
                            params=params,
                          
                            auth=auth,
                            headers={'Accept': 'application/json',})

    messages = list()
    data_out = list()
    stri = ""

#https://log.corp.ps.kz/streams/572c565c453c6d4aa65343fe/search?rangetype=relative&fields=message%2Csource&width=1680&highlightMessage=&relative=1209600&q=%22ahanovich%40zakonipravo.kz%22+AND+auth+failed

#https://log.corp.ps.kz/streams/572c565c453c6d4aa65343fe/search?rangetype=relative&fields=message%2Csource&width=1680&highlightMessage=&relative=28800&q=%22ahanovich%40zakonipravo.kz%22+AND+auth+failed

    for msg in response.json()['messages']:
        messages.append('{} {}'.format(msg['message']['message'], msg['message']['timestamp']))
        email = re.findall("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", msg['message']['message'])
        if email:
            time1 = msg['message']['timestamp'].replace('T',' ').replace('.000Z','') + " GMT"
            time1 = datetime.strptime(time1, "%Y-%m-%d %H:%M:%S %Z") + timedelta(hours=6)# 2020-11-22 12:23:31
            stri = email[0] + " --- " + time1.strftime('%m-%d-%Y %H:%M')
            data_out.append(stri)
    data['AuthFailed'] = " <br /> ".join(data_out)

    return(data)

data={}
print(emailInfoSearch(data, "ahanovich@zakonipravo.kz"))
