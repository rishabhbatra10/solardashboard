# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 12:57:56 2018

@author: Rishabh Batra
"""

from django.urls import path

from . import views

app_name='dashboard'
urlpatterns = [
            path('', views.index, name='index'),
            path('test/', views.test, name='test'),
            #path('', views.initialize, name='initialize'),
        ]