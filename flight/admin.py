from django.contrib import admin
from .models import Post, Aircraft, Airport, Flight

admin.site.register(Post)
admin.site.register(Aircraft)
# admin.site.register(Airport)
admin.site.register(Flight)

@admin.register(Airport)
class AirportAdmin(admin.ModelAdmin):
    search_fields = ['city']