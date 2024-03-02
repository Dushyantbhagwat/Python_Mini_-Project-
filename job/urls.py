from django.urls import path
from . import views

urlpatterns = [
    path('', views.LandingPage.as_view(), name='landing_page'),
    path('login', views.login, name='login'),
    path('u1', views.u1, name='u1'),
    path('j1/', views.job, name='j1'),

]
