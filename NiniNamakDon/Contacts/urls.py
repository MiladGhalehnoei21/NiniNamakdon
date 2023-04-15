

from django.urls import path, include
from . import views

app_name = 'Contacts'
urlpatterns = [

    path('', views.ContactList),
    path('<int:Contact_id>/', views.ContactListDitel),


]
