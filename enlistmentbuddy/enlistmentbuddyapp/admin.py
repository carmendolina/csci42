from django.contrib import admin

from .models import IndexCard

class IndexCardAdmin(admin.ModelAdmin):
    model = IndexCard

class IndexCardInline(admin.TabularInline):
    model = IndexCard
    

admin.site.register(IndexCard, IndexCardAdmin)


# Register your models here.
