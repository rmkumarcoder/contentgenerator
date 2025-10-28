import requests
import json

BASE_URL = "http://localhost:5000"

def test_ppt_generation():
    """Test PowerPoint generation endpoint"""
    print("=" * 60)
    print("Testing PowerPoint Generation Endpoint")
    print("=" * 60)
    
    # Test 1: PPT with specific template
    print("\n1. Testing with 'professional_blue' template...")
    data = {
        "prompt": "Create a presentation about AI in Education",
        "context": "Focus on benefits, challenges, and future trends",
        "template": "professional_blue"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/ppt", json=data, timeout=60)
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            filename = "test_presentation_1.pptx"
            with open(filename, "wb") as f:
                f.write(response.content)
            print(f"✓ Success! File saved as: {filename}")
            print(f"  File size: {len(response.content)} bytes")
        else:
            print(f"✗ Error: {response.text}")
    except requests.exceptions.Timeout:
        print("✗ Request timed out (generation took too long)")
    except Exception as e:
        print(f"✗ Error: {e}")
    
    # Test 2: PPT with random template (no template specified)
    print("\n2. Testing with random template (no template specified)...")
    data = {
        "prompt": "Create a presentation about Python Programming",
        "context": "Cover basics, advanced features, and best practices"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/ppt", json=data, timeout=60)
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            filename = "test_presentation_2.pptx"
            with open(filename, "wb") as f:
                f.write(response.content)
            print(f"✓ Success! File saved as: {filename}")
            print(f"  File size: {len(response.content)} bytes")
        else:
            print(f"✗ Error: {response.text}")
    except requests.exceptions.Timeout:
        print("✗ Request timed out (generation took too long)")
    except Exception as e:
        print(f"✗ Error: {e}")
    
    # Test 3: PPT with different template
    print("\n3. Testing with 'vibrant_orange' template...")
    data = {
        "prompt": "Create a short presentation",
        "context": "5 tips for productivity",
        "template": "vibrant_orange"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/ppt", json=data, timeout=60)
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            filename = "test_presentation_3.pptx"
            with open(filename, "wb") as f:
                f.write(response.content)
            print(f"✓ Success! File saved as: {filename}")
            print(f"  File size: {len(response.content)} bytes")
        else:
            print(f"✗ Error: {response.text}")
    except requests.exceptions.Timeout:
        print("✗ Request timed out (generation took too long)")
    except Exception as e:
        print(f"✗ Error: {e}")
    
    print("\n" + "=" * 60)
    print("Testing Complete!")
    print("=" * 60)

if __name__ == "__main__":
    test_ppt_generation()
