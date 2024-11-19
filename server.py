import socket
from utils.logger_config import logging
from utils.zone_loader import load_zone
from handlers.response_builder import build_response
from config.settings import IP,PORT

if __name__=="__main__":
    zonedata=load_zone()
    socket_udp=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    socket_udp.bind((IP,PORT))
    logging.info(f"DNS Server started on {IP}:{PORT}")

    while True:
        data,address=socket_udp.recvfrom(512)
        logging.info(f"Received request from {address} with data: {data.hex()}")
        response=build_response(data,zonedata)
        logging.info(f"Sending response to {address} with data: {response.hex()}")
        socket_udp.sendto(response,address)
        print(f"Received request from {address}")
        print(f"Sending response to {address}")
