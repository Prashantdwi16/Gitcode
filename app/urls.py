from django.urls import path,include

from .views import *


urlpatterns=[
   path("new-inventory",addinventory),
   path("merge",merge),
   path("view-all",viewinventoryitems),
   path("edit-inventory",editinventory),
   path("edit",edit),
   path("delete-inventory",deleteinventory),
   path("login",userLogin),
   path("logout",userLogout),
]