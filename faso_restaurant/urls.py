from django.contrib import admin
from django.urls import path,include
import faso_restaurant.views
#
urlpatterns = [
    path('',faso_restaurant.views.home,name='home')

]
