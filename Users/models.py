from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    def __str__(self):
        return str(self.user)
    MALE = 'M'
    FEMALE = 'F'
    Gender = (
        (MALE, 'M'),
        (FEMALE, 'F'),
    )
    gender = models.CharField(
        max_length=2,
        choices=Gender,
        default=MALE,
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)
    profileImg = models.ImageField()


class Group(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)


class Post(models.Model):
    def __str__(self):
        return str(self.content)
    poster_ID = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    content = models.TextField(max_length=1024)
    Time = models.DateField(auto_now_add=True)
    postImg = models.ImageField(blank=True, null=True)
    group_ID = models.ForeignKey(
        Group, blank=True, on_delete=models.DO_NOTHING, null=True)


class Message(models.Model):
    class Meta:
        unique_together = (('senderID', 'receiverID', 'Time'),)
    senderID = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, related_name='sender')
    receiverID = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, related_name='receiver')
    Time = models.DateField(auto_now_add=True)
    content = models.TextField(max_length=1024)


class Friends(models.Model):
    class Meta:
        unique_together = (('UID', 'FID'),)
    UID = models.ForeignKey(User, on_delete=models.DO_NOTHING,
                            related_name='main_User')
    FID = models.ForeignKey(User, on_delete=models.DO_NOTHING,
                            related_name='friend')


class join(models.Model):
    class Meta:
        unique_together = (('UID', 'GID'),)
    UID = models.ForeignKey(User, on_delete=models.DO_NOTHING,
                            related_name='User')
    GID = models.ForeignKey(Group, on_delete=models.DO_NOTHING,
                            related_name='Group')


class Like(models.Model):
    class Meta:
        unique_together = (('UID', 'PID'),)
    UID = models.ForeignKey(User, on_delete=models.DO_NOTHING,
                            related_name='likerID')
    PID = models.ForeignKey(Post, on_delete=models.DO_NOTHING,
                            related_name='liked_post')


class Comment(models.Model):
    class Meta:
        unique_together = (('UID', 'postID', 'Time'),)
    UID = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, related_name='commenter')
    postID = models.ForeignKey(
        Post, on_delete=models.DO_NOTHING, related_name='post')
    Time = models.DateField(auto_now_add=True)
    content = models.TextField(max_length=1024)