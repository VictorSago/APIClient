import configparser
import json
import requests
from requests.auth import HTTPBasicAuth
from datetime import datetime

import api_endpoints


AUTH_CONFIG_NAME = "auth.ini"
auth_conf = configparser.ConfigParser()
auth_conf.read(AUTH_CONFIG_NAME)

BASE_URL = auth_conf.get("DEFAULT", "BaseURL")
AUTH_PATH = auth_conf.get("DEFAULT", "AuthPath")
API_KEY = auth_conf.get("DEFAULT", "APIKey")
API_SECRET = auth_conf.get("DEFAULT", "APISecret")


endpoints = api_endpoints.endpoints

#print(config.sections())

# for section in config.sections():
#     part = config[section]
#     base_url = part.get("URL", "None")
#     print(f"Base_URL: {base_url}")
#     for key in part:
#         if key.lower() != "url":
#             print(f"{base_url}{part.get(key)}")


def get_access_token(baseurl = BASE_URL, authpath = AUTH_PATH, api_key = API_KEY, api_secret = API_SECRET):
    resp = get_auth(baseurl, authpath, api_key, api_secret)
    resp_json = resp.json()
    return resp_json["access_token"]

def get_auth(baseurl, authpath, api_key, api_secret):
    auth_url = baseurl + authpath
    auth_header = HTTPBasicAuth(api_key, api_secret)
    resp = requests.get(auth_url, auth=(api_key, api_secret))
    print(resp.status_code)
    print(json.dumps(resp.json(), indent=4))
    return resp

def run():
    for org, nfo in endpoints.items():
        print(org, ":")
        print(f"BaseURL: {nfo['BaseURL']}")
        print(f"Auth: {nfo['BaseURL'] + nfo['AuthPath']}")
        access_token = get_access_token()
        print("Access Token:", access_token)
        for endpoint in nfo["APIEndpoints"]:
            endpoint_url = f"{nfo['BaseURL'] + nfo['APIPath']}/{endpoint}"
            print(f"Endpoint: {endpoint_url}")
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
        print("--"*20)


if __name__ == "__main__":
    run()
