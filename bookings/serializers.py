from rest_framework import serializers
from .models import Appointment, Inquiry
from properties.serializers import PropertyListSerializer
from agents.serializers import AgentListSerializer


class AppointmentSerializer(serializers.ModelSerializer):
    property_details = PropertyListSerializer(source='property', read_only=True)
    agent_details = AgentListSerializer(source='agent', read_only=True)
    
    class Meta:
        model = Appointment
        fields = [
            'id', 'property', 'property_details', 'agent', 'agent_details',
            'client_name', 'client_email', 'client_phone', 'appointment_type',
            'scheduled_date', 'scheduled_time', 'duration', 'status', 'notes',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']


class AppointmentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = [
            'property', 'agent', 'client_name', 'client_email', 'client_phone',
            'appointment_type', 'scheduled_date', 'scheduled_time', 'duration', 'notes'
        ]


class InquirySerializer(serializers.ModelSerializer):
    property_details = PropertyListSerializer(source='property', read_only=True)
    
    class Meta:
        model = Inquiry
        fields = [
            'id', 'property', 'property_details', 'name', 'email', 'phone',
            'inquiry_type', 'message', 'is_responded', 'created_at'
        ]
        read_only_fields = ['created_at', 'is_responded']


class InquiryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inquiry
        fields = [
            'property', 'name', 'email', 'phone', 'inquiry_type', 'message'
        ]
