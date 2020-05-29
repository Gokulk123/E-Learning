from django.db import models

# Create your models here.



class usersdata(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=20)
    street = models.CharField(max_length=20, default='SOME STRING')
    hname = models.CharField(max_length=20, default='SOME STRING')
    district = models.CharField(max_length=50, default='SOME STRING')
    state = models.CharField(max_length=20, default='SOME STRING')
    pincode = models.CharField(max_length=20, default='SOME STRING')

    email = models.EmailField()
    phone = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


class facultydata(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=20)
    ed = models.CharField(max_length=20)
    spe = models.CharField(max_length=20)
    street = models.CharField(max_length=20, default='SOME STRING')
    hname = models.CharField(max_length=20, default='SOME STRING')
    district = models.CharField(max_length=50, default='SOME STRING')
    state = models.CharField(max_length=20, default='SOME STRING')
    pincode = models.CharField(max_length=20, default='SOME STRING')

    email = models.EmailField()
    phone = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class admindata(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class courses(models.Model):
    course_name = models.CharField(max_length=100)
    Description = models.CharField(max_length=2000,default='SOME STRING')

class materials(models.Model):
    materials = models.FileField()
    course_id = models.IntegerField(max_length=100)

class assign_work(models.Model):
    faculty = models.CharField(max_length=100)
    course_id = models.CharField(max_length=100)

class ask_doubts(models.Model):
    u_id = models.CharField(max_length=100)
    course_name = models.CharField(max_length=100)
    date = models.DateField()
    question = models.CharField(max_length=100)

class add_reply(models.Model):
    u_id = models.CharField(max_length=100)
    course_name = models.CharField(max_length=100)
    question = models.CharField(max_length=100)
    reply = models.CharField(max_length=100)




