from django.contrib import admin
from info.models import Info

# Register your models here.
# admin.site.register(Info)


@admin.register(Info)
class InfoAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "rating", "price", "is_buy")
    search_fields = ("name", )
    list_filter = ("is_buy", )
    sortable_by = ("price", 'rating')
