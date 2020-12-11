from django.urls import path,include
from . import views
urlpatterns=[
    path("",views.home,name="home"),
    path("login-/",views.loginpage,name="login"),
    path("register-/",views.register,name="register"),
    path("logout/",views.logoutuser,name="logout"),
    path("<str:formation>/creat-squad/",views.creat_squad,name="creat_squad"),
    path("display_squad/",views.display_squad,name="display_squad"),
    path("savelist/",views.savelist,name="savelist"),
    path('save/',views.save,name="save"),
    path('save_names/',views.save_names,name="save_names"),
    path("<str:sname>/display/",views.savelist_display,name="savelist_display"),
    path('delete/',views.delete,name="delete"),

]