from django.contrib import admin
from .models import MechanicalPart, RawMaterial, ElectricalPart
# Register your models here.

admin.site.register(MechanicalPart)
admin.site.register(RawMaterial)
admin.site.register(ElectricalPart)
