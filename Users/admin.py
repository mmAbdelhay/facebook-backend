from django.contrib import admin

from groups.models import join, Group
from .models import Profile, Friends, Post, Message, Like, Comment
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin


class FriendsAdmin(admin.ModelAdmin):
    list_display = (['UID', 'FID', 'status'])


class PostAdmin(admin.ModelAdmin):
    list_display = (['poster_ID', 'content', 'Time', 'postImg', 'group_ID'])


class GroupAdmin(admin.ModelAdmin):
    list_display = (['created_by'])


class JoinAdmin(admin.ModelAdmin):
    list_display = (['UID', 'GID'])


class LikeAdmin(admin.ModelAdmin):
    list_display = (['UID', 'PID','pk'])


class CommentAdmin(admin.ModelAdmin):
    list_display = (['UID', 'postID', 'Time', 'content'])


class MessageAdmin(admin.ModelAdmin):
    list_display = (['senderID', 'receiverID', 'Time', 'content'])


class ProfileInline(admin.StackedInline):
    model = Profile
    max_num = 1


class UserAdmin(AuthUserAdmin):
    inlines = [ProfileInline]


admin.site.register(join, JoinAdmin)
admin.site.register(Like, LikeAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Friends, FriendsAdmin)
admin.site.register(Post, PostAdmin)
admin.site.unregister(User)
admin.site.register(Comment,CommentAdmin)
admin.site.register(User, UserAdmin)
