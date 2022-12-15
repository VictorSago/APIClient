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


def get_access_token(baseurl = BASE_URL, authpath = AUTH_PATH, api_key = API_KEY, api_secret = API_SECRET):
    resp = get_auth(baseurl, authpath, api_key, api_secret)
    resp_json = resp.json()
    return resp_json["access_token"]

def get_auth(baseurl, authpath, api_key, api_secret):
    auth_url = baseurl + authpath
    resp = requests.get(auth_url, auth=(api_key, api_secret))
    return resp

def run():
    for org, nfo in endpoints.items():
        access_token = get_access_token()
        for endpoint in nfo["APIEndpoints"]:
            endpoint_url = f"{nfo['BaseURL'] + nfo['APIPath']}/{endpoint}"
            session = requests.Session()
            session.headers = {"Accept": "application/json",
                               "Authorization": f"Bearer {access_token}"}
            # session.auth = ""
            # header = {"Accept": "application/json",
            #           "Authorization": f"Bearer {access_token}"}
            # api_resp = requests.get(endpoint_url, headers=header)
            api_resp = session.get(endpoint_url)
            filename = f"{org}-{endpoint}-{datetime.now().strftime('%Y%m%d_%H%M')}.json"
            filepath = "retrieved_data/" + filename
            with open(filepath, "w", encoding="utf-8") as f:
                json.dump(api_resp.json(), f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    run()
