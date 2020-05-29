"""djangoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .djangoapp import views
from .download import views as downloadview
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('userReg/', views.userReg, name="userReg"),
    path('facultyReg/', views.facultyReg, name="facultyReg"),
    path('userlogin/', views.userlogin, name="userlogin"),
    path('facultylogin/', views.facultylogin, name="facultylogin"),
    path('adminlogin/', views.adminlogin, name="adminlogin"),
    path('about/', views.about, name="about"),
    path('userregistration/', views.usersignup, name="usersignup"),
    path('facultyregistration/', views.facultysignup, name="facultysignup"),
    path('admincredential/', views.admincredentialauth, name="admincredentialauth"),
    path('userdetails/',views.userdetails,name="userdetails"),
    path('adminhome/',views.adminhome,name="adminhome"),
    path('userhome/',views.userhome,name="userhome"),
    path('facultyhome/',views.facultyhome,name="facultyhome"),
    path('facultydetails/',views.facultydetails,name="facultydetails"),
    path('logout/',views.logout,name="logout"),
    path('admincredential/',views.usercredentialauth,name="usercredentialauth"),
    path('add_courses/',views.add_course,name="add_course"),
    path('add_course_materials/',views.add_course_materials,name="add_course_materials"),
    path('select_course/',views.select_course,name="select_course"),
    path('select_course_materials/',views.select_course_materials,name="select_course_materials"),
    path('ask_question/',views.ask_question,name="ask_question"),
    path('view_reply/',views.view_reply,name="view_reply"),
    path('view_question/',views.view_question,name="view_question"),
    path('responsing/',views.responsing,name="responsing"),
    path('usercredential/', views.usercredentialauth, name="usercredentialauth"),
    path('userlogout/',views.userlogout,name="userlogout"),
    path('facultycredential/', views.facultycredentialauth, name="facultycredentialauth"),
    path('facultylogout/',views.facultylogout,name="facultylogout"),
    path('add_values/',views.add_values,name="add_values"),
    path('assign_course/',views.assign_course,name="assign_course"),
    path('course_value/',views.course_value,name="course_value"),
    path('view_course/',views.view_course,name="view_course"),
    path('ask_question/',views.ask_question,name="ask_question"),
    path('save_doubts/',views.save_doubts,name="save_doubts"),
    path('view_assigned_courses/', views.view_assigned_courses, name="view_assigned_courses"),
    path('view_users_doubts/', views.view_users_doubts, name="view_users_doubts"),
    path('reply/', views.reply, name="reply"),
    path('save_reply/', views.save_reply, name="save_reply"),
    path('all_reply/', views.all_reply, name="all_reply"),
    path('view_solution/', views.view_solution, name="view_solution"),
    path('add_materials/', views.add_materials, name="add_materials"),
    path('generateKey/', views.generateKey, name="generateKey"),
    path('material_save/', views.material_save, name="material_save"),
    path('add_email/', views.add_email, name="add_email"),
    path('send_mail/', views.send_mail, name="send_mail"),
    path('read_keys/', views.read_keys, name="read_keys"),
    path('login/', downloadview.login, name="login"),
    path('downloadresoure/',downloadview.authenticate_and_download,name="authenticate_and_download"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)