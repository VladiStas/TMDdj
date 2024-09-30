from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from menu.models import Menu


class MenuMPTTModelAdmin(MPTTModelAdmin):
    mptt_level_indent = 20


admin.site.register(Menu, MenuMPTTModelAdmin)
