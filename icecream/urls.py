from django.urls import path
import views

urlpatterns = [
    path('<int:pk>/', views.icecream_detail),
]
