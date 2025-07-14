from django.contrib import admin
from .models import Property, PropertyImage, PropertyFeature


class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 1


class PropertyFeatureInline(admin.TabularInline):
    model = PropertyFeature
    extra = 1


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ['title', 'property_type', 'listing_type', 'price', 'city', 'state', 'status', 'agent', 'created_at']
    list_filter = ['property_type', 'listing_type', 'status', 'city', 'state', 'created_at']
    search_fields = ['title', 'address', 'city', 'state', 'zip_code']
    readonly_fields = ['created_at', 'updated_at']
    inlines = [PropertyImageInline, PropertyFeatureInline]
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description', 'property_type', 'listing_type', 'status', 'agent')
        }),
        ('Property Details', {
            'fields': ('price', 'bedrooms', 'bathrooms', 'area')
        }),
        ('Location', {
            'fields': ('address', 'city', 'state', 'zip_code', 'latitude', 'longitude')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(PropertyImage)
class PropertyImageAdmin(admin.ModelAdmin):
    list_display = ['property', 'caption', 'is_primary', 'created_at']
    list_filter = ['is_primary', 'created_at']
    search_fields = ['property__title', 'caption']


@admin.register(PropertyFeature)
class PropertyFeatureAdmin(admin.ModelAdmin):
    list_display = ['property', 'feature_name', 'feature_value']
    list_filter = ['feature_name']
    search_fields = ['property__title', 'feature_name', 'feature_value']
