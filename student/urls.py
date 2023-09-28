
from django.urls import path
from student import views


urlpatterns = [
    path('',views.home, name='home'),
    path('add_student/',views.add_student, name='add_student'),
    path('delete_student/<str:id>',views.delete_student, name='delete_student'),
    path('update_student/<str:id>',views.update_student, name='update_student'),
    
    path('signup/',views.signup_page, name='signup'),
    path('login/',views.login_page, name='login'),
    path('logout/',views.logout_page, name='logout'),
]


