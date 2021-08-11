from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from rest import views

urlpatterns = [
    path('categories/', views.CategoryList.as_view()),
    path('category/<int:pk>/', views.CategoryDetail.as_view()),
    path('offers/', views.OffersList.as_view()),
    path('offer/<int:pk>/', views.OfferDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

