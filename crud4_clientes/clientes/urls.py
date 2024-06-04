from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static 

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('clientes/lista', views.lista, name='lista'),
    path('<int:id>/', views.crear_editar, name='crear_editar'),
    path('clientes/eliminar/<int:id>', views.eliminar, name='eliminar'),
    


]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
