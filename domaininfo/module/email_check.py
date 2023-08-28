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
        ('range', 10000),
        ('fields', 'message'),
        ('limit', 2000)
    )
    auth = ("3mphvu7g4ntka9a8feenue2muai3uvhpudstekg6dvb518potfm", 'token')

    response = requests.get('http://10.216.129.70:12900/search/universal/relative',
                            params=params,
                          
                            auth=auth,
                            headers={'Accept': 'application/json',})

    messages = list()
    data_out = list()
    stri = ""



    for msg in response.json()['messages']:
        messages.append('{} {}'.format(msg['message']['message'], msg['message']['timestamp']))
        email = re.findall("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", msg['message']['message'])
        if email:
            time1 = msg['message']['timestamp'].replace('T',' ').replace('.000Z','') + " GMT"
            time1 = datetime.strptime(time1, "%Y-%m-%d %H:%M:%S %Z") + timedelta(hours=6)# 2020-11-22 12:23:31
            stri = "Неверные логин/пароль " + email[0] + " " + " в " + time1.strftime('%m-%d-%Y %H:%M')
            if stri not in data_out:
                data_out.append(stri)
            if len(data_out) > 22 :
                break
    data['AuthFailed'] = " <br /> ".join(data_out)

    return(data)

#data={}
#print(emailInfoSearch(data, "ps.kz"))
