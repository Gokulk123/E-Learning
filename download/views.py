import os

from django.conf import settings
from django.core.files import File
from django.shortcuts import render,redirect
from django.apps import apps
from django.http import HttpResponse, Http404

#import the models from the django app project
from django.template import RequestContext

usersdata=apps.get_model('djangoapp', 'usersdata')

# Create your views here.

def login(request):
    return render(request,'login.html',{})

def authenticate_and_download(request):
    from cryptography.fernet import Fernet
    import os
    from django.conf import settings
    from django.http import HttpResponse, Http404
    #read the form data
    file_password = request.POST.get('file_password')
    file_name = request.POST.get('file_name')
    user_id = request.POST.get('user_id')
    username = request.POST.get('username')
    password = request.POST.get('password')

    #select the userdata
    x = usersdata.objects.get(id=int(user_id))

    if x.username == username  and x.password == password and x.id == int(user_id):
        request.session['username'] = x.username

        try:
            from cryptography.fernet import Fernet
            key = file_password
            filename = file_name

            cipher = Fernet(key)

            with open(filename, 'rb') as df:
                encrypted_data = df.read()
                
            decrypted_file = cipher.decrypt(encrypted_data)

            with open(filename, 'wb') as df:
                df.write(decrypted_file)
            return render(request, 'download.html', {'filename': file_name})
        except Exception as e:
            print(e)



