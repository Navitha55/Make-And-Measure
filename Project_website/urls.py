from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('',views.indexAI,name='indexAI'),
    path('AiTailor/fabric',views.fabric,name='fabric'),
    path('AiTailor/fabric/category',views.category,name='category'),
    path('AiTailor/fabric/category/measure',views.measure,name='measure'),
    path('select_fabric/', views.select_fabric, name='select_fabric'),
    path('select_dress/', views.select_dress, name='select_dress'),
    path('measurements/', views.measurement_form, name='measurement_form'),
    path('AiTailor/fabric/category/measure/stitching_result',views.result,name='result')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
