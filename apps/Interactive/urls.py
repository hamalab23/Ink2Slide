from django.urls import path
from . import views

app_name = 'Interactive'

urlpatterns = [
    #path('', views.IndexView.as_view(), name='Interactive_index'),
    path('home/', views.home, name='home'),
    path('tips/', views.show_tips, name='tips'),
    path('developer', views.show_developer, name='developer')
]