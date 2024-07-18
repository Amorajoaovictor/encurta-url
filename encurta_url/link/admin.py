from django.contrib import admin

# Register your models here.
from .models import Link    
class LinkAdmin(admin.ModelAdmin):
    list_display = ( 'url',"urlEncurtada")


admin.site.register(Link, LinkAdmin)