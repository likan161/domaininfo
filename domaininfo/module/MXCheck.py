from ipwhois import IPWhois
import pydig


def MXCheck(data,mail1):
    MX = " ".join(pydig.query(mail1, 'MX'))

    if "mx.yandex.net" in MX:
        data['MXOwner'] = "Yandex"
        return(data)
    if "aspmx.l.google.com" in MX:
        data['MXOwner'] = "Google"
        return(data)
    elif "emx.mail.ru" in MX:
        data['MXOwner'] = "Mail.ru"
        return(data)

    Per = "mail." + mail1
    if Per in MX:
        MXIP = pydig.query(Per, 'A')
        MXWhois = IPWhois(MXIP[0])
        MXOwner = MXWhois.lookup_rdap()['asn_description']
        if MXOwner == "PS, KZ":
            data['MXOwner'] = "PS.kz"
            return(data)

    if MX:
        MXIP = pydig.query(MX, 'A')
        MXWhois = IPWhois(MXIP[0])
        MXOwner = MXWhois.lookup_rdap()['asn_description']
        data['MXOwner'] = MXOwner
        return(data)

#data = {}
#print(MXCheck(data,"ges.kz"))
