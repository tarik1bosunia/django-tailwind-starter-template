from django.urls import path, include
from home.views import HomePageView

app_name = 'home'

urlpatterns = [
    path('', HomePageView.as_view(), name='home-page'),
]