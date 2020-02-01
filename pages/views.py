from django.views.generic import TemplateView


# Create your views here.
class PrivacyPageView(TemplateView):
    template_name = 'pages/privacy.html'
