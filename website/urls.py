from django.urls import path
from website import views

urlpatterns = [
    path('',views.index, name='home'),
    # path('',views.message,name='message')
]
