class Article:
    """
    Class to store details of a news article from the News API.

    Attributes:
        url: The URL to the article
        source: The source of the article
        author: The author of the article
        title: The title of the article
        description: A brief description of the article
        publishedAt: The date and time the article was published
        content: The content of the article
    """

    def __init__(self, url=None, source=None, author=None, title=None,
                 description=None, publishedAt=None, content=None):
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
        # TODO: Initialize attributes
        pass

    def __str__(self):
        """Return a string representation of the article."""
        # TODO: Implement string representation
        pass

    def __repr__(self):
        """Return a detailed string representation of the article."""
        # TODO: Implement detailed representation
        pass
