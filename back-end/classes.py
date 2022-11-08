from flask import Flask, request
import requests
import json

app = Flask(__name__)

Soc_response = requests.get("https://api.peterportal.org/rest/v0/schedule/soc?term=2018%20Fall&department=COMPSCI&courseNumber=161")# Retrieving Schedule of Classes information from Peterportal API
ClassInfo = Soc_response.json()
print(ClassInfo)