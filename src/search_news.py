import requests
from typing import Optional, List, Dict, Any
from src.article import Article
import os


class SearchNews:
    """
    Class to interact with the News API and retrieve news articles.
    """

    def __init__(self, api_key: str):
        """
        Initialize SearchNews by reading API key from file.

        Args:
            api_key_file: Path to file containing the API key
        """
        pass

    def get_top_headlines(self, *terms: str) -> List[Article]:
        """
        Get top headlines from the News API.

        Args:
            date: Optional date filter (YYYY-MM-DD format)
            domain: Optional domain filter (e.g., 'bbc.co.uk')
            language: Optional language filter (e.g., 'en')
            *terms: Variable number of search terms

        Returns:
            List of Article objects
        """
        # TODO: Implement API call to /top-headlines endpoint
        # Base URL: https://newsapi.org/v2/top-headlines
        # Remember to include your API key in the request parameters
        # Parse JSON response and create Article objects
        pass

    def get_everything(
        self,
        date: Optional[str] = None,
        domains: Optional[List[str]] = None,
        language: Optional[str] = None,
        *terms: str
    ) -> List[Article]:
        """
        Get everything from the News API.

        Args:
            date: Optional date filter (YYYY-MM-DD format)
            domain: Optional domain filter (e.g., 'bbc.co.uk')
            language: Optional language filter (e.g., 'en')
            *terms: Variable number of search terms

        Returns:
            List of Article objects
        """
        # TODO: Implement API call to /everything endpoint
        # Base URL: https://newsapi.org/v2/everything
        # Remember to include your API key in the request parameters
        # Parse JSON response and create Article objects
        pass

    def _make_request(self, endpoint: str, params: Dict[str, str]) -> Any:
        """
        Helper method to make API requests.

        Args:
            endpoint: API endpoint (e.g., 'top-headlines')
            params: Query parameters for the request

        Returns:
            Dictionary of JSON response
        """
        # TODO: Implement helper method for making API requests
        # This can reduce code duplication between get_top_headlines and get_everything
        pass
        

    def _create_articles_from_response(self, response_data: Dict[str, Any]) -> List[Article]:
        """
        Helper method to create Article objects from API response.

        Args:
            response_data: JSON response from API

        Returns:
            List of Article objects
        """
        # TODO: Parse the 'articles' field from response and create Article objects
        pass
