# Google Maps Configuration
# Loads credentials from environment variables for security

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Your Google Maps API Key
# Get this from: https://console.cloud.google.com/google/maps-apis/credentials
GOOGLE_MAPS_API_KEY = os.getenv('GOOGLE_MAPS_API_KEY')

# Your Google Maps Map ID (required for AdvancedMarkerElement)
# Get this from: https://console.cloud.google.com/google/maps-apis/map-ids
GOOGLE_MAPS_MAP_ID = os.getenv('GOOGLE_MAPS_MAP_ID')

# Instructions:
# 1. Go to https://console.cloud.google.com/
# 2. Create a new project or select an existing one
# 3. Enable the Maps JavaScript API
# 4. Create credentials (API Key)
# 5. Create a Map ID in the Map Management section
# 6. Replace the placeholder values above with your actual credentials
# 7. Make sure billing is enabled on your Google Cloud project

# Optional: Restrict your API key for security
# You can restrict the API key to specific URLs in the Google Cloud Console
# Recommended restrictions:
# - HTTP referrers: http://localhost:8000/*, http://127.0.0.1:8000/*, your-domain.com/*
