
from ipwhois import IPWhois
import pydig
import socket
import re
import whois

def DNS(data,mail1):
    if  bool(re.search('[а-яА-Я]', mail1)):
        mail1 = whois.whois(mail1)['domain_name']

    IPv4 = pydig.query(mail1, 'A')

    if IPv4:
        NS = ", ".join(pydig.query(mail1, 'NS'))
        SOA = ", ".join(pydig.query(mail1, 'SOA'))

        ipwhois = IPWhois(IPv4[0])
        data['MyBarin'] = ipwhois.lookup_rdap()['asn_description']

        if "support.ps.kz" in SOA:
            if "ns2.ps.kz" in NS or "ns1.ps.kz" in NS or "ns.ps.kz" in NS:
                data['PowerDNS'] = True
        else:
            data['PowerDNS'] = False
        try:
            data['HostName'] = socket.gethostbyaddr(IPv4[0])[0]
        except:
            data['HostName'] = False

        data['IPv4'] = " <br /> ".join(sorted(IPv4))
        data['IPv6'] = " <br /> ".join(sorted(pydig.query(mail1, 'AAAA')))
        data['MX'] = " <br /> ".join(sorted(pydig.query(mail1, 'MX')))
        data['NS'] = NS
        data['SOA'] = SOA
        return(data)
    else:
        data['IPv4'] = False
        return(data)


data = {}
DNS(data,"lider-agency.kz")
print(data)
