from django.contrib import admin

# Register your models here.

from event.models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    pass
    # readonly_fields = 'author',
    # exclude = ('object_id', 'content_type')
