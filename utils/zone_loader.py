import glob
import json
from config.settings import ZONE_PATH

def load_zone():
    jsonzone={}
    zonefiles=glob.glob(f"{ZONE_PATH}/resource_records.zone")
    for zone in zonefiles:
        with open(zone) as zonedata:
            data=json.load(zonedata)
            for entry in data:
                zonename=entry.get("$origin","")
                if zonename:
                    jsonzone[zonename]=entry
    return jsonzone
