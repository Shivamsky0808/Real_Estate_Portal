from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from decimal import Decimal


class Property(models.Model):
    PROPERTY_TYPES = [
        ('house', 'House'),
        ('apartment', 'Apartment'),
        ('condo', 'Condo'),
        ('townhouse', 'Townhouse'),
        ('commercial', 'Commercial'),
    ]
    
    LISTING_TYPES = [
        ('sale', 'For Sale'),
        ('rent', 'For Rent'),
    ]
    
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('pending', 'Pending'),
        ('sold', 'Sold'),
        ('rented', 'Rented'),
        ('inactive', 'Inactive'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPES)
    listing_type = models.CharField(max_length=10, choices=LISTING_TYPES)
    price = models.DecimalField(
        max_digits=12, 
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'))],
        help_text="Price must be greater than 0"
    )
    bedrooms = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(50)],
        help_text="Number of bedrooms (0-50)"
    )
    bathrooms = models.DecimalField(
        max_digits=3, 
        decimal_places=1,
        validators=[MinValueValidator(Decimal('0.0')), MaxValueValidator(Decimal('50.0'))],
        help_text="Number of bathrooms (0-50)"
    )
    area = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        validators=[MinValueValidator(Decimal('1.0'))],
        help_text="Property area in square feet (minimum 1 sq ft)"
    )
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    agent = models.ForeignKey(User, on_delete=models.CASCADE, related_name='properties')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = "Properties"
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['city', 'state']),
            models.Index(fields=['property_type', 'listing_type']),
            models.Index(fields=['price']),
            models.Index(fields=['status']),
        ]
    
    def clean(self):
        """Custom validation for Property model"""
        # Validate coordinates
        if self.latitude is not None and not (-90 <= self.latitude <= 90):
            raise ValidationError({'latitude': 'Latitude must be between -90 and 90'})
        if self.longitude is not None and not (-180 <= self.longitude <= 180):
            raise ValidationError({'longitude': 'Longitude must be between -180 and 180'})
        
        # Validate status transitions
        if self.pk:
            old_instance = Property.objects.get(pk=self.pk)
            if old_instance.status == 'sold' and self.status != 'sold':
                if self.listing_type == 'sale':
                    raise ValidationError({'status': 'Cannot change status from sold for sale properties'})
            if old_instance.status == 'rented' and self.status != 'rented':
                if self.listing_type == 'rent':
                    raise ValidationError({'status': 'Cannot change status from rented for rental properties'})
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.title} - {self.city}, {self.state}"
    
    @property
    def is_available(self):
        """Check if property is available for booking"""
        return self.status == 'active'
    
    @property
    def price_per_sqft(self):
        """Calculate price per square foot"""
        if self.area > 0:
            return self.price / self.area
        return 0


class PropertyImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='property_images/')
    caption = models.CharField(max_length=200, blank=True)
    is_primary = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-is_primary', 'created_at']
    
    def __str__(self):
        return f"Image for {self.property.title}"


class PropertyFeature(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='features')
    feature_name = models.CharField(max_length=100)
    feature_value = models.CharField(max_length=200, blank=True)
    
    def __str__(self):
        return f"{self.feature_name}: {self.feature_value}"
