from django.apps import AppConfig

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class PlayerConfig(AppConfig):
    name = 'player'
    verbose_name = _('players')

    def ready(self):
        import player.signals  # noqa