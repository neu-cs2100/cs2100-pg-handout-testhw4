from typing import Optional

class Article:
    """
    Class to store details of a news article from the News API.

    Properties:
        url: The URL to the article
        source: The source of the article
        author: The author of the article
        title: The title of the article
        description: A brief description of the article
        published_at: The date and time the article was published
        content: The content of the article
    """

    def __init__(
            self, url: Optional[str]=None, source: Optional[str]=None, 
            author: Optional[str]=None, title: Optional[str]=None,
            description: Optional[str]=None, published_at: Optional[str]=None,
            content: Optional[str]=None) -> None:
        """
        Initialize an Article object with the given attributes.

        Args:
            url: The URL to the article
            source: The source of the article
            author: The author of the article
            title: The title of the article
            description: A brief description of the article
            publishedAt: The date and time the article was published
            content: The content of the article
        """
        pass

    def __str__(self) -> str:
        """Return a string representation of the article of the format
        'Title by Author from Source on PublishedAt' """
        pass

    def __repr__(self) -> str:
        """Return a string representation of the article of the format
        "Article(title='...', author='...', source='...', publishedAt='...')" """
        pass
