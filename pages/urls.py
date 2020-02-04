from django.urls import path
# from .views import HomePageView, HelpPageView, NotFound, ViewMyProfile
from .views import PrivacyPageView, HomePageView, FeaturesPageView, TermsPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('privacy', PrivacyPageView.as_view(), name='privacy'),
    path('features', FeaturesPageView.as_view(), name='features'),
    path('terms', TermsPageView.as_view(), name='terms_of_service'),
    # path('help', HelpPageView.as_view(), name='help'),
    # path('tournament', NotFound.as_view(), name='404'),
    # path('profile', ViewMyProfile.as_view(), name='my-profile'),
]
