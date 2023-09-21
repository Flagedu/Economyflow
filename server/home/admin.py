from django.contrib import admin

from .models import *


admin.site.register(UserProfile)
admin.site.register(Leads)

class APIRegAdmin(admin.ModelAdmin):
    list_display = ("get_type_display", "is_active", "get_total_member")
    search_fields = ["type", ]
    list_filter = ("type",)

    def get_total_member(self, obj):
        return obj.members.count()

    get_total_member.short_description = "Total Member"

admin.site.register(ApiRegistration, APIRegAdmin)