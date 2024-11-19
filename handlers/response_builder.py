from utils.dns_utils import get_flags
from handlers.query_handler import get_records
from handlers.record_utils import build_question, records_to_bytes

def build_response(data,zonedata):
    TransactionID=data[:2]
    Flags=get_flags()
    records,recordtypes,domainname=get_records(data[12:],zonedata)
    QDCOUNT=b"\x00\x01"
    ANCOUNT=len(records).to_bytes(2,byteorder="big")
    NSCOUNT=(0).to_bytes(2,byteorder="big")
    ARCOUNT=(0).to_bytes(2,byteorder="big")
    header=TransactionID+Flags+QDCOUNT+ANCOUNT+NSCOUNT+ARCOUNT
    question=build_question(domainname,recordtypes)
    body=b""
    for record in records:
        body+=records_to_bytes(recordtypes,record["ttl"],record["value"])
    return header+question+body
