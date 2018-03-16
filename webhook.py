import requests
import json

def responder(request.POST):
  data = request.POST
  if data["challenge"]:
    return data["challenge"]
  else:
    retrun "Error!!"

responder(request.POST)
