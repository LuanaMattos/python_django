from django.urls import path
from cursos.views import index

urlpatterns = [
  	 path('', index)
]
