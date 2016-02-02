from django.contrib import admin
from app01.models import *
# Register your models here.

class UserTypeAdmin(admin.ModelAdmin):
    list_display = ('display',)

class AdminAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'usertype')

class NewsTypeAdmin(admin.ModelAdmin):
    list_display = ('display',)

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'user','create_date',)

class ReplyAdmin(admin.ModelAdmin):
    list_display = ('content', 'new', 'user', 'create_date')

class ChatAdmin(admin.ModelAdmin):
    list_display = ('content', 'user', 'create_date')

admin.site.register(UserType, UserTypeAdmin)
admin.site.register(Admin, AdminAdmin)
admin.site.register(NewsType, NewsTypeAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Reply, ReplyAdmin)
admin.site.register(Chat, ChatAdmin)

