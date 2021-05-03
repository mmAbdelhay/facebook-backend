# Generated by Django 3.2 on 2021-05-03 13:15

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
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('overview', models.TextField(max_length=1024)),
                ('name', models.TextField(max_length=20)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='join',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, choices=[('pending', 'pending'), ('accepted', 'accepted'), ('rejected', 'rejected')], default='pending', max_length=100, null=True)),
                ('GID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Group', to='groups.group')),
                ('UID', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='User', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('UID', 'GID')},
            },
        ),
    ]
