import requests
import os


def scrape_linkedin_profile(linkedin_profile_url: str):
    """scrape the information of a linkedin profiles,
    Manually scrape the information of a linkedin profile."""
    api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
    api_key = os.environ["PROXY_CURL_API_KEY"]
    header_dic = {"Authorization": f"Bearer {api_key}"}

    response = requests.get(
        api_endpoint,
        params={"url": linkedin_profile_url},
        headers=header_dic,
    )

    data = response.json()

    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k not in ["people_also_viewed", "certifications"]
    }

    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data
