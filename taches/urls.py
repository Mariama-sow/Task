from django.urls import path 
from .views import Home , TacheCreateViewt , TacheDetailView , TacheListView , TacheDeleteView,TacheUpdateView,CategorieCreateView,CategorieDeleteView,CategorieListView






urlpatterns = [
    path('categorie/',CategorieListView.as_view(),name='categorie_list'),
    path('categorie_edit/<int:pk>/',CategorieDeleteView.as_view(),name='categorie_delete'),
    path('categorie_form/',CategorieCreateView.as_view(),name='categorie_form'),
    path('tache_edit/<int:pk>/',TacheUpdateView.as_view(),name='tache_edit'),
    path('tache_delete/<int:pk>/',TacheDeleteView.as_view(),name='tache_delete'),
    path('tache_form/',TacheCreateViewt.as_view(),name='tache_form'),
    path('tache_detail/<int:pk>/',TacheDetailView.as_view(),name='tache_detail'),
    path('tache/',TacheListView.as_view(),name='tache_list'),
    path('',Home,name='home' ),

]