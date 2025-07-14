from rest_framework import serializers
from .models import Property, PropertyImage, PropertyFeature


class PropertyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyImage
        fields = ['id', 'image', 'caption', 'is_primary', 'created_at']


class PropertyFeatureSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='feature_name', read_only=True)
    value = serializers.CharField(source='feature_value', read_only=True)
    
    class Meta:
        model = PropertyFeature
        fields = ['id', 'name', 'value', 'feature_name', 'feature_value']


class PropertySerializer(serializers.ModelSerializer):
    images = PropertyImageSerializer(many=True, read_only=True)
    features = PropertyFeatureSerializer(many=True, read_only=True)
    agent_name = serializers.CharField(source='agent.get_full_name', read_only=True)
    agent_email = serializers.CharField(source='agent.email', read_only=True)
    primary_image = serializers.SerializerMethodField()
    
    class Meta:
        model = Property
        fields = [
            'id', 'title', 'description', 'property_type', 'listing_type',
            'price', 'bedrooms', 'bathrooms', 'area', 'address', 'city',
            'state', 'zip_code', 'latitude', 'longitude', 'status',
            'agent', 'agent_name', 'agent_email', 'primary_image', 'images', 'features', 'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']
    
    def get_primary_image(self, obj):
        primary_image = obj.images.filter(is_primary=True).first()
        if primary_image:
            return self.context['request'].build_absolute_uri(primary_image.image.url)
        return None


class PropertyListSerializer(serializers.ModelSerializer):
    primary_image = serializers.SerializerMethodField()
    agent_name = serializers.CharField(source='agent.get_full_name', read_only=True)
    
    class Meta:
        model = Property
        fields = [
            'id', 'title', 'property_type', 'listing_type', 'price',
            'bedrooms', 'bathrooms', 'area', 'address', 'city', 'state',
            'zip_code', 'latitude', 'longitude', 'status', 'agent_name', 'primary_image', 'created_at'
        ]
    
    def get_primary_image(self, obj):
        primary_image = obj.images.filter(is_primary=True).first()
        if primary_image:
            return self.context['request'].build_absolute_uri(primary_image.image.url)
        return None
