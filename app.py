import configparser
import json
import requests
from datetime import datetime

import api_endpoints


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
    auth_url = baseurl + auth_path
    resp = requests.get(auth_url, auth=(api_key, api_secret))
    return resp


def get_access_token(baseurl=BASE_URL, auth_path=AUTH_PATH, api_key=API_KEY, api_secret=API_SECRET):
    resp = get_auth(baseurl, auth_path, api_key, api_secret)
    resp_json = resp.json()
    return resp_json["access_token"]


def save_to_file(data, name):
    filepath = "retrieved_data/" + name
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
                filename = f"{org}-{endpoint}-{datetime.now().strftime('%Y%m%d_%H%M')}.json"
                save_to_file(api_resp.json(), filename)


if __name__ == "__main__":
    main()
