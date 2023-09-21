import logging

from django.utils.html import format_html

from wagtail.contrib.modeladmin.options import (
    ModelAdmin, 
    modeladmin_register,
    ModelAdminGroup
)
from .models import *


class RedirectionAdmin(ModelAdmin):    
    model = Redirection
    menu_label = "Force Redirect"
    menu_icon = "folder"
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = (
        "page_type",
    )
    # list_filter = (
    #     'category', 
    #     'is_publish',
    #     'in_stock'
    # )
    # search_fields = ('name',)

modeladmin_register(RedirectionAdmin)


class CentralRedirectionAdmin(ModelAdmin):    
    model = CentralRedirection
    menu_label = "Central Redirect"
    menu_icon = "folder"
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = (
        "name",
        "is_active"
    )
    # list_filter = (
    #     'category', 
    #     'is_publish',
    #     'in_stock'
    # )
    # search_fields = ('name',)

modeladmin_register(CentralRedirectionAdmin)


class ButtonLinkAdmin(ModelAdmin):    
    model = ButtonRules
    menu_label = "Button Rules"
    menu_icon = "folder"
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = (
        "name",
    )
    # list_filter = (
    #     'category', 
    #     'is_publish',
    #     'in_stock'
    # )
    # search_fields = ('name',)

modeladmin_register(ButtonLinkAdmin)



from django.utils.html import format_html, format_html_join
from django.conf import settings

from wagtail.core import hooks


@hooks.register('insert_editor_js')
def editor_js():
    js_files = [
        'script/wagtail_admin_edit_js.js',
    ]
    js_includes = format_html_join('\n', '<script src="{0}{1}"></script>',
        ((settings.STATIC_URL, filename) for filename in js_files)
    )
    return js_includes
