from django.contrib import admin

from .models import Announcement


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ["fullname", "created_at", "is_active"]
    list_filter = ["chat", "district"]
