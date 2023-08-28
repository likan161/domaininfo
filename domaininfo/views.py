import sys
sys.path.insert(0, 'domaininfo/module')
from django.http import HttpResponse
from django import forms
from django.shortcuts import render
import re
import threading
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

class NameForm(forms.Form):
        mail1 = forms.CharField(max_length=50)
        mail2 = forms.CharField(max_length=50,required=False)

@csrf_exempt
def get_form(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            mail1= form.cleaned_data.get("mail1")
            mail2= form.cleaned_data.get("mail2")

            data = {"otvet":  True, "mail1": mail1}

            email = re.findall("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", mail1)
            if email:
                import email_check
                email_check.emailInfoSearch(data, mail1)
                return render(request,'email.html', context=data)

            import DNS
            DnsThread = threading.Thread(target=DNS.DNS, args=(data,mail1))
            DnsThread.daemon = True
            
            if not mail2:
                import WhoisInfo
                WhoisThread = threading.Thread(target=WhoisInfo.WhoisInfo, args=(data,mail1))
                WhoisThread.daemon = True

                import SslCheck
                SertThread = threading.Thread(target=SslCheck.CERT, args=(data,mail1,443))
                SertThread.daemon = True
            
            import MXCheck                     
            MXCheckThread = threading.Thread(target=MXCheck.MXCheck, args=(data,mail1))
            MXCheckThread.daemon = True

            import HostingType
            HostingTypeThread = threading.Thread(target=HostingType.HostingType, args=(data,mail1))
            HostingTypeThread.daemon = True


            if not mail2:
                WhoisThread.start()
                SertThread.start()
            MXCheckThread.start()
            HostingTypeThread.start()
            DnsThread.start()


            HostingTypeThread.join()
            DnsThread.join()
            MXCheckThread.join()
            if not mail2:
                SertThread.join(timeout=2)
                WhoisThread.join()


            if mail2 == "V1.4" and mail1 == "love":
                return render(request,'veronika.html', context=data)
            elif mail2 == "V1.4":
                return render(request,'expansion.html', context=data)
            elif mail2:
                return render(request,'expansionupdate.html')
            else:
                return render(request,'index.html', context=data)

        else:
            data = {"otvet":  False}
            return render(request,'index.html', context=data)
    else:
         return render(request,'index.html')
