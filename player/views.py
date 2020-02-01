from django.views.generic import ListView, DetailView
from .models import PlayerStatistic


class ViewAllPlayers(ListView):
    model = PlayerStatistic
    template_name = 'player/view-all-players.html'


class PlayerDetailView(DetailView):
    model = PlayerStatistic
    template_name = 'player/view-single-player.html'
    #
    # def get_template_names(self):
    #     return 'player/view-single-player.html'
