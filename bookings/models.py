from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
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
    
    def __str__(self):
        return f"{self.client_name} - {self.property.title} on {self.scheduled_date}"


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
    
    def __str__(self):
        return f"{self.name} - {self.property.title}"
