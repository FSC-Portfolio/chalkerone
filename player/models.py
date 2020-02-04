from django.db import models
from django.conf import settings
from api_v0.models import BaseModel


class PlayerStatistic(BaseModel):
    CLUB_POSITION = (
        ('PRES', 'President'),
        ('VPRE', 'Vice President'),
        ('TRES', 'Treasurer'),
        ('SECR', 'Secretary'),
        ('MEMB', 'Member'),
        ('OTHE', 'Other'),
    )

    player = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='player_stat'
    )

    player_club = models.ForeignKey(
        'club.DartClub',
        on_delete=models.CASCADE,
        related_name='home_club',
        blank=True,
        null=True,
    )

    club_position = models.CharField(
        choices=CLUB_POSITION,
        max_length=22,
        blank=True,
        null=True,
    )

    big_name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )

    win_percent = models.DecimalField (
        decimal_places=4,
        default=0.0000,
        blank=True,
        max_digits=8
    )

    games_played = models.IntegerField(
        default=0,
        blank=True,
    )

    total_wins = models.IntegerField(
        default=0,
        blank=True,
    )

    total_score = models.IntegerField(
        default=0,
        blank=True,
    )

    total_darts_thrown = models.IntegerField(
        default=0,
        blank=True,
    )

    points_per_dart = models.DecimalField(
        decimal_places=4,
        default=0.0000,
        blank=True,
        max_digits=8,
    )

    six_dart_out = models.IntegerField(
        default=0,
        blank=True,
    )

    seven_dart_out = models.IntegerField(
        default=0,
        blank=True,
    )

    eight_dart_out = models.IntegerField(
        default=0,
        blank=True,
    )

    nine_dart_out = models.IntegerField(
        default=0,
        blank=True,
    )

    four_round_out = models.IntegerField(
        default=0,
        blank=True,
    )

    triple_treble_twenty = models.IntegerField(
        default=0,
        blank=True,
    )

    triple_treble_other = models.IntegerField(
        default=0,
        blank=True,
    )

    half_ton = models.IntegerField(
        default=0,
        blank=True,
    )

    high_ton = models.IntegerField(
        default=0,
        blank=True,
    )

    low_ton = models.IntegerField(
        default=0,
        blank=True,
    )

    one_seventy_peg = models.IntegerField(
        default=0,
        blank=True,
    )

    one_seven_one = models.IntegerField(
        default=0,
        blank=True,
    )

    cc_notes = models.TextField(
        blank=True,
        null=True,
    )

    def __str__(self):
        if self.big_name:
            big_name = self.big_name
        else:
            big_name = self.id
        return "%s" % big_name


# class Post(models.Model):
#     # title = models.CharField(max_length=200)
#     # author = models.ForeignKey(
#     # 'auth.User',
#     # on_delete=models.CASCADE,
#     # )
#     # body = models.TextField()
#     # def __str__(self):
#     # return self.title
#     def get_absolute_url(self):
#         return reverse('view_single_player', args=[str(self.id)])