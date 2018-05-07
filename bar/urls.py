from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views


urlpatterns=[   
    url(r'^api/barstaff/$', views.StaffList.as_view()),
    url(r'^api/barwaiter/$', views.WaitersList.as_view()),
    url(r'^api/barorder/$', views.OrdersList.as_view()),
    url(r'^api/baritem/$', views.ItemsList.as_view()),

]