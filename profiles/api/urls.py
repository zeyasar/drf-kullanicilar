
from django.urls import path, include
from profiles.api.views import ProfilViewSet, ProfilDurumViewset, ProfilFotoUpdateView
from rest_framework.routers import DefaultRouter

# profil_list = ProfilViewSet.as_view({'get':'list'})
# profil_detay = ProfilViewSet.as_view({'get': 'retrieve'})

# urlpatterns = [
#     path('kullanici-profilleri/', profil_list, name='kullanici-profilleri'),
#     path('kullanici-profilleri/<int:pk>', profil_detay, name='kullanici-profilleri'),

# ]
router = DefaultRouter()
router.register('kullanici-profilleri', ProfilViewSet)
router.register('durum', ProfilDurumViewset, basename='durum')


urlpatterns = [
    path('', include(router.urls)),
    path('profil_foto', ProfilFotoUpdateView.as_view(), name='foto'),
]