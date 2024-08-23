from django.contrib import admin
from .models import BlogModel, BlogCategoryModel



class BlogModelAdmin(admin.ModelAdmin):
    list_display = ("title","category","date_created")


admin.site.register(BlogCategoryModel)
admin.site.register(BlogModel,BlogModelAdmin)
