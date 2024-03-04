from EspApi import EspApi
import argparse
import json
import sys

token = ""
try:
    with open("config/token.txt", "r") as f:
        token = f.readline().strip()
except:
    print("Token file not found.")
    token = input("What is your token? ")
    with open("config/token.txt", "w") as f:
        f.write(token)
    sys.exit(0)

area_id = ""
try:
    with open("config/area-id.txt", "r") as f:
        area_id = f.readline().strip()
except:
    print("Area ID not found.")
    area_id = input("What is your area ID?")
    with open("config/area-id.txt", "w") as f:
        f.write(area_id)
    sys.exit(0)

esp = EspApi(token)
print(json.dumps(esp.area(area_id), indent=4))