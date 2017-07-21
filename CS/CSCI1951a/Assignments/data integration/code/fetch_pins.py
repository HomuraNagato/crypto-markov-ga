#!/usr/bin/env python
import requests
import json
import csv
from pinterest import PinterestAPI

access_token = '' # Fill this in!

p = PinterestAPI(access_token)
data = p.get_all_board_pins('bdatascience/ikea')
with open('../data/pinterest.json', 'w') as f:
    json.dump(data, f)
