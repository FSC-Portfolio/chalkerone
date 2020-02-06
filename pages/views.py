from django.views.generic import TemplateView


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class PrivacyPageView(TemplateView):
    template_name = 'pages/privacy.html'


class FeaturesPageView(TemplateView):
    template_name = 'pages/features.html'


class TermsPageView(TemplateView):
    template_name = 'pages/terms_of_service.html'


class TutorialsPageView(TemplateView):
    template_name = 'pages/tutorials.html'


class LiveGamePageView(TemplateView):
    template_name = 'pages/view-live-game.html'