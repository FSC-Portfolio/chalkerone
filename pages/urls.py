from django.urls import path
# from .views import HomePageView, HelpPageView, NotFound, ViewMyProfile
from .views import PrivacyPageView

urlpatterns = [
    # path('', HomePageView.as_view(), name='home'),
    path('', PrivacyPageView.as_view(), name='privacy'),
    path('privacy', PrivacyPageView.as_view(), name='privacy'),
    # path('help', HelpPageView.as_view(), name='help'),
    # path('tournament', NotFound.as_view(), name='404'),
    # path('profile', ViewMyProfile.as_view(), name='my-profile'),
]
