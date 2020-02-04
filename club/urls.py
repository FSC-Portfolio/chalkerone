from django.urls import path, re_path
from django.conf.urls import include, url
from .views import ClubDetailView, ViewAllClubs, CreateClub

urlpatterns = [
    path('', ViewAllClubs.as_view(), name='view_all_clubs'),
    path('<int:pk>/', ClubDetailView.as_view(), name='view_single_club'),
    path('create/', CreateClub.as_view(), name='create_club'),
]
