from django.urls import path
from WebApp import views

urlpatterns = [
    path('',views.home_page,name='Home'),
    path('About/',views.about_page,name='About'),
    path('Contact/',views.contact_page,name='Contact'),
    path('OurProduct/',views.ourproduct,name='OurProduct'),
    path('save_contact/',views.save_contact,name='save_contact'),
    path('filter_products/<cat_name>/',views.filter_products,name='filter_products'),
    path('single_product/<int:pro_id>/',views.single_product,name='single_product'),
    path('registration_page',views.registration_page,name='registration_page'),
    path('save_register',views.save_register,name='save_register'),
    path('Userlogin',views.Userlogin,name='Userlogin'),
    path('User_logout',views.User_logout,name='User_logout'),
    path('save_cart',views.save_cart,name='save_cart'),
    path('cart_page',views.cart_page,name='cart_page'),
    path('delete_item/<int:cart_id>/',views.delete_item,name='delete_item'),
    path('user_login_page/',views.user_login_page,name='user_login_page'),

]