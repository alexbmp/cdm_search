from django.urls import path
from . import views

app_name = 'drug'
urlpatterns = [
    path('', views.search_form, name='search_form'), # '/' in --> views.search_form
    path('results/', views.search, name='search'), # /results/ in --> views.search
]
