from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from rooms import views

urlpatterns = [
    path('', views.rooms, name='rooms'),
    path('<slug:slug>/', views.userroom, name='userroom'),
    # path('<str:file_id>', views.file_download, name='uploadFiles'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
