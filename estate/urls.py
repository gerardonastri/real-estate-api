from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.getRoutes, name="routes"),
    path('properties/',  views.getProperties, name="properties"),
    path('properties/create/', views.createProperty, name="create-property"),
    path('properties/<str:pk>',  views.getProperty, name="property"),
    path('search/properties/', views.searchProperty, name="search-property"),
    # path('properties/category/<str:cat>',  views.getCategory, name="property"),
    # path('auth/register/',  views.register, name="register"),
    # path('auth/login/',  views.login, name="login")
]
