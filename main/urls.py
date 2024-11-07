from django.urls import path
from .views import *

urlpatterns=[
    path('',Index),
    path('contact/',Contact),
    path('project/',Project),
    path('news/',News),
    path('sms/',SMS),
    path('pdf6/',Pdf6),
    path('pdf8/',Pdf8),
    path('pdf3/',Pdf3),
    path('pdf4/',Pdf4),
    path('pdf5/',Pdf5),
    path('pdf9/',Pdf9),
]