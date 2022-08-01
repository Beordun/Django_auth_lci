from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login_api),
    path('user/', views.get_user_data),
    path('register/', views.get_user_data),
    #path('logout/', views.logout_api),
]