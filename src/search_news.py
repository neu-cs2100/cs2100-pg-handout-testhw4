import requests
from typing import Optional, List
from article import Article


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
        # TODO: Read API key from file and store as attribute
        # Remember to handle file reading errors appropriately
        pass

    def get_top_headlines(
        self,
        date: Optional[str] = None,
        domain: Optional[str] = None,
        language: Optional[str] = None,
        *terms
    ) -> List[Article]:
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
        # Remember to include your API key in the request headers
        # Parse JSON response and create Article objects
        pass

    def get_everything(
        self,
        date: Optional[str] = None,
        domain: Optional[str] = None,
        language: Optional[str] = None,
        *terms
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
        # Remember to include your API key in the request headers
        # Parse JSON response and create Article objects
        pass

    def _make_request(self, endpoint: str, params: dict) -> dict:
        """
        Helper method to make API requests.

        Args:
            endpoint: API endpoint (e.g., 'top-headlines')
            params: Query parameters for the request

        Returns:
            JSON response as dictionary
        """
        # TODO: Implement helper method for making API requests
        # This can reduce code duplication between get_top_headlines and get_everything
        pass

    def _create_articles_from_response(self, response_data: dict) -> List[Article]:
        """
        Helper method to create Article objects from API response.

        Args:
            response_data: JSON response from API

        Returns:
            List of Article objects
        """
        # TODO: Parse the 'articles' field from response and create Article objects
        pass


ﬁ
