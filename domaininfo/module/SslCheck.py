from OpenSSL import SSL
from cryptography import x509
from cryptography.x509.oid import NameOID
import idna
from datetime import datetime

import socket
#socket.setdefaulttimeout(1000)
from collections import namedtuple

HostInfo = namedtuple(field_names='cert hostname peername', typename='HostInfo')

def verify_cert(cert, hostname):
    cert.has_expired()

def get_certificate(hostname, port):
    hostname_idna = idna.encode(hostname)
    sock = socket.socket()

    #sock.settimeout(10)
    sock.connect((hostname, port))
    peername = sock.getpeername()
    ctx = SSL.Context(SSL.SSLv23_METHOD) # most compatible
    ctx.check_hostname = False
    ctx.verify_mode = SSL.VERIFY_NONE

    sock_ssl = SSL.Connection(ctx, sock)
    sock_ssl.set_connect_state()
    sock_ssl.set_tlsext_host_name(hostname_idna)
    sock_ssl.do_handshake()
    cert = sock_ssl.get_peer_certificate()
    crypto_cert = cert.to_cryptography()
    sock_ssl.close()
    sock.close()

    return HostInfo(cert=crypto_cert, peername=peername, hostname=hostname)

def get_alt_names(cert):
    try:
        ext = cert.extensions.get_extension_for_class(x509.SubjectAlternativeName)
        return ext.value.get_values_for_type(x509.DNSName)
    except x509.ExtensionNotFound:
        return None

def get_common_name(cert):
    try:
        names = cert.subject.get_attributes_for_oid(NameOID.COMMON_NAME)
        return names[0].value
    except x509.ExtensionNotFound:
        return None

def get_issuer(cert):
    try:
        names = cert.issuer.get_attributes_for_oid(NameOID.COMMON_NAME)
        return names[0].value
    except x509.ExtensionNotFound:
        return None

def print_basic_info(hostinfo):
    try:
        s = '''Имя сертификата: {commonname}
        \tДополнительные имена: {SAN}
        \tИздатель: {issuer}
        \tДата регистрации: {notbefore}
        \tДата истечения:  {notafter}
        '''.format(
                #commonname=''.join(get_common_name(hostinfo.cert)),
                #SAN=''.join(get_alt_names(hostinfo.cert)),
                commonname=''.join(get_common_name(hostinfo.cert)),
                SAN=''.join(get_alt_names(hostinfo.cert)),
                issuer=get_issuer(hostinfo.cert),
                notbefore=hostinfo.cert.not_valid_before,
                notafter=hostinfo.cert.not_valid_after
        )
    except:
        return(False)
    return s

def check_it_out(hostname, port):
    hostinfo = get_certificate(hostname, port)
    print_basic_info(hostinfo)




def CERT(data, mail1, port):
    try:
        Sert = get_certificate(mail1, port)
    except:
        return(data)
    
    ExpiriedDate = Sert.cert.not_valid_after
    data['ExpiriedDate'] = ExpiriedDate.strftime('%m-%d-%Y')

    IssuerName = get_issuer(Sert.cert)
    data['IssuerName'] = IssuerName

    if Sert.cert.not_valid_after < datetime.now():
        data['SertExpiried']= True
        ExpiresIn = Sert.cert.not_valid_after - datetime.now()
        data['ExpiresIn'] = ExpiresIn

#    SertName = get_common_name(Sert.cert)
#    SertAltName = ', '.join(get_alt_names(Sert.cert))
#    ReleaseDate = Sert.cert.not_valid_before
#    data['SertName']= SertName
#    data['SertAltName'] = SertAltName
#    data['ReleaseDate'] = ReleaseDate

    return(data)


#data = {}
#print(CERT(data,"ps.kz", 443))

