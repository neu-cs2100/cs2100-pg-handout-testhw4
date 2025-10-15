import pandas as pd
import matplotlib.pyplot as plt
from typing import List, Dict, Callable, Optional, Any
import datetime
from src.article import Article


class NewsProcessor:
    """
    Class to process and visualize news articles data.
    """

    def to_df(self, articles: List[Article],
              sort_by: Optional[Callable[[Article], Any]] = None,
              filter_func: Optional[Callable[[Article], bool]] = None
    ) -> pd.DataFrame:
        """
        Convert list of Article objects to a Pandas DataFrame.

        Args:
            articles: List of Article objects
            sort_by: Optional function to sort rows by
            filter_func: Optional function to filter rows (include rows where function returns True)

        Returns:
            Pandas DataFrame with articles data
        """
        # TODO: Convert Article objects to DataFrame
        # Each Article attribute should be a column
        # Each article should be a row

        # TODO: Apply filtering if filter_func is provided

        # TODO: Apply sorting if sort_by is provided
        pass

    def plot_word_popularity(self, articles: List[Article], search_term: str) -> None:
        """
        Plot the frequency of a search term in article titles over time.

        Args:
            articles: List of Article objects
            search_term: The term to search for in titles
        """
        # TODO:
        # 1. Extract dates and titles from articles
        # 2. Count occurrences of search_term in titles for each date
        # 3. Create a plot with dates on x-axis and frequency on y-axis
        # 4. Display the plot

        # Hints:
        # - You may need to parse the published_at dates
        # - Consider using case-insensitive search
        # - matplotlib.pyplot can be used for plotting
        pass

    def _extract_date_from_published_at(self, published_at: Optional[str]) -> Optional[datetime.date]:
        """
        Helper method to extract date from publishedAt timestamp.

        Args:
            published_at: ISO format timestamp string (e.g., '2023-10-01T12:34:56Z')

        Returns:
            Date string in YYYY-MM-DD format, or None if input is None
        """
        # TODO: Parse ISO timestamp and return just the date part
        pass

    def _count_word_in_title(self, title: str, search_term: str) -> int:
        """
        Helper method to count occurrences of search term in title.

        Args:
            title: Article title
            search_term: Term to search for

        Returns:
            Number of occurrences (case-insensitive)
        """
        # TODO: Count occurrences of search_term in title (case-insensitive)
        pass
