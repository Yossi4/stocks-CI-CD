import requests

# Define the stock data for the three stocks
stock1 = {
    "name": "NVIDIA Corporation", 
    "symbol": "NVDA",
    "purchase price": 134.66, 
    "purchase date": "18-06-2024",
    "shares":7
}

stock2 = {
    "name": "Apple Inc.", 
    "symbol": "AAPL",
    "purchase price": 183.63, 
    "purchase date": "22-02-2024", 
    "shares": 19
}

stock3 = {
    "name": "Alphabet Inc.", 
    "symbol": "GOOG",
    "purchase price": 140.12, 
    "purchase date": "24-10-2024", 
    "shares": 14
}

# The base URL of your application (adjust as necessary)
base_url = "http://localhost:5001"  # Replace with actual endpoint if different

def test_create_stocks():
    # Perform POST requests for the three stocks
    response1 = requests.post(f"{base_url}/stocks", json=stock1)
    response2 = requests.post(f"{base_url}/stocks", json=stock2)
    response3 = requests.post(f"{base_url}/stocks", json=stock3)

    # Assert status codes are 201 (Created)
    assert response1.status_code == 201
    assert response2.status_code == 201
    assert response3.status_code == 201

    # Get the returned IDs from the responses
    id1 = response1.json().get("id")
    id2 = response2.json().get("id")
    id3 = response3.json().get("id")

    # Assert that all IDs are unique
    assert id1 != id2
    assert id1 != id3
    assert id2 != id3
