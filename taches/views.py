from django.shortcuts import render , redirect , get_object_or_404 , HttpResponse
from django.urls import reverse , reverse_lazy
from django.views.generic import ListView , DetailView , CreateView , DeleteView , UpdateView
from .models import Taches , Categorie
from .forms import TacheForm , CategorieForm
from django.contrib.auth.mixins import LoginRequiredMixin


import logging

logger = logging.getLogger(__name__)

def Home(request):
    return render(request,'taches/home.html')

class TacheListView(ListView,LoginRequiredMixin):
    model = Taches
    template_name = 'taches/tache_list.html'
    context_object_name = 'taches'

    def get_queryset(self):
        queryset = super().get_queryset()  

        
        date_filtre = self.request.GET.get('date')
        if date_filtre:
            queryset = queryset.filter(date_echeance__date=date_filtre)

        priorite_filtre = self.request.GET.get('priorite')
        if priorite_filtre:
            queryset = queryset.filter(priorite=priorite_filtre)

        categorie_filtre = self.request.GET.get('q')  
        if categorie_filtre:
            queryset = queryset.filter(categorie__type__icontains=categorie_filtre)

        return queryset

class TacheCreateViewt(LoginRequiredMixin,CreateView):
    model = Taches
    form_class = TacheForm
    template_name = 'taches/tache_form.html'
    success_url = reverse_lazy('tache_list')

    def form_valid(self, form):
        # Associer l'utilisateur connecté à l'article avant de l'enregistrer
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def form_invalid(self, form):
        logger.error("Le formulaire est invalide : %s", form.errors)  
        return super().form_invalid(form)

class TacheDetailView(DetailView):
    model = Taches
    template_name = 'taches/tache_detail.html'
    context_object_name = 'tache'

class TacheDeleteView(LoginRequiredMixin,DeleteView):
    model = Taches
    template_name = 'taches/tache_delete.html'
    success_url = reverse_lazy('tache_list')

class TacheUpdateView(LoginRequiredMixin,UpdateView):
    model = Taches
    form_class = TacheForm
    template_name = ('taches/tache_edit.html')
    success_url = reverse_lazy('tache_list')

class CategorieListView(ListView,LoginRequiredMixin):
    model = Categorie
    template_name = 'taches/categorie_list.html'
    context_object_name = 'categories'
     

class CategorieCreateView(CreateView, LoginRequiredMixin):
    model = Categorie
    form_class = CategorieForm
    template_name = 'taches/categorie_form.html'
    success_url = reverse_lazy('categorie_list')

    
    def form_valid(self, form):
        # Associer l'utilisateur connecté à l'article avant de l'enregistrer
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def form_invalid(self, form):
        logger.error("Le formulaire est invalide : %s", form.errors)  
        return super().form_invalid(form)

class CategorieDeleteView(DeleteView):
    model = Categorie
    template_name = 'taches/categorie_delete.html'
    success_url = reverse_lazy('categorie_list')