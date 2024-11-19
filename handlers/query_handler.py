from utils.dns_utils import get_question_domain

def get_zone(domain,zonedata):
    zone_name=".".join(domain)+"."
    return zonedata.get(zone_name)

def get_records(data,zonedata):
    domain,questiontype=get_question_domain(data)
    rectype=""
    if questiontype==b"\x00\x01":
        rectype="a"
    zone=get_zone(domain,zonedata)
    if zone and rectype in zone:
        return zone[rectype],rectype,domain
    else:
        return [],rectype,domain