from django.urls import path
from .views import *


urlpatterns=[
    path('item',GetItemwithCategoryView.as_view(),name='item'),
    path('datruck',GetDATruckListView.as_view(),name='datruck'),
]