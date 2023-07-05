from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
 )


urlpatterns = [
    path('', views.endpoints),
    path('advocates/', views.advocate_list, name="advocates"),
    # dynamic file with slug(username)
    # path('advocates/<str:username>/', views.advocate_details),
    # with vie method
    path('advocates/<str:username>/', views.AdvocateDetail.as_view()),
   
    
    # Token JWT
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    
    # componies endpoints 
    path('companies/', views.companies_list),
    
]
