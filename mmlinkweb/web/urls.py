from django.urls import path

from .import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('plan', views.plan, name='plan'),
    path('feature', views.feature, name='feature'),
    path('form', views.form, name='form'),
    path('complain', views.complain, name='complain'),
    path('newinstallation', views.newinstallation, name='newinstallation'),
    path('billing', views.billing, name='billing'),
    path('contact', views.contact, name='contact'),
    # path('message', views.contact, name='contact'),
    
]