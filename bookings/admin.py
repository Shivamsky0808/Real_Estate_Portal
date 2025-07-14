from django.contrib import admin
from .models import Appointment, Inquiry


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'property', 'agent', 'appointment_type', 'scheduled_date', 'scheduled_time', 'status']
    list_filter = ['appointment_type', 'status', 'scheduled_date', 'created_at']
    search_fields = ['client_name', 'client_email', 'property__title', 'agent__user__first_name', 'agent__user__last_name']
    readonly_fields = ['created_at', 'updated_at']
    date_hierarchy = 'scheduled_date'
    
    fieldsets = (
        ('Client Information', {
            'fields': ('client_name', 'client_email', 'client_phone')
        }),
        ('Appointment Details', {
            'fields': ('property', 'agent', 'appointment_type', 'scheduled_date', 'scheduled_time', 'duration', 'status')
        }),
        ('Additional Information', {
            'fields': ('notes',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ['name', 'property', 'inquiry_type', 'is_responded', 'created_at']
    list_filter = ['inquiry_type', 'is_responded', 'created_at']
    search_fields = ['name', 'email', 'property__title', 'message']
    readonly_fields = ['created_at']
    
    fieldsets = (
        ('Contact Information', {
            'fields': ('name', 'email', 'phone')
        }),
        ('Inquiry Details', {
            'fields': ('property', 'inquiry_type', 'message', 'is_responded')
        }),
        ('Timestamps', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
