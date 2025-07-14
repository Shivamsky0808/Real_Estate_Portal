from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import datetime, timedelta
from properties.models import Property
from agents.models import Agent


class Appointment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
        ('rescheduled', 'Rescheduled'),
    ]
    
    APPOINTMENT_TYPES = [
        ('viewing', 'Property Viewing'),
        ('consultation', 'Consultation'),
        ('inspection', 'Inspection'),
        ('signing', 'Document Signing'),
    ]
    
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='appointments')
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, related_name='appointments')
    client_name = models.CharField(max_length=100)
    client_email = models.EmailField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    client_phone = models.CharField(validators=[phone_regex], max_length=20)
    appointment_type = models.CharField(max_length=20, choices=APPOINTMENT_TYPES)
    scheduled_date = models.DateField()
    scheduled_time = models.TimeField()
    duration = models.DurationField(default='01:00:00')  # Default 1 hour
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['scheduled_date', 'scheduled_time']
        indexes = [
            models.Index(fields=['scheduled_date', 'scheduled_time']),
            models.Index(fields=['agent', 'status']),
            models.Index(fields=['property', 'status']),
        ]
    
    def clean(self):
        """Custom validation for Appointment model"""
        # Ensure appointment is not in the past
        if self.scheduled_date and self.scheduled_time:
            appointment_datetime = timezone.make_aware(
                datetime.combine(self.scheduled_date, self.scheduled_time)
            )
            if appointment_datetime < timezone.now():
                raise ValidationError({'scheduled_date': 'Appointment cannot be scheduled in the past'})
        
        # Ensure property is available
        if self.property and not self.property.is_available:
            raise ValidationError({'property': 'Property is not available for appointments'})
        
        # Check for double booking
        if self.agent and self.scheduled_date and self.scheduled_time:
            existing_appointments = Appointment.objects.filter(
                agent=self.agent,
                scheduled_date=self.scheduled_date,
                scheduled_time=self.scheduled_time,
                status__in=['pending', 'confirmed']
            )
            if self.pk:
                existing_appointments = existing_appointments.exclude(pk=self.pk)
            
            if existing_appointments.exists():
                raise ValidationError({
                    'scheduled_time': 'Agent already has an appointment at this time'
                })
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.client_name} - {self.property.title} on {self.scheduled_date}"
    
    @property
    def appointment_is_upcoming(self):
        """Check if appointment is upcoming"""
        if self.scheduled_date and self.scheduled_time:
            appointment_datetime = timezone.make_aware(
                datetime.combine(self.scheduled_date, self.scheduled_time)
            )
            return appointment_datetime > timezone.now()
        return False
    
    @property
    def can_be_cancelled(self):
        """Check if appointment can be cancelled"""
        return self.status in ['pending', 'confirmed'] and self.appointment_is_upcoming


class Inquiry(models.Model):
    INQUIRY_TYPES = [
        ('general', 'General Inquiry'),
        ('price', 'Price Information'),
        ('viewing', 'Schedule Viewing'),
        ('mortgage', 'Mortgage Information'),
        ('other', 'Other'),
    ]
    
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='inquiries')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=20, blank=True)
    inquiry_type = models.CharField(max_length=20, choices=INQUIRY_TYPES)
    message = models.TextField()
    is_responded = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Inquiries"
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['property', 'is_responded']),
            models.Index(fields=['inquiry_type']),
            models.Index(fields=['created_at']),
        ]
    
    def clean(self):
        """Custom validation for Inquiry model"""
        if not self.name.strip():
            raise ValidationError({'name': 'Name is required'})
        if not self.message.strip():
            raise ValidationError({'message': 'Message is required'})
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.name} - {self.property.title}"
