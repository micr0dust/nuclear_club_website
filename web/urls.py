from django.urls import path
from . import views
from .views import register


urlpatterns = [
    path('', views.MessageList.as_view()),
    path('create/', views.MessageCreate.as_view()),  
    path('<int:pk>', views.MessageDetail.as_view()),
    path('<int:pk>/delete/', views.MessageDelete.as_view()),   
    path('accounts/register/', register),
]