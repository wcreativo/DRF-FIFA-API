"Django Imports"
from django.urls import path
"Local Imports"
from apps.tecnicos.api.api import TecnicosAPIView

urlpatterns = [
    path('', TecnicosAPIView.as_view(), name='tecnicos_api'),
]