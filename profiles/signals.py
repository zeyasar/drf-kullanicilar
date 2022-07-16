from django.contrib.auth.models import User
from .models import Profil, ProfilDurum
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_profil(sender, instance, created, **kwargs):
    if created:
        Profil.objects.create(user=instance)


@receiver(post_save, sender=Profil)
def create_ilk_durum_mesaji(sender, instance, created, **kwargs):
    if created:
        ProfilDurum.objects.create(
            user_profil=instance,
            durum_mesaji=f'{instance.user.username} aramiza katildi.'
        )