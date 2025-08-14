import os
import requests
from dotenv import load_dotenv

load_dotenv()

def scrape_linkedin_profile(linkedin_profile_url:str, mock:bool=False) -> str:
    """
    Scrape a LinkedIn profile for information.
    """
    if mock:
        linkedin_profile_url = "https://gist.githubusercontent.com/Hashamjavedofficial/be18d8a45097b32fdd8fc24ad403eee7/raw/35134ae72ec5fceeea43c1a27fdaca7591ce4b12/hasham-linkedin-json"
        response = requests.get(linkedin_profile_url, timeout=10)

    else:

        print(os.getenv("SCRAPIN_API_KEY"))
        url = "https://api.scrapin.io/v1/enrichment/profile"

        payload = {
            "linkedInUrl": linkedin_profile_url,
        }
        headers = {
            "x-api-key": os.getenv("SCRAPIN_API_KEY")
        }

        response = requests.post(url, json=payload, headers=headers)



    data = response.json().get("person")
    data = {
            k: v
            for k, v in data.items()
            if v not in ([], "", "", None) and k not in ["certifications"]
        }
    return data

scrape_linkedin_profile(mock=True,linkedin_profile_url="https://www.linkedin.com/in/hashamjaved/")
