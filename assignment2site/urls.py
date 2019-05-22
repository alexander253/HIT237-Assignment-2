"""assignment2site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from assignment2app import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/', views.home, name= 'home'),

    url(r'^addCasino/?$', views.add_casino_request, name= "casinoRequest"),
    url(r'^addCasinoDone/?$', views.add_casino, name= "donee"),
    url(r'^editCasino/(\d{1,4})/?$', views.edit_casino, name ="edit_casino"),
    url(r'^deleteCasino/(\d{1,4})/?$', views.delete_casino, name ="delete_casino"),
    url(r'^casinoRecords/?$', views.all_records, name= "allCasinos"),

    url(r'^addGame/?$', views.add_game_request, name= "gameRequest"),
    url(r'^addGameDone/?$', views.add_game, name= "gameAdded"),
    url(r'^editGame/(\d{1,4})/?$', views.edit_game, name ="edit_game"),
    url(r'^deleteGame/(\d{1,4})/?$', views.delete_game, name ="delete_game"),
    url(r'^gameRecords/?$', views.all_records, name= "allGames"),

    url(r'^addRestaurant/?$', views.add_restaurant_request, name= "restaurantRequest"),
    url(r'^addRestaurantDone/?$', views.add_restaurant, name= "restaurantAdded"),
    url(r'^editRestaurant/(\d{1,4})/?$', views.edit_restaurant, name ="edit_restaurant"),
    url(r'^deleteRestaurant/(\d{1,4})/?$', views.delete_restaurant, name ="delete_restaurant"),
    url(r'^restaurantRecords/?$', views.all_records, name= "allRestaurants"),
]
