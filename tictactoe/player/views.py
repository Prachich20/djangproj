from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from .models import Welcome
from .forms import NameForm
from gameplay.models import Game


# Create your views here.


# def home(request):
#    return render(request,"player/home.html",
#                    {'ngames': Game.objects.count()}
#                    )

# my_games = Game.objects.games_for_user(request.user)
# active_games = my_games.active()
# return render(request, "player/home.html", {'games': active_games})

def home(request):

    games_first_player = Game.objects.filter(
        first_player = request.user,
        status ='F'
    )
    games_second_player = Game.objects.filter(
        second_player=request.user,
        status='S'
    )
    all_my_games = list(games_first_player) + list(games_second_player)

    return render(request,"player/home.html",{'games': all_my_games})






# def New(request):
#     if request.method == 'POST':
#         form = NameForm(data= request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("player/new.html")
#     else:
#         form = NameForm()
#     return render(request, "player/home.html", {'form': form})

