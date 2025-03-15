from django.urls import path, include
from PazarBet.common.views import index


urlpatterns = [
     path('', index, name='index')
]