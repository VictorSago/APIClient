"""
API Client that retrieves information from CENELEC and saves it in json files inside retrieved_data folder
"""

import configparser
import json
from datetime import datetime
import requests

import api_endpoints


__author__ = "Victor Sago"
__email__ = "VictorSago01@gmail.com"
__copyright__ = ""
__license__ = "Unlicensed"
__version__ = "0.5.0"
__maintainer__ = ""
__email__ = "dev@elstandard.se"
__status__ = "Development"


AUTH_CONFIG_NAME = "auth.ini"
auth_conf = configparser.ConfigParser()
auth_conf.read(AUTH_CONFIG_NAME)

BASE_URL = auth_conf.get("DEFAULT", "BaseURL")
AUTH_PATH = auth_conf.get("DEFAULT", "AuthPath")
API_KEY = auth_conf.get("DEFAULT", "APIKey")
API_SECRET = auth_conf.get("DEFAULT", "APISecret")

# Get all the API repositories and endpoints
endpoints = api_endpoints.endpoints


def get_auth(baseurl, auth_path, api_key, api_secret):
    """
    Get access token to be used in subsequent calls
    """
    auth_url = baseurl + auth_path
    resp = requests.get(auth_url, auth=(api_key, api_secret))
    return resp


def get_access_token(baseurl=BASE_URL, auth_path=AUTH_PATH, api_key=API_KEY, api_secret=API_SECRET):
    """
    Retrieve the access token
    The function makes a call to the API and then extracts the access token from the response.
    :param baseurl: Base URL
    :param auth_path: Path at the API for retrieving the access authorization
    :param api_key: API Key
    :param api_secret: API Secret
    :return: Access token
    """
    resp = get_auth(baseurl, auth_path, api_key, api_secret)
    resp_json = resp.json()
    return resp_json["access_token"]


def save_to_file(data, filename):
    """
    Save data to file
    :param data: The data in the json format
    :param filename: The name of the file
    """
    filepath = "retrieved_data/" + filename
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def main():
    for org, nfo in endpoints.items():
        access_token = get_access_token()
        with requests.Session() as s:
            s.headers = {"Accept": "application/json",
                         "Authorization": f"Bearer {access_token}"}
            for endpoint in nfo["APIEndpoints"]:
                endpoint_url = f"{nfo['BaseURL'] + nfo['APIPath']}/{endpoint}"
                api_resp = s.get(endpoint_url)
                # The retrieved data is saved in a file with a name that combines the name of 
                # the organization, the type of data retrieved and today's date and time
                file_name = f"{org}-{endpoint}-{datetime.now().strftime('%Y%m%d_%H%M')}.json"
                save_to_file(api_resp.json(), file_name)


if __name__ == "__main__":
    main()
