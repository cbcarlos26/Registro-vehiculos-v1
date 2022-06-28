from django.urls import path
from usuarios.views import login_user, logout_user

#Here the links are linked with a function that respond a request
urlpatterns = [
    path('', login_user, name='login'),
    path('logout_user', logout_user, name='logout'),
]