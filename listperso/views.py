from django.shortcuts import redirect, render
from .models import *
from django.db.models import Q
from .forms import *
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.http import JsonResponse

# Create your views here.

class CreatePersonnel(LoginRequiredMixin,CreateView):
    model = Personnel
    form_class = FormPersonnel
    template_name = 'listperso/personnel.html'
    success_url = reverse_lazy('listepersonnel')
    login_url = '/login'

################################ LIST VIEWS ###############################
class ListePersonnel(LoginRequiredMixin,ListView):
    model = Personnel
    context_object_name = "liste_personnel"
    template_name = 'listperso/listepersonnel.html'
    login_url = '/login'
    
    
################################ DATATABLE DATA ##########################

class ListePersonnelJson(BaseDatatableView):

    model = Personnel
    
    columns = ['id','identifiant', 'prenom','nom','fonction','tel','email']

    order_columns = ['id','identifiant', 'prenom','nom','fonction','tel','email']
    
    def filter_queryset(self, qs):
        # use parameters passed in GET request to filter queryset

        search = self.request.GET.get('search[value]', None)

        identifiant = self.request.GET.get('columns[1][search][value]', '')
        prenom = self.request.GET.get('columns[2][search][value]', '')
        nom = self.request.GET.get('columns[3][search][value]', '')
        fonction = self.request.GET.get('columns[4][search][value]', '')
        tel = self.request.GET.get('columns[5][search][value]', '')
        email= self.request.GET.get('columns[6][search][value]', '')
        
        if search:
            q = Q(identifiant__contains=search)|Q(prenom__contains=search)|Q(nom__contains=search)
            Q(fonction__grade__contains=fonction)|Q(tel__contains=tel)|Q(email__contains=email)|Q(prenom__contains=prenom)|Q(nom__contains=nom)
            qs = qs.filter(q)
        q = Q(identifiant__contains=identifiant)&Q(prenom__contains=prenom)&Q(nom__contains=nom)&Q(fonction__contains=fonction)&Q(tel__contains=tel)&Q(email__contains=email)
        qs = qs.filter(q)
        return qs


################################ DETAIL VIEWS ###############################

class LirePersonnel(LoginRequiredMixin,DetailView):
    model = Personnel
    context_object_name = "detpersonnel"
    template_name = 'listperso/lirepersonnel.html'
    login_url = '/login'
    
######################################## UPDATE VIEWS  ######################################## 
class UpdatePersonnel(LoginRequiredMixin,UpdateView):
    model = Personnel
    template_name = 'list/updatepersonnel.html'
    form_class = FormPersonnel
    success_url = reverse_lazy('listepersonnel')  
    login_url = '/login'
    
######################################## DELETE VIEWS   ######################################## 

class DeletePersonnel(LoginRequiredMixin,DeleteView):
    model = Personnel
    template_name = 'listperso/lirepersonnel.html'
    success_url = reverse_lazy('listepersonnel') 
    login_url = '/login'
    

################################ SUPPRESSION MULTIPLE ###############################

def Delete_Personnel(request, id=None):

    if request.method == 'POST': 
        id_list = request.POST.getlist('choice')
        if id_list:
          for personnel_id in id_list:
              Personnel.objects.get(id=personnel_id).delete()
          return JsonResponse({"success":1}) 
          
        else:
            return JsonResponse({"success":0})
    return  render(request, 'listperso/listepersonnel.html') 

