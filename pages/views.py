from django.views.generic import TemplateView


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class PrivacyPageView(TemplateView):
    template_name = 'pages/privacy.html'
