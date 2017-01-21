from django.contrib import admin
from rango.models import Category,Page

class CategoryAdmin(admin.ModelAdmin):          # this is for to simplify urls
    prepopulated_fields = {'slug':('name',)}

class pageadmin(admin.ModelAdmin):
    list_display = ['__str__','category','title']
    class Meta:
        model= Page


admin.site.register(Category,CategoryAdmin)
admin.site.register(Page,pageadmin)


