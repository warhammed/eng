from django.contrib import admin
from .models import Album, AlbumImage

class AlbumImageInline(admin.StackedInline):
    model = AlbumImage
    extra = 0


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',),}
    inlines=[AlbumImageInline]