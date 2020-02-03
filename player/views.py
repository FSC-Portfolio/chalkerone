from django.views.generic import ListView, DetailView, UpdateView
from .models import PlayerStatistic
from django.urls import reverse


class ViewAllPlayers(ListView):
    model = PlayerStatistic
    template_name = 'player/view-all-players.html'


class PlayerDetailView(DetailView):
    model = PlayerStatistic
    template_name = 'player/view-single-player.html'
    #
    # def get_template_names(self):
    #     return 'player/view-single-player.html'


class UpdatePlayerStats(UpdateView):
    model = PlayerStatistic
    template_name = 'player/edit-single-player.html'
    fields = ['big_name', 'player_club', 'cc_notes']

    def get_success_url(self):
        return reverse('view_single_player', kwargs={'pk': self.object.id})