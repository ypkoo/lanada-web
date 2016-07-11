from django.contrib import admin

# Register your models here.

from .models import *

class PhotoAdmin(admin.StackedInline):
	model = Photo


class MemoryAdmin(admin.ModelAdmin):
	inlines = [PhotoAdmin,]


admin.site.register(Memory, MemoryAdmin)