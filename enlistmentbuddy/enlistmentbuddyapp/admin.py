from django.contrib import admin

from .models import IndexCard, ClassModel, ClassCode

class IndexCardAdmin(admin.ModelAdmin):
    model = IndexCard

class IndexCardInline(admin.TabularInline):
    model = IndexCard

class ClassModelAdmin(admin.ModelAdmin):
    model = ClassModel

class ClassCodeAdmin(admin.ModelAdmin):
    model = ClassCode
    

admin.site.register(IndexCard, IndexCardAdmin)
admin.site.register(ClassModel,ClassModelAdmin)
admin.site.register(ClassCode,ClassCodeAdmin)

# Register your models here.
