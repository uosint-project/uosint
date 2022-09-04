import json, requests
from datetime import date

R = "\033[1;31m"
B = "\033[1;34m"
Y = "\033[1;33m"
G = "\033[1;32m"
RS = "\033[0m"
W = "\033[1;37m"
P = "\033[35m"
C = '\033[36m'
BL = '\033[1m'


def Phone_number_lookup(number):

    today = date.today()
    Today_Date = today.strftime("%B %d, %Y")
    print(f"""
         {B}___  _  _ ____ _  _ ____    {R}_  _ _  _ _  _ ___  ____ ____ {RS}
         {B}|__] |__| |  | |\ | |___    {R}|\ | |  | |\/| |__] |___ |__/ {RS}
         {B}|    |  | |__| | \| |___    {R}| \| |__| |  | |__] |___ |  \ {RS}

         Github {Y}:{RS} https://github.com/naimkowshik 
         {B}NOW {Y}:{RS} {Today_Date}  {B}Version {Y}:{C} 1{Y}.{C}0{RS}
         {B}Status {Y}:{RS} This Tool Is Still In Development Mode 〽️
    """)

    url = f"https://demo.phone-number-api.com/json/?number={number}"

    pnlp_request = requests.request("GET", url)

    pnlp_json = json.loads(pnlp_request.content)

    if pnlp_json['status'] == 'success':
        if (not pnlp_json['numberType']):
            print(f"{C}[{RS} {B}Number Type {C}]{RS} {Y}: {R}❌{RS}")
        else:
            print(f"{C}[{RS} {B}Number Type {C}]{RS} {Y}: {RS}{pnlp_json['numberType']}")

        if (not pnlp_json['numberValid']):
            print(f"{C}[{RS} {B}Number Valid {C}]{RS} {Y}: {R}❌{RS}")
        else:
            print(f"{C}[{RS} {B}Number Valid {C}]{RS} {Y}: {RS}{pnlp_json['numberValid']} ✔️ ")

        if (not pnlp_json['numberValidForRegion']):
            print(f"{C}[{RS} {B}Number Valid For Region {C}]{RS} {Y}: {R}❌{RS}")
        else:
            print(f"{C}[{RS} {B}Number Valid For Region {C}]{RS} {Y}: {RS}{pnlp_json['numberValidForRegion']} ✔️ ")

        if (not pnlp_json['numberCountryCode']):
            print(f"{C}[{RS} {B}Number Country Code {C}]{RS} {Y}: {R}❌{RS}")
        else:
            print(f"{C}[{RS} {B}Number Country Code {C}]{RS} {Y}: {RS}{pnlp_json['numberCountryCode']}")

        if (not pnlp_json['numberAreaCode']):
            print(f"{C}[{RS} {B}Number Area Code {C}]{RS} {Y}: {R}❌{RS}")
        else:
            print(f"{C}[{RS} {B}Number Area Code {C}]{RS} {Y}: {RS}{pnlp_json['numberAreaCode']}")

        if (not pnlp_json['ext']):
            print(f"{C}[{RS} {B}Ext {C}]{RS} {Y}: {R}❌{RS}")
        else:
            print(f"{C}[{RS} {B}Ext {C}]{RS} {Y}: {RS}{pnlp_json['ext']}")

        if (not pnlp_json['formatE164']):
            print(f"{C}[{RS} {B}FormatE164 {C}]{RS} {Y}: {R}❌{RS}")
        else:
            print(f"{C}[{RS} {B}FormatE164 {C}]{RS} {Y}: {RS}{pnlp_json['formatE164']}")

        if (not pnlp_json['formatNational']):
            print(f"{C}[{RS} {B}Format National {C}]{RS} {Y}: {R}❌{RS}")
        else:
            print(f"{C}[{RS} {B}Format National {C}]{RS} {Y}: {RS}{pnlp_json['formatNational']}")

        if (not pnlp_json['formatInternational']):
            print(f"{C}[{RS} {B}Format International {C}]{RS} {Y}: {R}❌{RS}")
        else:
            print(f"{C}[{RS} {B}Format International {C}]{RS} {Y}: {RS}{pnlp_json['formatInternational']}")

        if (not pnlp_json['carrier']):
            print(f"{C}[{RS} {B}Carrier {C}]{RS} {Y}: {R}❌{RS}")
        else:
            print(f"{C}[{RS} {B}Carrier {C}]{RS} {Y}: {RS}{pnlp_json['carrier']}")

        if (not pnlp_json['continent']):
            print(f"{C}[{RS} {B}Continent {C}]{RS} {Y}: {R}❌{RS}")
        else:
            print(f"{C}[{RS} {B}Continent {C}]{RS} {Y}: {RS}{pnlp_json['continent']}")

        if (not pnlp_json['countryName']):
            print(f"{C}[{RS} {B}Country Name {C}]{RS} {Y}: {R}❌{RS}")
        else:
            print(f"{C}[{RS} {B}Country Name {C}]{RS} {Y}: {RS}{pnlp_json['countryName']}")

        if (not pnlp_json['region']):
            print(f"{C}[{RS} {B}Region {C}]{RS} {Y}: {R}❌{RS}")
        else:
            print(f"{C}[{RS} {B}Region {C}]{RS} {Y}: {RS}{pnlp_json['region']}")

        if (not pnlp_json['regionName']):
            print(f"{C}[{RS} {B}Region Name {C}]{RS} {Y}: {R}❌{RS}")
        else:
            print(f"{C}[{RS} {B}Region Name {C}]{RS} {Y}: {RS}{pnlp_json['regionName']}")

        if (not pnlp_json['city']):
            print(f"{C}[{RS} {B}City Name {C}]{RS} {Y}: {R}❌{RS}")
        else:
            print(f"{C}[{RS} {B}City Name {C}]{RS} {Y}: {RS}{pnlp_json['city']}")

        if (not pnlp_json['zip']):
            print(f"{C}[{RS} {B}Zip Name {C}]{RS} {Y}: {R}❌{RS}")
        else:
            print(f"{C}[{RS} {B}Zip Name {C}]{RS} {Y}: {RS}{pnlp_json['zip']}")

        if (not pnlp_json['offset']):
            print(f"{C}[{RS} {B}Offset {C}]{RS} {Y}: {R}❌{RS}")
        else:
            print(f"{C}[{RS} {B}Offset {C}]{RS} {Y}: {RS}{pnlp_json['offset']}")

        if (not pnlp_json['timezone']):
            print(f"{C}[{RS} {B}Time Zone {C}]{RS} {Y}: {R}❌{RS}")
        else:
            print(f"{C}[{RS} {B}Time Zone {C}]{RS} {Y}: {RS}{pnlp_json['timezone']}")

        if (not pnlp_json['currency']):
            print(f"{C}[{RS} {B}Currency {C}]{RS} {Y}: {R}❌{RS}")
        else:
            print(f"{C}[{RS} {B}Currency {C}]{RS} {Y}: {RS}{pnlp_json['currency']}")

    if pnlp_json['status'] == 'fail':
        print(f"{C}[{RS} {B}Message {C}]{RS} {Y}:{RS} {pnlp_json['message']} {Y}&{RS} Check number again {R}❌{RS}")

if __name__ == "__main__":
    Phone_number_lookup()
