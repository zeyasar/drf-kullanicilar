# Generated by Django 4.0.6 on 2022-07-12 15:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(blank=True, max_length=500, null=True)),
                ('sehir', models.CharField(blank=True, max_length=100, null=True)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profil', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProfilDurum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('durum_mesaji', models.CharField(max_length=240)),
                ('yaratilma_zamani', models.DateTimeField(auto_now_add=True)),
                ('guncellenme_zamani', models.DateTimeField(auto_now=True)),
                ('user_profil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.profil')),
            ],
        ),
    ]
