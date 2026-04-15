from django.urls import path
from . import views

urlpatterns = [
    path('join/<int:id>/', views.join_event, name='join_event'),
    path('cancel/<int:id>/', views.cancel_event, name='cancel_event'),
    path('<int:id>/participants/', views.participants_list, name='participants_list'),
     path('cancel/<int:id>/', views.cancel_event, name='cancel_event'),

]