from django.views.generic import ListView, DetailView, CreateView
from .models import DartClub
from django.urls import reverse


class ViewAllClubs(ListView):
    model = DartClub
    template_name = 'club/view-all-clubs.html'


class ClubDetailView(DetailView):
    model = DartClub
    template_name = 'club/view-single-club.html'


class CreateClub(CreateView):
    model = DartClub
    template_name = 'club/create-club.html'
    fields = ['club_name', 'date_established', 'club_status', 'club_member_fees', 'club_meeting_frequency', 'club_banner_image']

    def get_success_url(self):
        return reverse('view_single_club', kwargs={'pk': self.object.id})

