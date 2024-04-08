from django.contrib import admin

# Register your models here.

from .models import Students , Attendence , Groups

class UserAdmin(admin.ModelAdmin):
    ordering=['id']
    list_display=(
        ['username']
    )
    search_fields=('username','date') # search qo'shib beradi

admin.site.register(Students,UserAdmin)
admin.site.register(Attendence)
admin.site.register(Groups)