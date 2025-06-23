from django.urls import path
from . import views

urlpatterns = [
    path('',views.Homeindex,name='Homeindex'),
    path('about/',views.about,name='about'),
    path('booking/',views.Booking,name='booking'),
    path('reserve/',views.Reserve,name='reserve'),
    path('venues/',views.venues,name='venues'),
    # path('weddings/',views.book_weddings,name='weddings'),
    path('weddings/', views.book_weddings, name='weddings'), 
    path('contact/',views.contact,name='contact'),
    path('service/',views.service,name='service'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('musical/', views.musical, name='musical'),
    path('parties/', views.parties, name='parties'),
    path('corporate/', views.corporate, name='corporate'),
    path('myfile/', views.myfile, name='myfile'),
    path('allweddings/', views.allweddings, name='allweddings'),
    # path('user-form/', views.user_form_view, name='user-form'),
    path('form_success/', views.form_success, name='form_success'),
    path('create/', views.create, name='create'),
    path('Servicemain/', views.service_page, name='Servicemain'),
    path('book/<int:event_id>/', views.book_event, name='book_event'),
     path('suggest/', views.suggestion_view, name='suggest'),
   

]