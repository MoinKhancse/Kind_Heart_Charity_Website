from django.urls import path
from adminpanel import views

urlpatterns = [
    path('admin',views.index, name='admin'),
    path('login',views.login_page, name='login_page'),
    path('reg',views.reg_page,name='reg_page'),
    path('logout_user',views.logout_page, name='logout_user'),
    path('add_slider',views.create_slider, name='add_slider'),
    path('delete/<int:id>',views.delete, name='delete'),
    path('edit/<int:id>/',views.edit, name='edit'),
    # path('update/<int:id>',views.update,name='update'),

]
