from django.urls import path
from test1.views import *

urlpatterns = [
    path('', Test1View.as_view()),
    path('p2', PageTwo.as_view()),
    path('contact/', ContactView.as_view())
]
