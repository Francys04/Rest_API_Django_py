from django.urls import path
from . import views



urlpatterns = [
    path('', views.endpoints),
    path('advocates/', views.advocate_list, name="advocates"),
    # dynamic file with slug(username)
    # path('advocates/<str:username>/', views.advocate_details),
    # with vie method
    path('advocates/<str:username>/', views.AdvocateDetail.as_view()),
    
    
    
    # componies endpoints 
    path('componies/', views.companies_list)
]
