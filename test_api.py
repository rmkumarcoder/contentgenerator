import requests
import json

BASE_URL = "http://localhost:5000"

def test_endpoint(endpoint, data):
    """Test an API endpoint and print the results"""
    print(f"\n{'='*60}")
    print(f"Testing: {endpoint}")
    print(f"{'='*60}")
    print(f"Request data: {json.dumps(data, indent=2)}")
    
    try:
        response = requests.post(f"{BASE_URL}{endpoint}", json=data, timeout=60)
        response.raise_for_status()
        result = response.json()
        
        print(f"\nStatus Code: {response.status_code}")
        print(f"\nResponse:")
        print(f"Message: {result.get('message', 'N/A')}")
        print(f"\nGenerated Content:")
        print("-" * 60)
        print(result.get('content', 'No content'))
        print("-" * 60)
        
    except requests.exceptions.Timeout:
        print("\nError: Request timed out (content generation took too long)")
    except requests.exceptions.RequestException as e:
        print(f"\nError: {e}")

def main():
    print("AI Content Generator API - Test Suite")
    print("=" * 60)
    
    # Test 1: Blog Post
    test_endpoint("/blog-post", {
        "prompt": "Write a short blog post about the benefits of Python programming"
    })
    
    # Test 2: Whitepaper
    test_endpoint("/whitepaper", {
        "prompt": "Create a brief whitepaper on blockchain technology in supply chain"
    })
    
    # Test 3: PPT
    test_endpoint("/ppt", {
        "prompt": "Create a 5-slide presentation",
        "context": "Introduction to Machine Learning for beginners"
    })
    
    # Test 4: Facebook Post
    test_endpoint("/facebook-post", {
        "prompt": "Announce a new product",
        "context": "Smart fitness tracker with AI coaching"
    })
    
    # Test 5: LinkedIn Post
    test_endpoint("/linkedin-post", {
        "prompt": "Share professional insights",
        "context": "Leadership lessons from managing remote teams"
    })
    
    print("\n" + "=" * 60)
    print("All tests completed!")
    print("=" * 60)

if __name__ == "__main__":
    main()
