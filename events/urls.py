from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('add/', views.add_event, name='add_event'),
    path('<int:id>/', views.event_detail, name='event_detail'),
    path('<int:id>/edit/', views.edit_event, name='edit_event'),
    path('<int:id>/delete/', views.delete_event, name='delete_event'),

    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.register, name='register'),
    path('stats/', views.stats, name='stats'),
]