from django.urls import path
from webpage import views

app_name ='webpage'

urlpatterns=[
  path('register/',views.register,name='register'),
  path('user_login/',views.user_login,name='user_login')
]
