from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    #path('login/', views.login_user, name='login'), Use if want to create seperate login page 
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('record/<int:pk>', views.user_record, name='record'),
    path('delete_record/<int:pk>', views.delete_record, name='delete_record'),
    path('add_record/', views.add_record, name='add_record'),
    path('update_record/<int:pk>', views.update_record, name='update_record'), # pk as the primary key (ID), gets int
    path('search_records/', views.search_records, name='search_records'),
]
