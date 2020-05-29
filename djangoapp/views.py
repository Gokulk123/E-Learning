from django.contrib.sessions.models import Session
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import usersdata
from .models import admindata
from .models import facultydata
from .models import courses
from .models import assign_work
from .models import ask_doubts
from .models import add_reply
from .models import materials
from django.http import JsonResponse, HttpResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage
# Create your views here.
def index(request):
    return render(request,'index.html',{})

def userReg(request):
    return render(request,'userregistration.html')

def facultyReg(request):
    return render(request,'facultyReg.html')

def userlogin(request):
    return render(request,'userlogin.html')

def facultylogin(request):
    return render(request,'facultylogin.html')

def adminlogin(request):
    return render(request,'adminlogin.html')

def about(request):
    return render(request,'about.html')
def adminhome(request):
    return render(request,'adminhome.html')
def userhome(request):
    return render(request,'userhome.html')
def facultyhome(request):
    return render(request,'facultyhome.html')
def add_course(request):
    return render(request,'add_course.html')
def add_course_materials(request):
    return render(request,'add_course_materials.html')
def select_course(request):
    return render(request,"select_course.html")
def select_course_materials(request):
    return render(request,"select_course_materials.html")
def view_reply(request):
    return render(request,'view_reply.html')
def view_question(request):
    return render(request,'view_question.html')
def responsing(request):
    return render(request,'responsing.html')
def usersignup(request):
    db = usersdata(fname=request.POST.get('fname'),
                      lname=request.POST.get('lname'),
                      dob=request.POST.get('date'),
                      gender=request.POST.get('gender'),
                      street=request.POST.get('street'),
                      hname=request.POST.get('hname'),
                      district=request.POST.get('district'),
                      state=request.POST.get('state'),
                      pincode=request.POST.get('pincode'),
                      email=request.POST.get('email'),
                      phone=request.POST.get('phone'),
                      username=request.POST.get('username'),
                      password=request.POST.get('password'))
    db.save()
    messages.success(request, 'Registration successfully.')
    return render(request,'userregistration.html')

def facultysignup(request):
    db = facultydata(fname=request.POST.get('fname'),
                   lname=request.POST.get('lname'),
                   dob=request.POST.get('date'),
                   gender=request.POST.get('gender'),
                   ed=request.POST.get('ed'),
                   spe=request.POST.get('spe'),
                   street=request.POST.get('street'),
                   hname=request.POST.get('hname'),
                   district=request.POST.get('district'),
                   state=request.POST.get('state'),
                   pincode=request.POST.get('pincode'),
                   email=request.POST.get('email'),
                   phone=request.POST.get('phone'),
                   username=request.POST.get('username'),
                   password=request.POST.get('password'))
    db.save()
    messages.success(request, 'Registration successfully.')
    return render(request, 'facultyReg.html')


