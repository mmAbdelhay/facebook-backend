# Generated by Django 3.2 on 2021-05-04 08:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('M', 'M'), ('F', 'F')], default='M', max_length=2)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('profileImg', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=1024)),
                ('Time', models.DateField(auto_now_add=True)),
                ('postImg', models.ImageField(blank=True, null=True, upload_to='')),
                ('group_ID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='groups.group')),
                ('poster_ID', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Time', models.DateField(auto_now_add=True)),
                ('content', models.TextField(max_length=1024)),
                ('UID', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='commenter', to=settings.AUTH_USER_MODEL)),
                ('postID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post', to='Users.post')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Time', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField(max_length=1024)),
                ('receiverID', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='receiver', to=settings.AUTH_USER_MODEL)),
                ('senderID', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='sender', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('senderID', 'receiverID', 'Time')},
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='liked_post', to='Users.post')),
                ('UID', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='likerID', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('UID', 'PID')},
            },
        ),
        migrations.CreateModel(
            name='Friends',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Friends', 'Friends')], max_length=15)),
                ('FID', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='friend', to=settings.AUTH_USER_MODEL)),
                ('UID', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='main_User', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('UID', 'FID')},
            },
        ),
    ]
