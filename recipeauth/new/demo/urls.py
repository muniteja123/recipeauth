from django.urls import path
from demo import views

app_name = "demo"

urlpatterns = [
    path("home/",views.home, name='home'),
    path("details/<int:recipe_id>/",views.details,name='details'),
    path("process/",views.process,name='process'),
    path("reg/",views.reg,name='reg'),
    path("",views.login_info,name='login'),
    path("validate/",views.validate,name='validate'),
    path("logout/",views.logout_info,name='logout'),
]




