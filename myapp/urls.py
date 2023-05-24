from django.urls import path
from .views import *
urlpatterns = [
    path('get_data/<int:pk>',Getdata.as_view(),name='get_data'),
    path('create_data/',Createdata.as_view(),name='create_data'),
    path('update_data/<int:pk>',Updatedata.as_view(),name='update_data'),
    path('delete_data/<int:pk>',Deletedata.as_view(),name='delete_data'),

]