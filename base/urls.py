"""This is used to define URL patterns in your Django application."""
from django.urls import path
"""This is a module containing your custom views for handling different API endpoints."""
from . import views
"""These are views provided by the DRF Simple JWT library for obtaining and refreshing 
JSON Web Tokens (JWT) for authentication."""
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

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

"""token/: This endpoint is used to obtain a JWT by sending a POST request with valid user credentials. 
This is typically used for user authentication (login).

token/refresh/: This endpoint is used to refresh an existing JWT by sending a POST request with a valid refresh token. 
JWTs have a limited lifespan, and this endpoint allows you to get a new JWT without requiring users to re-enter their credentials."""