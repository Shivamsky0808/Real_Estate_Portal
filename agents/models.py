from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from decimal import Decimal


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    license_number = models.CharField(max_length=50, unique=True)
    agency_name = models.CharField(max_length=200)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='agent_profiles/', blank=True)
    years_experience = models.PositiveIntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(99)],
        help_text="Years of experience (0-99)"
    )
    specialization = models.CharField(max_length=200, blank=True)
    website = models.URLField(blank=True)
    is_verified = models.BooleanField(default=False)
    rating = models.DecimalField(
        max_digits=4, 
        decimal_places=2, 
        default=0.00,
        validators=[MinValueValidator(Decimal('0.00')), MaxValueValidator(Decimal('5.00'))],
        help_text="Agent rating (0.00-5.00)"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['agency_name']),
            models.Index(fields=['is_verified']),
            models.Index(fields=['rating']),
            models.Index(fields=['years_experience']),
        ]
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - {self.agency_name}"
    
    def update_rating(self):
        """Update agent rating based on reviews"""
        reviews = self.reviews.all()
        if reviews.exists():
            total_rating = sum(review.rating for review in reviews)
            self.rating = total_rating / reviews.count()
            self.save(update_fields=['rating'])
    
    @property
    def total_reviews(self):
        """Get total number of reviews"""
        return self.reviews.count()
    
    @property
    def properties_count(self):
        """Get total number of properties"""
        return self.user.properties.count()


class AgentReview(models.Model):
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, related_name='reviews')
    reviewer_name = models.CharField(max_length=100)
    reviewer_email = models.EmailField()
    rating = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
        unique_together = ['agent', 'reviewer_email']  # Prevent duplicate reviews
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Update agent rating after saving review
        self.agent.update_rating()
    
    def __str__(self):
        return f"Review for {self.agent.user.first_name} {self.agent.user.last_name} - {self.rating} stars"
