from django.conf.urls import url

from . import views

app_name = 'contactBook'
urlpatterns = [
    url(r'^addcontact/$', views.AddContact.as_view()),
    url(r'^editcontact/$', views.EditContact.as_view()),
    url(r'^deletecontact/$', views.DeleteContact.as_view()),
    url(r'^searchcontact/$', views.SearchContact.as_view()),
    url(r'^searchcontactbyname/$', views.SearchContactByName.as_view()),
    url(r'^deletecontactbyemail/$', views.SearchContactByEmail.as_view()),
]