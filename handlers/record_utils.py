def build_question(domainname,rectype):
    qbytes=b""
    for part in domainname:
        length=len(part)
        qbytes+=bytes([length])+part.encode()
    qbytes+=b"\x00"
    if rectype=="a":
        qbytes+=b"\x00\x01"
    qbytes+=b"\x00\x01"
    return qbytes

def records_to_bytes(rectype,recttl,recval):
    rbytes=b"\xc0\x0c"
    if rectype=="a":
        rbytes+=b"\x00\x01"
    rbytes+=b"\x00\x01"
    rbytes+=int(recttl).to_bytes(4,byteorder="big")
    if rectype=="a":
        rbytes+=b"\x00\x04"
        for part in recval.split("."):
            rbytes+=bytes([int(part)])
    return rbytes