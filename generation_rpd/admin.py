from django.contrib import admin

from .models import Generator, Category, Prepod, Discip


class GeneratorAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at', 'updated_at', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


class PrepodAdmin(admin.ModelAdmin):
    list_display = ('familiya_prepod', 'name_prepod', 'otchestvo')
    search_fields = ('familiya_prepod', 'name_prepod')
    list_filter = ('familiya_prepod', 'name_prepod')


class DiscipAdmin(admin.ModelAdmin):
    list_display = ('discip_title', 'obyem_discip')
    search_fields = ('discip_title', 'obyem_discip')
    list_filter = ('discip_title', 'obyem_discip')


admin.site.register(Generator, GeneratorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Prepod, PrepodAdmin)
admin.site.register(Discip, DiscipAdmin)
