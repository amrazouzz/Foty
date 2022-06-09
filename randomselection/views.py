
from multiprocessing import context
from turtle import position
from django.shortcuts import render, redirect
import random

from randomselection.models import Player
from .forms import SelectionForm, PlayerForm
# Create your views here.
def home(response):
    context = {}
    return render(response,"../templates/home.html",context)

def selection(response):
    players = Player.objects.all()
    gks = Player.objects.filter(position="حارس")
    defenders = Player.objects.filter(position="دفاع")
    mids = Player.objects.filter(position="وسط")
    strikers = Player.objects.filter(position="هجوم")

    gk_names = list(gks)
    gks_r = random.sample(gk_names,k=3)
    gks_ra = gks_r[0]
    gks_rb = gks_r[1]
    gks_rc = gks_r[2]

    defs = list(defenders)
    defs_r = random.sample(defs,k=6)
    defs_a = defs_r[0]
    defs_b = defs_r[1]
    defs_c = defs_r[2]
    defs_d = defs_r[3]
    defs_e = defs_r[4]
    defs_f = defs_r[5]

    mid = list(mids)
    mids_r = random.sample(mid,k=6)
    mids_a = mids_r[0]
    mids_b = mids_r[1]
    mids_c = mids_r[2]
    mids_d = mids_r[3]
    mids_e = mids_r[4]
    mids_f = mids_r[5]

    fwd = list(strikers)
    stk_r = random.sample(fwd,k=6)
    stk_a = stk_r[0]
    stk_b = stk_r[1]
    stk_c = stk_r[2]
    stk_d = stk_r[3]
    stk_e = stk_r[4]
    stk_f = stk_r[5]
   


    context = {
        'players' : players,
        'defenders':defenders,
        'gks_ra':gks_ra,
        'gks_rb':gks_rb,
        'gks_rc':gks_rc,
        'gks':gks,
        'mids':mids,
        'strikers':strikers,
        'gks_r':gks_r,
        'defs_a':defs_a,
        'defs_b':defs_b,
        'defs_c':defs_c,
        'defs_d':defs_d,
        'defs_e':defs_e,
        'defs_f':defs_f,
        'mids_a':mids_a,
        'mids_b':mids_b,
        'mids_c':mids_c,
        'mids_d':mids_d,
        'mids_e':mids_e,
        'mids_f':mids_f,
        'stk_a':stk_a,
        'stk_b':stk_b,
        'stk_c':stk_c,
        'stk_d':stk_d,
        'stk_e':stk_e,
        'stk_f':stk_f,

    }
    return render(response,"../templates/randomSelection.html",context)

def createNewSelection(request):
    form = SelectionForm()
    if request.method == 'POST':
        form = SelectionForm(request.POST)
        if form.is_valid:
            form.save()
        return redirect('../add_new_player/')

    context={'form': form}
    return render(request,"../templates/forms/create_selection.html",context)


def AddPlayer(request):
    playerform = PlayerForm()
    if request.method =='POST':
        playerform = PlayerForm(request.POST)
        if playerform.is_valid:
            playerform.save()
            # return redirect("../templates/forms/add_players.html")
        else:
            pass
    players = Player.objects.all()
    context = {'playerForm':playerform, 'players':players}
    return render (request,'../templates/forms/add_players.html',context)

def UpdatePlayer(request, pk):
    player = Player.objects.get(id=pk)
    form = PlayerForm(instance=player)

    if request.method == 'POST':
        form = PlayerForm(request.POST, instance=player)
        if form.is_valid():
            form.save()
            return redirect('players_list')
    context ={'form':form}
    return render(request,'../templates/update_player.html',context)

def PlayersList(request):
    players = Player.objects.all()
    return render(request,'../templates/players_list.html',{'players':players})


def deletePlayer(request,pk):
    player = Player.objects.get(id=pk)
    if request.method == "POST":
        player.delete()
        return redirect('players_list')
    context = {'item':player}
    return render(request, '../templates/delete_player.html',context)