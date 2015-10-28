from django.contrib import admin
from sakuya.accounts.models import Child, Medal


class MedalInline(admin.StackedInline):
    model = Child.medals.through
    extra = 1


class ChildAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'sex', 'birth', 'image', 'comment'] })
    ]
    inlines = [MedalInline]
    list_display = ('name', 'detail_age', 'sex', 'birth',)


class MedalAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'type', 'image']})
    ]
    list_display = ('title', 'type',)

admin.site.register(Child, ChildAdmin)
admin.site.register(Medal, MedalAdmin)
