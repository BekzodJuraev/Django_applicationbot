from django.urls import path
from . import views
app_name='application'
urlpatterns=[

    path('api/',views.APIBOT.as_view(),name='api')
]