from django.urls import path, include
from .views import home, dashboard, addpost, editpost, updatepost, deletepost, published, unpublished
# app_name = 'coreapp'

urlpatterns = [
    path('', home, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
    path('addpost/', addpost, name='addpost'),
    path('editpost/<str:id>/', editpost, name='editpost'),
    path('updatepost/<str:id>/', updatepost, name='updatepost'),
    path('deletepost/<str:id>/', deletepost, name='deletepost'),
    
    path('published/<str:id>/', published, name='published'),
    path('unpublished/<str:id>/', unpublished, name='unpublished'),
   

]
