from django.contrib import admin

# Register your models here.
from main_system.models import Citizen, CitizensGroup


class CitizenAdmin(admin.ModelAdmin):
    readonly_fields = ('age',)


admin.site.register(Citizen, CitizenAdmin)
admin.site.register(CitizensGroup)
