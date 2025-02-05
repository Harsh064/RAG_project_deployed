import requests

# Base URL of the Flask app
base_url = 'http://127.0.0.1:5000'

def test_chat_endpoint():
    """Test the /chat endpoint."""
    print("Testing /chat endpoint...")
    
    # Send a POST request to the /chat endpoint
    response = requests.post(f'{base_url}/chat', json={'query': 'which games were played in olympics?'})
    
    # print(f"Status Code: {response.status_code}")
    # print(f"Response JSON: {response.json()}")
    
    if 'answer' in response.json():
        print("Test passed: 'answer' key found in response.")
    else:
        print("Test failed: 'answer' key not found in response.")
    
    if 'retrieved_chunks' in response.json():
        print("Test passed: 'retrieved_chunks' key found in response.")
    else:
        print("Test failed: 'retrieved_chunks' key not found in response.")

def test_history_endpoint():
    """Test the /history endpoint."""
    print("\nTesting /history endpoint...")
    
    # Send a GET request to the /history endpoint
    response = requests.get(f'{base_url}/history')
    
    # print(f"Status Code: {response.status_code}")
    # print(f"Response JSON: {response.json()}")
    
    # Check if the response is a list (chat history)
    if isinstance(response.json(), list):
        print("Test passed: Response is a list.")
    else:
        print("Test failed: Response is not a list.")

if __name__ == '__main__':
    # Run the tests
    test_chat_endpoint()
    test_history_endpoint()