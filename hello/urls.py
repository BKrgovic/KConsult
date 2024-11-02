from django.urls import path
from hello import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('details/<int:id>', views.details, name='details'),
    path('', views.home2, name='home2'),
    path('search_firme', views.search_firme, name='search_firme'),
    path('companies/', views.company_index, name='company_index'),
    path('about/', views.about, name='about'),
]