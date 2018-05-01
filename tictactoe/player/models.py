from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User

# Create your models here.


class Welcome(models.Model):
    firstName = models.CharField(max_length=10, default= '')
    lastName = models.CharField(max_length=10)


GAME_STATUS_CHOICES = (
    ('F', "First Player to move"),
    ('S', "Second Player to move"),
    ('W', "First player wins"),
    ('L', "Second player wins"),
    ('D', "Draw")
)


class GamesQuerySet(models.QuerySet):
    def games_for_user(self, user):
        return self.filter(
            Q(first_player=user) | Q(second_player=user)
        )

    def active(self):
        return self.filter(
            Q(status ='F') | Q(status='S')
        )


class Game(models.Model):
    first_player =models.ForeignKey(User , related_name="games_fplayer",on_delete=models.DO_NOTHING)
    second_player =models.ForeignKey(User, related_name= "games_Splayer", on_delete=models.DO_NOTHING)

    start_time = models.DateField(auto_now_add= True)
    last_active = models.DateField(auto_now= True)
    status = models.CharField(max_length= 1, default= 'F', choices=GAME_STATUS_CHOICES)
    objects = GamesQuerySet()

    def __str__(self):
        return "{0} vs {1}".format(self.first_player,self.second_player)


class Move(models.Model):
    x= models.IntegerField()
    y= models.IntegerField()
    comment= models.CharField(max_length=100, blank=True)
    by_first_player = models.BooleanField()