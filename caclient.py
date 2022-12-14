import os
import configparser
import json
import requests
from requests.auth import HTTPBasicAuth
from datetime import datetime


AUTH_CONFIG_NAME = "auth.ini"
auth_conf = configparser.ConfigParser()
auth_conf.read(AUTH_CONFIG_NAME)

BASE_URL = auth_conf.get("DEFAULT", "BaseURL")
AUTH_PATH = auth_conf.get("DEFAULT", "AuthPath")
API_KEY = auth_conf.get("DEFAULT", "APIKey")
API_SECRET = auth_conf.get("DEFAULT", "APISecret")

config = configparser.ConfigParser()
config.read("config.ini")


ENDPOINTS = ["projects"]

print(config.sections())

for section in config.sections():
    part = config[section]
    base_url = part.get("URL", "None")
    print(f"Base_URL: {base_url}")
    for key in part:
        if key.lower() != "url":
            print(f"{base_url}{part.get(key)}")

def get_auth_response():
    auth_url = BASE_URL + AUTH_PATH
    auth_header = HTTPBasicAuth(API_KEY, API_SECRET)
    resp = requests.get(auth_url, auth=auth_header)
    return resp

def run():
    cred_response = get_auth_response()
    print(cred_response)
    print(json.dumps(cred_response.json(), indent=4))
    


# if __name__ == "__main__":
#     run()
