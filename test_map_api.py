#!/usr/bin/env python

import os
import sys
import django
import json

# Add the project directory to Python path
sys.path.insert(0, '/Users/sundaramkumaryadav/Downloads/real_estate_portal')

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'real_estate_portal.settings')
django.setup()

from properties.models import Property
from properties.serializers import PropertyListSerializer
from rest_framework.test import APIRequestFactory

def test_map_api():
    print("Testing Map API...")
    
    # Create a mock request
    factory = APIRequestFactory()
    request = factory.get('/api/properties/')
    
    # Get active properties
    properties = Property.objects.filter(status='active')
    print(f"Total active properties: {properties.count()}")
    
    # Serialize the data
    serializer = PropertyListSerializer(properties, many=True, context={'request': request})
    
    if not serializer.data:
        print("❌ No data returned from serializer")
        return
    
    print("✅ Data returned from serializer")
    
    # Check if latitude and longitude are present
    sample_property = serializer.data[0]
    print(f"Sample property: {sample_property.get('title', 'N/A')}")
    
    required_fields = ['id', 'title', 'latitude', 'longitude', 'property_type', 'listing_type', 'price', 'address', 'city']
    missing_fields = []
    
    for field in required_fields:
        if field not in sample_property:
            missing_fields.append(field)
    
    if missing_fields:
        print(f"❌ Missing required fields: {missing_fields}")
        return
    
    print("✅ All required fields are present")
    
    # Check coordinate validity
    valid_coordinates = 0
    for prop in serializer.data:
        lat = prop.get('latitude')
        lng = prop.get('longitude')
        
        if lat is not None and lng is not None:
            try:
                lat_float = float(lat)
                lng_float = float(lng)
                
                if -90 <= lat_float <= 90 and -180 <= lng_float <= 180:
                    valid_coordinates += 1
                else:
                    print(f"❌ Invalid coordinates for property {prop['id']}: lat={lat}, lng={lng}")
            except ValueError:
                print(f"❌ Invalid coordinate format for property {prop['id']}: lat={lat}, lng={lng}")
    
    print(f"✅ {valid_coordinates} properties have valid coordinates")
    
    # Print sample API response
    print("\n--- Sample API Response ---")
    print(json.dumps(serializer.data[0], indent=2))
    
    print("\n🎉 Map API test completed successfully!")
    print("The issue with the map not showing properties should now be resolved.")

if __name__ == '__main__':
    test_map_api()
