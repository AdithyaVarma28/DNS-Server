def get_flags():
    QR=1
    OPCODE=0
    AA=1
    TC=0
    RD=1
    RA=0
    Z=0
    RCODE=0
    byte1=(QR<<7) | (OPCODE<<3) | (AA<<2) | (TC<<1) | RD
    byte2=(RA<<7) | (Z<<4) | RCODE
    return bytes([byte1,byte2])

def get_question_domain(data):
    state=0
    expectedlength=0
    domainstring=""
    domainparts=[]
    x,y=0,0
    for byte in data:
        if state==1:
            if byte!=0:
                domainstring+=chr(byte)
            x+=1
            if x==expectedlength:
                domainparts.append(domainstring)
                domainstring=""
                state,x=0,0
        else:
            state=1
            expectedlength=byte
        y+=1
        if byte==0:
            break
    questiontype=data[y:y+2]
    return domainparts,questiontype