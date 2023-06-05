from django.contrib import admin
from cooperation.models import Cooperation


@admin.register(Cooperation)
class CooperationAdmin(admin.ModelAdmin):
    list_display = ('subject', 'company', 'email', 'city', 'created')
    list_filter = ('subject', 'email')

    def has_add_permission(self, request):
        return False

    def has_change_permission(request, obj=None):
        return False
