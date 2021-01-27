from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
# On import les vues de Django, avec un nom spécifique

urlpatterns = [

################################ URLS CREATE ###############################
    path('personnel/nouvelle', views.CreatePersonnel.as_view(), name='personnel'),
################################ URLS LIST ###############################
    path('liste/personnel', views.ListePersonnel.as_view(), name="listepersonnel"),
    path('personnel/datatable/data', views.ListePersonnelJson.as_view(), name='personnel_list_json'),
################################ URLS DETAIL ###############################
    path('lirepersonnel/<int:pk>', views.LirePersonnel.as_view(), name="detailpersonnel"),
################################ URLS UPDATE ###############################
    path('updatepersonnel/<int:pk>', views.UpdatePersonnel.as_view(), name="updatepersonnel"),
################################ URLS DELETE ###############################
    path('supprimerpersonnel/<int:pk>', views.DeletePersonnel.as_view(), name="supprimerpersonnel"),
################################ URLS DELETE MULTIPLE ###############################
    path('delete/personnel', views.Delete_Personnel, name='delete_personnel'),

]