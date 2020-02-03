from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from player.models import PlayerStatistic

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        PlayerStatistic.objects.create(player=instance)

@receiver(post_save, sender=PlayerStatistic)
def save_user_profile(sender, instance, **kwargs):
    instance.player.save()