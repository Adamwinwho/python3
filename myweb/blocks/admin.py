from django.contrib import admin
from .models import Blocks
# Register your models here.

class BlocksAdmin(admin.ModelAdmin):
    list_display = ("name",)

admin.site.register(Blocks,BlocksAdmin)
