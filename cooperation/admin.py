from django.contrib import admin
from .models import Cooperation


@admin.register(Cooperation)
class CooperationAdmin(admin.ModelAdmin):
    list_display = ('subject', 'company', 'city', 'created')
    list_filter = ('subject',)
    readonly_fields = ('subject', 'company', 'city', 'text', 'person', 'phone', 'email', 'file', 'created')
