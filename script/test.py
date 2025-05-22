import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
import os
from main import fetch_trading_data, save_to_csv

class TestMainFunctions(unittest.TestCase):

    @patch("main.requests.get")
    def test_fetch_trading_data_success(self, mock_get):
        # Mock the API response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"symbol": "AAPL", "price": 150.0}
        mock_get.return_value = mock_response

        # Call the function
        api_url = "https://api.example.com/trading-data"
        params = {"symbol": "AAPL", "interval": "1min", "apikey": "test_api_key"}
        result = fetch_trading_data(api_url, params)

        # Assertions
        mock_get.assert_called_once_with(api_url, params=params)
        self.assertEqual(result, {"symbol": "AAPL", "price": 150.0})

    @patch("main.requests.get")
    def test_fetch_trading_data_failure(self, mock_get):
        # Mock a failed API response
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("Not Found")
        mock_get.return_value = mock_response

        # Call the function and expect an exception
        api_url = "https://api.example.com/trading-data"
        params = {"symbol": "AAPL", "interval": "1min", "apikey": "test_api_key"}
        with self.assertRaises(requests.exceptions.HTTPError):
            fetch_trading_data(api_url, params)

    def test_save_to_csv(self):
        # Sample data to save
        data = [{"symbol": "AAPL", "price": 150.0}, {"symbol": "GOOG", "price": 2800.0}]
        filename = "test_trading_data.csv"

        # Call the function
        save_to_csv(data, filename)

        # Verify the file contents
        self.assertTrue(os.path.exists(filename))
        df = pd.read_csv(filename)
        self.assertEqual(len(df), 2)
        self.assertEqual(list(df.columns), ["symbol", "price"])
        self.assertEqual(df.iloc[0]["symbol"], "AAPL")
        self.assertEqual(df.iloc[1]["price"], 2800.0)

        # Clean up
        os.remove(filename)

if __name__ == "__main__":
    unittest.main()