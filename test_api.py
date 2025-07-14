#!/usr/bin/env python
"""
Quick test script to verify API endpoints
"""
import requests
import json
from time import sleep

BASE_URL = "http://localhost:8000"

def test_endpoints():
    """Test all API endpoints"""
    print("🧪 Testing Real Estate Portal API endpoints...")
    
    endpoints = [
        "/properties/api/properties/",
        "/agents/api/agents/",
        "/bookings/api/appointments/",
        "/bookings/api/inquiries/",
    ]
    
    for endpoint in endpoints:
        try:
            response = requests.get(f"{BASE_URL}{endpoint}")
            if response.status_code == 200:
                print(f"✅ {endpoint} - Status: {response.status_code}")
            else:
                print(f"❌ {endpoint} - Status: {response.status_code}")
        except requests.exceptions.ConnectionError:
            print(f"❌ {endpoint} - Connection failed (server not running?)")
        except Exception as e:
            print(f"❌ {endpoint} - Error: {e}")
    
    print("\n🌐 Testing main pages...")
    
    pages = [
        "/",
        "/properties/",
        "/agents/",
        "/bookings/appointments/",
    ]
    
    for page in pages:
        try:
            response = requests.get(f"{BASE_URL}{page}")
            if response.status_code == 200:
                print(f"✅ {page} - Status: {response.status_code}")
            else:
                print(f"❌ {page} - Status: {response.status_code}")
        except requests.exceptions.ConnectionError:
            print(f"❌ {page} - Connection failed (server not running?)")
        except Exception as e:
            print(f"❌ {page} - Error: {e}")

if __name__ == "__main__":
    print("Make sure the Django development server is running:")
    print("  python manage.py runserver")
    print("\nWaiting 3 seconds...")
    sleep(3)
    test_endpoints()
