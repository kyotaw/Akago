from django.contrib import admin
from sakuya.photos.models import Photo, Stamp


class PhotoInline(admin.StackedInline):
   model = Photo
   extra = 1


class PhotoAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'image', 'audio', 'movie', 'stamp', 'date', 'age', 'comment', 'motion', 'footer', 'owner']})
    ]
    list_display = ('title', 'date',)


class StampAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'image']})
    ]
    list_display = ('title',)
    inlines = [PhotoInline]

admin.site.register(Photo, PhotoAdmin)
admin.site.register(Stamp, StampAdmin)
