"""
Example usage of the News API classes.

Before running this code:
1. Get your API key from https://newsapi.org/register
2. Make sure to not push it to Github!
"""

from search_news import SearchNews
from news_processor import NewsProcessor
from datetime import datetime, timedelta


def main():
    # Initialize the news searcher
    # Make sure you have your API key in 'api_key.txt'
    searcher = SearchNews()
    
    # Initialize the processor
    processor = NewsProcessor()
    
    # Example 1: Get top headlines
    print("Getting top headlines...")
    headlines = searcher.get_top_headlines(language="en", "technology")
    print(f"Found {len(headlines)} headlines")
    
    # Example 2: Convert to DataFrame
    print("\nConverting to DataFrame...")
    df = processor.to_df(headlines)
    print(df.head())
    
    # Example 3: Filter articles (only articles with authors)
    print("\nFiltering articles with authors...")
    df_with_authors = processor.to_df(
        headlines, 
        filter_func=lambda article: article.author is not None
    )
    print(f"Articles with authors: {len(df_with_authors)}")
    
    # Example 4: Sort by publication date
    print("\nSorting by publication date...")
    df_sorted = processor.to_df(
        headlines,
        sort_by=lambda article: article.publishedAt or ""
    )
    print("Sorted DataFrame created")
    
    # Example 5: Plot word popularity
    print("\nPlotting word popularity...")
    processor.plot_word_popularity(headlines, "AI")
    
    # Example 6: Search everything for a specific term
    print("\nSearching everything for 'climate change'...")
    yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
    climate_articles = searcher.get_everything(
        date=yesterday,
        language="en",
        "climate change"
    )
    print(f"Found {len(climate_articles)} articles about climate change")


if __name__ == "__main__":
    main()