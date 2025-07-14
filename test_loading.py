#!/usr/bin/env python3
import requests
import json
import time

# Test the API endpoints directly
def test_api_endpoints():
    base_url = "http://localhost:8000"
    
    # Test properties API
    print("Testing Properties API...")
    try:
        response = requests.get(f"{base_url}/properties/api/properties/")
        print(f"Properties API Status: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"Properties count: {data['count']}")
            print(f"Results length: {len(data['results'])}")
            if data['results']:
                print(f"First property: {data['results'][0]['title']}")
        else:
            print(f"Error: {response.text}")
    except Exception as e:
        print(f"Error accessing Properties API: {e}")
    
    print("\nTesting Agents API...")
    try:
        response = requests.get(f"{base_url}/agents/api/agents/")
        print(f"Agents API Status: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"Agents count: {data['count']}")
            print(f"Results length: {len(data['results'])}")
            if data['results']:
                print(f"First agent: {data['results'][0]['full_name']}")
        else:
            print(f"Error: {response.text}")
    except Exception as e:
        print(f"Error accessing Agents API: {e}")
    
    print("\nTesting main pages...")
    try:
        response = requests.get(f"{base_url}/properties/")
        print(f"Properties page Status: {response.status_code}")
        if response.status_code == 200:
            print("Properties page loads successfully")
        else:
            print(f"Error: {response.text}")
    except Exception as e:
        print(f"Error accessing Properties page: {e}")
    
    try:
        response = requests.get(f"{base_url}/agents/")
        print(f"Agents page Status: {response.status_code}")
        if response.status_code == 200:
            print("Agents page loads successfully")
        else:
            print(f"Error: {response.text}")
    except Exception as e:
        print(f"Error accessing Agents page: {e}")

if __name__ == "__main__":
    test_api_endpoints()
