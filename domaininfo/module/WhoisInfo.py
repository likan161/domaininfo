import whois
import sys
import re
sys.path.insert(0, 'domaininfo/module')
import htmlparser
import datetime
from itertools import groupby

def WhoisInfo(data, mail1):
    WhosiInfo = whois.whois(mail1)
    NS = WhosiInfo['name_servers']
    if NS:
        if NS:
            Status= WhosiInfo['status']
            if ('clientHold' in "".join(Status)):
                data['ClientHold']= True
            elif ('serverhold' in "".join(Status)):
                data['ServerHold']= True

            if ".com" in mail1[-4:]:
                data['CurentRegistrar']= WhosiInfo['registrar'] 
            elif ".ru" in mail1[-3:]:
                data['CurentRegistrar']= WhosiInfo['registrar']
            else:
                data['CurentRegistrar']= WhosiInfo['curent_registrar']
            try:
                data['Emails']= "".join(WhosiInfo['emails'])
            except:
                data['Emails']= "NoData"
            data['NSWhois']= " <br /> ".join(sorted(NS))
   
            if ".com" in mail1[-4:]:
                Status= " ".join(Status)
                Status = re.sub('\([^)]*\)', '', Status).replace('https://icann.org/epp#','').replace('http://www.icann.org/epp#','').replace('https://www.icann.org/epp#','')
                Status = set(Status.split())
                data['Status']= " <br /> ".join(sorted(Status))
            elif "status : ok" in Status:
                data['Status']= Status.replace('status :','')
            else:
                Status= " ".join(Status).replace('status :','')
                data['Status']= Status

            if ".kz" in mail1[-3:]:
                data['CreateDate']= WhosiInfo['creation_date'][:10]
            elif isinstance(WhosiInfo['creation_date'], list): 
                data['CreateDate']= WhosiInfo['creation_date'][0].strftime('%m-%d-%Y')
            else:
                data['CreateDate']= WhosiInfo['creation_date'].strftime('%m-%d-%Y')

            if "kz" in mail1[-3:]:
                htmlparser.htmlParser(data,mail1)
            elif isinstance(WhosiInfo['expiration_date'], list): 
                data['ExpirationDate']= WhosiInfo['expiration_date'][0].strftime('%m-%d-%Y')
            else:
                data['ExpirationDate']= WhosiInfo['expiration_date'].strftime('%m-%d-%Y')
            return(data)
    else:
        data['NSWhois']= False
        return(data)

#data = {}
#print(WhoisInfo(data,"lider-agency.kz"))
