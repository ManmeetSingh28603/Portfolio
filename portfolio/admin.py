from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at', 'is_read', 'message_preview')
    list_filter = ('is_read', 'created_at')
    search_fields = ('name', 'email', 'message')
    readonly_fields = ('created_at',)
    list_editable = ('is_read',)
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    
    fieldsets = (
        ('Contact Information', {
            'fields': ('name', 'email', 'created_at')
        }),
        ('Message', {
            'fields': ('message',),
            'classes': ('wide',)
        }),
        ('Status', {
            'fields': ('is_read',),
            'classes': ('collapse',)
        }),
    )
    
    def message_preview(self, obj):
        """Show first 50 characters of the message"""
        return obj.message[:50] + '...' if len(obj.message) > 50 else obj.message
    message_preview.short_description = 'Message Preview'
    
    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)
    mark_as_read.short_description = "Mark selected messages as read"
    
    def mark_as_unread(self, request, queryset):
        queryset.update(is_read=False)
    mark_as_unread.short_description = "Mark selected messages as unread"
    
    def get_queryset(self, request):
        """Show unread messages first"""
        qs = super().get_queryset(request)
        return qs.extra(select={'is_read_order': 'CASE WHEN is_read = 1 THEN 1 ELSE 0 END'}).order_by('is_read_order', '-created_at')
    
    actions = [mark_as_read, mark_as_unread]
