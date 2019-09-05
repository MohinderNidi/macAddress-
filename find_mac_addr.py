import ssl
import time
import urllib.request, json 
import click
import os
from dotenv import load_dotenv



#Reading env file
load_dotenv()
api_key = os.getenv("API_KEY")

@click.command()
@click.option('--macaddr', help='MacAdress to lookup', required=True)

def main(macaddr):
    """
    Program  output the Company Name associated with that MAC address

    Usage: python find_mac_addr.py --macaddr 44:38:39:ff:ef:57
    """
    
    context = ssl._create_unverified_context()
    
    # Query macaddr api to get information
    with urllib.request.urlopen(f'https://api.macaddress.io/v1?apiKey={api_key}&output=json&search={macaddr}', context=context) as url:
        data = json.loads(url.read().decode())
        print(data['vendorDetails']['companyName'])
    
if __name__ == '__main__':
    main()