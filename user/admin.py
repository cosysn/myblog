from django.contrib import admin
from myapp.models import BlogUser


# Register your models here.

class BlogUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'create_time', 'last_mod_time', 'qq', 'mobile')
    fieldsets = (('Basic', {'fields': ('username', 'create_time', 'last_mod_time', 'qq', 'mobile')}))


admin.site.register(BlogUser, BlogUserAdmin)