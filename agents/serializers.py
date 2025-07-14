from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Agent, AgentReview


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']


class AgentReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgentReview
        fields = ['id', 'reviewer_name', 'rating', 'comment', 'created_at']
        read_only_fields = ['created_at']


class AgentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    reviews = AgentReviewSerializer(many=True, read_only=True)
    property_count = serializers.SerializerMethodField()
    full_name = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()
    profile_image = serializers.SerializerMethodField()
    
    class Meta:
        model = Agent
        fields = [
            'id', 'user', 'full_name', 'email', 'phone_number', 'license_number', 'agency_name',
            'bio', 'profile_picture', 'profile_image', 'years_experience', 'specialization',
            'website', 'is_verified', 'rating', 'reviews', 'property_count',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at', 'rating']
    
    def get_property_count(self, obj):
        return obj.properties_count
    
    def get_full_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"
    
    def get_email(self, obj):
        return obj.user.email
    
    def get_profile_image(self, obj):
        if obj.profile_picture:
            return self.context['request'].build_absolute_uri(obj.profile_picture.url)
        return None


class AgentListSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    property_count = serializers.SerializerMethodField()
    full_name = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()
    profile_image = serializers.SerializerMethodField()
    phone = serializers.CharField(source='phone_number', read_only=True)
    properties_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Agent
        fields = [
            'id', 'user', 'full_name', 'email', 'phone', 'phone_number', 'agency_name', 'years_experience',
            'specialization', 'is_verified', 'rating', 'property_count', 'properties_count', 'profile_image', 'bio'
        ]
    
    def get_property_count(self, obj):
        return obj.properties_count
    
    def get_properties_count(self, obj):
        return obj.properties_count
    
    def get_full_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"
    
    def get_email(self, obj):
        return obj.user.email
    
    def get_profile_image(self, obj):
        if obj.profile_picture:
            return self.context['request'].build_absolute_uri(obj.profile_picture.url)
        return None
