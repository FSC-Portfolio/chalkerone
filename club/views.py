from django.views.generic import ListView, DetailView
from .models import DartClub


class ViewAllClubs(ListView):
    model = DartClub
    template_name = 'club/view-all-clubs.html'


class ClubDetailView(DetailView):
    model = DartClub
    template_name = 'club/view-single-club.html'
