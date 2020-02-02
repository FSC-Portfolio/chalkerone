from django.urls import path, re_path
from django.conf.urls import include, url
from .views import ViewAllPlayers, PlayerDetailView

urlpatterns = [
    # path('', HomePageView.as_view(), name='home'),
    path('', ViewAllPlayers.as_view(), name='view_players'),
    path('<int:pk>/', PlayerDetailView.as_view(), name='view_single_player'),
    # path('help', HelpPageView.as_view(), name='help'),
    # path('tournament', NotFound.as_view(), name='404'),
    # path('profile', ViewMyProfile.as_view(), name='my-profile'),
]
