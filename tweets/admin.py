from django.contrib import admin

# Register your models here.
from .models import Tweet


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'content', 'image']
    search_fields = ['user__username', 'user__email']

    class Meta:
        model = Tweet
