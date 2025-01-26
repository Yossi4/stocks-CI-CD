import pytest
import requests

# Replace this URL with the actual address of your stocks service
STOCKS_SERVICE_URL = "http://localhost:5001/stocks"

@pytest.fixture(scope="module")
def check_stocks_service():
    """Fixture to check if the stocks service is running."""
    try:
        response = requests.get(STOCKS_SERVICE_URL)
        # Check for 204 No Content status code (service is up but empty)
        assert response.status_code == 204, f"Expected 204, but got {response.status_code}"
        print("Stocks service is up and running, but empty.")
    except requests.RequestException as e:
        pytest.fail(f"Failed to connect to stocks service: {e}")

def test_stocks_service(check_stocks_service):
    """Test that ensures the stocks service is up and responsive."""
    # The fixture check_stocks_service does the verification
    assert check_stocks_service is None, "The stocks service is not available."
