from django.contrib import admin
from .models import *

# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
     list_display=('id','name','age','gender','occupation','email')
     list_display_links=('name','email')
     list_filter=('gender','is_married')
     search_filters=('occupations',)

admin.site.register(Profile, ProfileAdmin)


admin.site.register(Father)
admin.site.register(Religion)
admin.site.register(Sect)
admin.site.register(hobby)
admin.site.register(Caste)