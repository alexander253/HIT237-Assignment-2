from django.shortcuts import render
from assignment2app.models import *
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import *


def home(request):
    return render(request, 'index.html')

# Displays records depending on path

def all_records(request):
    if request.path == '/casinoRecords':
        results = CasinoModel.objects.order_by('name')
        page_data = {'list_casinos': results}
        return render(request,'all_records.html', page_data)

    elif request.path == '/gameRecords':
        results = TableGameModel.objects.order_by('name')
        page_data = {'list_games': results}
        return render(request,'all_records.html', page_data)

    elif request.path == '/restaurantRecords':
        results = RestaurantModel.objects.order_by('name')
        page_data = {'list_restaurants': results}
        return render(request,'all_records.html', page_data)



#Add, Edit and Delete Functions are all the same, just seperated.
#There's probably a better way to go about it, but yeah.


#Casino Functions


def add_casino_request(request):
    page_data = {'my_form': Casino(),}
    return render(request, 'models_form.html', page_data)

def add_casino(request):
    if request.method != 'POST':
        page_data= {'my_form': Casino(),}
    else:
        form = Casino(request.POST)
        if form.is_valid() != True:
            page_data = {'val_errors': form.errors,}

        else:
            data = form.cleaned_data
            form.save()
            return render (request,'models_form_done.html', data )
            return HttpResponseRedirect(reverse('donee'))

    return render(request, 'models_form_done.html', page_data)


def edit_casino(request, key):
    casino = CasinoModel.objects.get(id=key)
    if request.method == 'POST':
        form= Casino(request.POST, instance= casino)
        if form.is_valid() != True:
            page_data = {'val_errors': form.errors,}
            return render (request,'models_form_done.html', page_data )
        else:
            form.save()
            return HttpResponseRedirect(reverse('donee'))
    else:
        form = Casino(instance= casino)
        page_data= {'my_form': form,}
    return render(request, 'edit.html', page_data)


def delete_casino(request, key):
    casino = CasinoModel.objects.get(id=key)
    form= Casino(instance= casino)
    page_data = {'delete': form}
    casino.delete()
    return render(request, 'delete.html', page_data)




#Table Game Functions



def add_game_request(request):
    page_data = {'my_form': TableGame(),}
    return render(request, 'models_form.html', page_data)

def add_game(request):
    if request.method != 'POST':
        page_data= {'my_form': TableGame(),}
    else:
        form = TableGame(request.POST)
        if form.is_valid() != True:
            page_data = {'val_errors': form.errors,}
        else:
            data = form.cleaned_data
            form.save()
            return render (request,'models_form_done.html', data )
            return HttpResponseRedirect(reverse('gameAdded'))

    return render(request, 'models_form_done.html', page_data)


def edit_game(request, key):
    game = TableGameModel.objects.get(id=key)
    if request.method == 'POST':
        form= TableGame(request.POST, instance= game)
        if form.is_valid() != True:
            page_data = {'val_errors': form.errors,}
            return render (request,'models_form_done.html', page_data )
        else:
            form.save()
            return HttpResponseRedirect(reverse('gameAdded'))
    else:
        form = TableGame(instance= game)
        page_data= {'my_form': form,}
    return render(request, 'edit.html', page_data)

def delete_game(request, key):
    game = TableGameModel.objects.get(id=key)
    form= TableGame(instance= game)
    page_data = {'delete': form}
    game.delete()
    return render(request, 'delete.html', page_data)



#Restaurant Functions


def add_restaurant_request(request):
    page_data = {'my_form': Restaurant(),}
    return render(request, 'models_form.html', page_data)

def add_restaurant(request):
    if request.method != 'POST':
        page_data= {'my_form': Restaurant(),}
    else:
        form = Restaurant(request.POST)
        if form.is_valid() != True:
            page_data = {'val_errors': form.errors,}
        else:
            data = form.cleaned_data
            form.save()
            return render (request,'models_form_done.html', data )
            return HttpResponseRedirect(reverse('restaurantAdded'))

    return render(request, 'models_form_done.html', page_data)

def edit_restaurant(request, key):
    restaurant = RestaurantModel.objects.get(id=key)
    if request.method == 'POST':
        form= Restaurant(request.POST, instance= restaurant)
        if form.is_valid() != True:
            page_data = {'val_errors': form.errors,}
            return render (request,'models_form_done.html', page_data )
        else:
            form.save()
            return HttpResponseRedirect(reverse('restaurantAdded'))
    else:
        form = Restaurant(instance= restaurant)
        page_data= {'my_form': form,}
    return render(request, 'edit.html', page_data)


def delete_restaurant(request, key):
    restaurant = RestaurantModel.objects.get(id=key)
    form= Restaurant(instance= restaurant)
    page_data = {'delete': form}
    restaurant.delete()
    return render(request, 'delete.html', page_data)
