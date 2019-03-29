from django.contrib import admin
from .models import AgendaPrivada
from .models import AgendaPublica
from .models import AgendaInstitucional

# Register your models here.
@admin.register(AgendaPrivada)
class AgendaAdmin(admin.ModelAdmin):
    pass

@admin.register(AgendaPublica)
class AgendaPublicaAdmin(admin.ModelAdmin):
    pass

@admin.register(AgendaInstitucional)
class AgendaInstitucionalAdmin(admin.ModelAdmin):
    pass    