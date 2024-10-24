from django.urls import path
from . import views


app_name="shorturl"

urlpatterns = [


    path('',views.index,name="index"),
    path('shorten/', views.shorten_url, name='shorten_url'),
    path('<str:short_url>/', views.redirect_original_url, name='redirect_original_url'),
]

