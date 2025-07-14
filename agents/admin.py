from django.contrib import admin
from .models import Agent, AgentReview


class AgentReviewInline(admin.TabularInline):
    model = AgentReview
    extra = 0
    readonly_fields = ['created_at']


@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = ['user', 'license_number', 'agency_name', 'phone_number', 'years_experience', 'rating', 'is_verified']
    list_filter = ['is_verified', 'agency_name', 'years_experience', 'created_at']
    search_fields = ['user__first_name', 'user__last_name', 'user__email', 'license_number', 'agency_name']
    readonly_fields = ['created_at', 'updated_at', 'rating']
    inlines = [AgentReviewInline]
    
    fieldsets = (
        ('User Information', {
            'fields': ('user',)
        }),
        ('Professional Details', {
            'fields': ('license_number', 'agency_name', 'years_experience', 'specialization', 'is_verified')
        }),
        ('Contact Information', {
            'fields': ('phone_number', 'website')
        }),
        ('Profile', {
            'fields': ('bio', 'profile_picture', 'rating')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(AgentReview)
class AgentReviewAdmin(admin.ModelAdmin):
    list_display = ['agent', 'reviewer_name', 'rating', 'created_at']
    list_filter = ['rating', 'created_at']
    search_fields = ['agent__user__first_name', 'agent__user__last_name', 'reviewer_name', 'reviewer_email']
    readonly_fields = ['created_at']
