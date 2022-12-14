import os
import configparser
import requests
import json
from datetime import datetime


CONFIG_NAME = "config.ini"
config = configparser.ConfigParser()
config.read(CONFIG_NAME)

print(config.sections())

for section in config.sections():
    for key in config[section]:
        print(section + ":" + key, "=", config.get(section, key))
