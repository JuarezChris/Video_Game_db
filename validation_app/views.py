from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

def video_games(request):
    return redirect('/home_page')

def home_page(request):
    context = {
        'all_video_games': Video_Game.objects.all()
    }
    return render(request,'home_page.html', context)

def new_page(request):
    return render(request,'new_page.html')

def add_video_game(request):
    errors = Video_Game.objects.basic_validator(request.POST)
    # check if the errors dictionary has anything in it
    if len(errors) > 0:
    # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect(f'/new')
    else:
        game = Video_Game.objects.create(title=request.POST['title'], company=request.POST['company_name'], release_date=request.POST['release_date'], description=request.POST['description'])
        return redirect(f'/details_page/{game.id}')

def details_page(request, game_id):
    context = {
        'get_game': Video_Game.objects.get(id=game_id)
    }
    return render(request, "details_page.html", context)

def edit_page(request, game_id):
    context = {
        'video_game': Video_Game.objects.get(id=game_id)
    }
    return render(request, "edit_page.html", context)

def update_my_video_game(request, game_id):
    video_game = Video_Game.objects.get(id=game_id)

    errors = Video_Game.objects.basic_validator(request.POST)
    # check if the errors dictionary has anything in it
    if len(errors) > 0:
    # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect(f'/edit_page/{game_id}')
    else:
        video_game.title = request.POST['title']
        video_game.company = request.POST['company_name']
        video_game.release_date = request.POST['release_date']
        video_game.description = request.POST['description']
        video_game.save()
        return redirect(f'/details_page/{game_id}')

def destroy(request, game_id):
    video_game = Video_Game.objects.get(id=game_id)
    video_game.delete()
    return redirect("/")