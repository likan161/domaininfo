
import ipaddress
import pydig


def HostingType(data,mail1):
    ip = ipaddress.ip_address(pydig.query(mail1, 'A')[0])
    if ip == ipaddress.ip_address('195.210.46.121'):
        data['HostingType'] = "конструктора"
        return(data)
    elif ip == ipaddress.ip_address('195.210.46.115'):
        data['HostingType'] = "сервера редиректа"
        return(data)
    elif ip in ipaddress.ip_network('195.210.46.0/25'):
        data['HostingType'] = "виртуального хостинга"
        return(data)
    elif ip in ipaddress.ip_network('195.210.46.0/25'):
        data['HostingType'] = "VPS хостинга"
        return(data)
    elif ip in ipaddress.ip_network('195.210.47.0/24'):
        data['HostingType'] = "VPS хостинга"
        return(data)
    elif ip in ipaddress.ip_network('195.93.152.64/26'):
        data['HostingType'] = "VPS хостинга"
        return(data)
    elif ip in ipaddress.ip_network('195.93.152.64/26'):
        data['HostingType'] = "VPS хостинга"
        return(data)
    elif ip in ipaddress.ip_network('185.146.3.0/24'):
        data['HostingType'] = "VPS хостинга"
        return(data)
    elif ip in ipaddress.ip_network('185.146.1.0/25'):
        data['HostingType'] = "VPS хостинга"
        return(data)
    elif ip in ipaddress.ip_network('185.22.67.0/25'):
        data['HostingType'] = "VPS хостинга"
        return(data)
    elif ip in ipaddress.ip_network('94.247.128.128/25'):
        data['HostingType'] = "VPS хостинга"
        return(data)
    elif ip in ipaddress.ip_network('91.201.215.192/26'):
        data['HostingType'] = "VPS хостинга"
        return(data)
    elif ip in ipaddress.ip_network('91.201.215.128/26'):
        data['HostingType'] = "VPS хостинга"
        return(data)
    elif ip in ipaddress.ip_network('91.201.215.0/26'):
        data['HostingType'] = "VPS хостинга"
        return(data)
    elif ip in ipaddress.ip_network('91.201.214.128/25'):
        data['HostingType'] = "VPS хостинга"
        return(data)
    elif ip in ipaddress.ip_network('89.219.32.0/25'):
        data['HostingType'] = "VPS хостинга"
        return(data)
    elif ip in ipaddress.ip_network('78.40.109.0/24'):
        data['HostingType'] = "VPS хостинга"
        return(data)
