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

stock4 = {
    "name":"Tesla, Inc.", 
    "symbol":"TSLA",
    "purchase price":194.58, 
    "purchase date":"28-11-2022",
    "shares":32

}
stock5 = {
    "name":"Microsoft Corporation", 
    "symbol":"MSFT",
    "purchase price":420.55, 
    "purchase date":"09-02-2024",
    "shares":35
}

stock6 = {
    "name":"Intel Corporation", 
    "symbol":"INTC",
    "purchase price":19.15, 
    "purchase date":"13-01-2025", 
    "shares":10
}

stock7 = {

    "name":"Amazon.com, Inc.", 
    "purchase price":134.66, 
    "purchase date":"18-06-2024", 
    "shares":7
}


stock8 = {
    "name":"Amazon.com, Inc.", 
    "symbol":"AMZN",
    "purchase price":134.66,
    "purchase date":"Tuesday, June 18, 2024",
    "shares":7
}

# The base URL of your application (adjust as necessary)
base_url = "http://localhost:5001"  # Replace with actual endpoint if different




def test_create_stocks(): # Test 1
    
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

    return [id1,id2,id3] # For future tests


def test_get_stock_by_id1(): # Test 2
    
    # Accuiring the first id:
    stock1_id = test_create_stocks()[0]

    # Preforming the actual GET request:
    response = requests.get(f"{base_url}/stocks/{stock1_id}")

    assert response.status_code == 200

    assert response.json()["symbol"] == "NVDA"


def test_get_all_stocks(): # Test 3
    response = requests.get(f"{base_url}/stocks")

    assert response.status_code == 200

    stocks = response.json()


    assert len(stocks) == 6


def test_get_stock_by_id2():
    stock1_id = test_create_stocks()[0]
    stock2_id = test_create_stocks()[1]
    stock3_id = test_create_stocks()[2]

    response1 = requests.get(f"{base_url}/stock-value/{stock1_id}")
    response2 = requests.get(f"{base_url}/stock-value/{stock2_id}")
    response3 = requests.get(f"{base_url}/stock-value/{stock3_id}")

    assert response1.status_code == 200
    assert response2.status_code == 200
    assert response3.status_code == 200

    assert response1.json()["symbol"] == "NVDA"
    assert response2.json()["symbol"] == "AAPL"
    assert response3.json()["symbol"] == "GOOG"

    sv1 = response1.json()["ticker"]
    sv2 = response2.json()["ticker"]
    sv3 = response3.json()["ticker"]

    return [sv1,sv2,sv3]


def test_get_portfolio_value():
    stock_values = test_get_stock_by_id2()
    sv1, sv2, sv3 = float(stock_values[0]), float(stock_values[1]), float(stock_values[2])

    response = requests.get(f"{base_url}/portfolio-value")

    assert response.status_code == 200

    pv = float(response.json()["portfolio value"])

    shares1 = stock1["shares"]
    shares2 = stock2["shares"]
    shares3 = stock3["shares"]

    

    total_value = sv1*shares1 + sv2*shares2 + sv3*shares3

     # Print for debugging
    print(f"Stock 1 value: {sv1}, Shares: {shares1}, Total: {sv1 * shares1}")
    print(f"Stock 2 value: {sv2}, Shares: {shares2}, Total: {sv2 * shares2}")
    print(f"Stock 3 value: {sv3}, Shares: {shares3}, Total: {sv3 * shares3}")
    print(f"Total stock value: {total_value}")
    print(f"Portfolio value (pv): {pv}")

    # Checking for the ±3%:
    assert pv * 0.97 <= total_value <= pv * 1.03