def admincredentialauth(request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        ad = admindata.objects.all()
        for x in ad:
            if x.username == username and x.password == password:
                request.session['username'] = x.username
                # user = authenticate(request, username=username, password=password)
                # login(request, user)
                return render(request, 'adminhome.html', {'username': x.username})
        return render(request, 'adminlogin.html', {'msg': "Incorrect username or password.Try again"})

def usercredentialauth(request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        ad = usersdata.objects.all()
        for x in ad:
            if x.username == username and x.password == password:
                request.session['username'] = x.username
                # user = authenticate(request, username=username, password=password)
                # login(request, user)
                return render(request, 'userhome.html', {'username': x.username})
        return render(request, 'userlogin.html', {'msg': "Incorrect username or password.Try again"})

def facultycredentialauth(request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        ad = facultydata.objects.all()
        for x in ad:
            if x.username == username and x.password == password:
                request.session['username'] = x.username
                # user = authenticate(request, username=username, password=password)
                # login(request, user)
                return render(request, 'facultyhome.html', {'username': x.username})
        return render(request, 'facultylogin.html', {'msg': "Incorrect username or password.Try again"})







def userdetails(request):
    users = usersdata.objects.all()
    return render(request, 'userdetails.html', {'users':users})

def facultydetails(request):
    users = facultydata.objects.all()
    return render(request, 'facultydetails.html', {'users':users})

def logout(request):

    try:
        ss = Session.objects.all().delete()
        ss.save()
        request.session['username'].delete()
        del request.session['pass']
    except:
        pass
        return render(request, 'adminlogin.html')
def userlogout(request):
    try:
        ss = Session.objects.all().delete()
        ss.save()
        request.session['username'].delete()
        del request.session['pass']
    except:
        pass
        return render(request, 'userlogin.html')
def facultylogout(request):
    try:
        ss = Session.objects.all().delete()
        ss.save()
        request.session['username'].delete()
        del request.session['pass']
    except:
        pass
        return render(request, 'facultylogin.html')


def add_values(request):
    db = courses(course_name=request.POST.get('course'),Description=request.POST.get('des'))
    db.save()
    messages.success(request, 'Course Adding  successfully.')
    return render(request,'add_course.html')


def assign_course(request):
    course = courses.objects.all()
    facu = facultydata.objects.all()
    return render(request,'assign_course.html',{'course':course,'facu':facu})

def course_value(request):
    db = assign_work(faculty=request.POST.get('faculty'),course_id=request.POST.get('course'))
    db.save()
    messages.success(request, 'Work Assigned successfully.')
    return render(request,'assign_course.html')

def view_course(request):
    u_name = request.session['username']
    user = usersdata.objects.get(username=u_name)
    course = courses.objects.all()
    material = materials.objects.all()
    return render(request, 'view_course.html',{'course':course,'material':material,'user':user})

def ask_question(request):
    u_name=request.session['username']
    user = usersdata.objects.get(username=u_name)
    course = courses.objects.all()
    return render(request,'ask_question.html',{'user':user,'course':course})

def save_doubts(request):
    u_name = request.session['username']
    user = usersdata.objects.get(username=u_name)
    course = courses.objects.all()
    db = ask_doubts(u_id=request.POST.get('uid'),course_name=request.POST.get('course'),date=request.POST.get('date'),question=request.POST.get('ques'))
    db.save()
    messages.success(request, 'Doubts Added successfully.')
    return render(request,'ask_question.html',{'user':user,'course':course})

def view_assigned_courses(request):
    u_name=request.session['username']
    faculty = facultydata.objects.get(username=u_name)
    course = assign_work.objects.get(faculty=faculty.id)
    value = courses.objects.get(id=course.course_id)
    return render(request,'view_assigned_courses.html',{'value':value})


def view_users_doubts(request):
    doubts = ask_doubts.objects.all()
    return render(request, 'view_users_doubts.html',{'doubts':doubts})

def reply(request):
    u_id = request.POST.get('uid')
    c_name = request.POST.get('c_name')
    ques = request.POST.get('ques')
    #doubts = ask_doubts.objects.filter(u_id=uid)
    return render(request, 'reply.html',{'uid':u_id,'c_name':c_name,'ques':ques})



def save_reply(request):

    db = add_reply(u_id=request.POST.get('uid'),course_name=request.POST.get('course'),question=request.POST.get('ques'),reply=request.POST.get('reply'))
    db.save()
    messages.success(request, 'Reply Added successfully.')
    return render(request,'reply.html',{'uid':request.POST.get('uid'),'c_name':request.POST.get('course'),'ques':request.POST.get('ques')})


def all_reply(request):
    reply = add_reply.objects.all()
    return render(request, 'all_reply.html',{'reply':reply})


def view_solution(request):
    u_name=request.session['username']
    user = usersdata.objects.get(username=u_name)
    re = add_reply.objects.filter(u_id=user.id)
    return render(request,'view_solution.html',{'result':re})


def add_materials(request):
    course = courses.objects.all()
    return render(request, 'add_materials.html', {'course': course})

def generateKey(request):
    import base64
    from cryptography.hazmat.backends import default_backend
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

    pass_from_user = request.GET.get('plain')
    password = pass_from_user.encode()

    mysalt = b'q\xe3Q5\x8c\x19~\x17\xcb\x88\xc6A\xb8j\xb4\x85'

    kdf = PBKDF2HMAC(

        algorithm=hashes.SHA256,
        length=32,
        salt=mysalt,
        iterations=100000,
        backend=default_backend()

    )

    key = base64.urlsafe_b64encode(kdf.derive(password))
    generated_key={"key":key.decode()}
    return JsonResponse(generated_key, safe=False)


def material_save(request):
    from cryptography.fernet import Fernet
    key = request.POST.get('Generated_key')
    if request.method == 'POST' and request.FILES['mat']:
        uploaded_file = request.FILES['mat']
        fs = FileSystemStorage()
        fname = uploaded_file.name
        filename = fs.save(fname, uploaded_file)
        uploaded_file_url = fs.url(filename)


        cipher = Fernet(key)
        with open('media/'+filename, 'rb') as f:
            e_file = f.read()

        encrypted_file = cipher.encrypt(e_file)


        with open('media/'+filename, 'wb') as ef:
            ef.write(encrypted_file)

        write_keys('media/'+filename, key)

        db = materials(materials='media/'+filename, course_id=request.POST.get('course'))
        db.save()
        #material = materials.object.last('id')
    course = courses.objects.all()
    return render(request, 'add_materials.html', {'course': course,'msg':'Successfully Uploaded.'})


def add_email(request):
    material_id = request.GET.get('id')
    user_id = request.GET.get('u_id')
    material_name = request.GET.get('material_name')
    return render(request, 'add_email.html', {'material_id':material_id,'u_id':user_id,'material_name':material_name})

def send_mail(request):
    material_id = request.POST.get('m_id')
    user_id = request.POST.get('u_id')
    material_name = request.POST.get('material_name')
    material_keys=read_keys(material_name)
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    import smtplib

    # create message object instance
    msg = MIMEMultipart()



    # setup the parameters of the message
    password = "7736483306"
    msg['From'] = "gokulkrishnanml@gmail.com"
    msg['To'] = request.POST.get('email')
    msg['Subject'] = "E - Learning Secure Portal"
    message = 'You have authenticated for downloading a file. \n\n ' \
                     'File name: ' + material_name + ' \n\n ' \
                     ' Please click on the following URL for the file.' \
                     '\n\t http://127.0.0.1:8000/login/?user_id=' + user_id + \
                     '&name=' + material_name + '&id=' + material_keys + \
                     '\n\t\t\t E - Learning'

    # add in the message body
    msg.attach(MIMEText(message, 'plain'))

    # create server
    server = smtplib.SMTP('smtp.gmail.com: 587')

    server.starttls()

    # Login Credentials for sending the mail
    server.login(msg['From'], password)

    # send the message via the server.
    server.sendmail(msg['From'], msg['To'], msg.as_string())

    server.quit()

    print("successfully sent email to %s:" % (msg['To']))

    return render(request, 'add_email.html', {'material_id':material_id,'user_id':user_id,'material_name':material_name,'msg':'Successfully Send Mail.'})

def write_keys(key,value):
    import pickle
    try:
        pickle_file = open ("keys.pickle", "rb")
        keys = dict()
        while 1:
            try:
                keys=pickle.load(pickle_file)
            except EOFError:
                break
        try:
            keys[key]=value
        except KeyError:
            print("Key duplication")
        pickle_file.close()
        pickle_file = open ("keys.pickle", "wb")
        pickle.dump(keys, pickle_file)
        pickle_file.close()
    except FileNotFoundError:
        print("This is the first pickling opertation")
        pickle_file = open ("keys.pickle", "wb")
        keys={key:value}
        pickle.dump(keys, pickle_file)
        pickle_file.close()
    return None


def read_keys(material_name):
    import pickle
    pickle_file = open ("keys.pickle", "rb")
    content = pickle.load(pickle_file)
    encryption_key=None
    for key in content:
            print((key)," : ",material_name,(key==material_name))
            encryption_key=content[key]
    return encryption_key