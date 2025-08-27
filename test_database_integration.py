#!/usr/bin/env python3
"""
Test script to verify database integration works correctly
Run this after setting up your database integration
"""

import requests
import json

BASE_URL = "http://127.0.0.1:8000"

def test_health_check():
    """Test if the API is running and database is connected"""
    print("\n🔍 Testing health check...")
    response = requests.get(f"{BASE_URL}/health")
    if response.status_code == 200:
        print("✅ Health check passed:", response.json())
        return True
    else:
        print("❌ Health check failed:", response.status_code)
        return False

def test_analyze_without_user():
    """Test analysis without user information (should still work)"""
    print("\n🔍 Testing analysis without user data...")

    # Test with no file (should use sample.pdf)
    response = requests.post(f"{BASE_URL}/analyze")

 if response.status_code == 200:
        result = response.json()
        print("✅ Analysis without user succeeded")
        print(f"   Analysis ID: {result.get('id')}")
        print(f"   Filename: {result.get('filename')}")
        print(f"   Status: {result.get('status')}")
        return result.get('id')
    else:
        print("❌ Analysis without user failed:", response.status_code)
        print("   Error:", response.text)
        return None

def test_analyze_with_user():
    """Test analysis with user information"""
    print("\n🔍 Testing analysis with user data...")

    data = {
        'user_email': 'test@example.com',
        'user_name': 'Test User'
    }

    response = requests.post(f"{BASE_URL}/analyze", data=data)

    if response.status_code == 200:
        result = response.json()
        print("✅ Analysis with user succeeded")
        print(f"   Analysis ID: {result.get('id')}")
        print(f"   User ID: {result.get('user_id')}")
        print(f"   Filename: {result.get('filename')}")
        return result.get('id'), result.get('user_id')
    else:
        print("❌ Analysis with user failed:", response.st
