from langchain.serpapi import SerpAPIWrapper


def get_profile_url(text: str) -> str:
    """Get the profile page URL of a person from their name"""
    search = SerpAPIWrapper()
    response = search.run(f"{text}")
    return response
