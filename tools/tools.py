from langchain_tavily import TavilySearch


def get_profile_url_tavily(name:str):
    """Searches for Linkedin or Twitter Profile Page."""
    search = TavilySearch()
    res = search.run(f"{name}")
    print("res:", res,res.get("results")[0].get("url", ""))
    return res.get("results")[0].get("url", "")
