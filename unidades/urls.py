from django.urls import path
from unidades.views import index

urlpatterns = [
  	 path('', index)
]
