import json
from datetime import date

import requests

R = "\033[1;31m"
B = "\033[1;34m"
Y = "\033[1;33m"
G = "\033[1;32m"
RS = "\033[0m"
W = "\033[1;37m"
P = "\033[35m"
C = "\033[36m"
BL = "\033[1m"


def leakcheck_email(email):
    today = date.today()
    Today_Date = today.strftime("%B %d, %Y")
    print(
        f"""
         {R}___  ____ ____{B} ____ ____ _  _ {RS}
         {R}|__] |__/ |___ {B}|__| |    |__| {RS}
         {R}|__] |  \ |___ {B}|  | |___ |  | {RS}

         Github {Y}:{RS} https://github.com/naimkowshik
         {B}NOW {Y}:{RS} {Today_Date}  {B}Version {Y}:{C} 1{Y}.{C}0{RS}
         {B}Status {Y}:{RS} This Tool Is Still In Development Mode 〽️
    """
    )

    LEAKCHECK_API = "49535f49545f5245414c4c595f4150495f4b4559"

    url = f"https://leakcheck.net/api/public?key={LEAKCHECK_API}&check={email}"

    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.33",
    }

    leakcheck_request = requests.request("GET", url, headers=headers)

    leakcheck_json = json.loads(leakcheck_request.content)

    if leakcheck_json["success"] == True:
        print(f" \n         [{B} Email {RS}]{Y}:{RS} {email} {C}[{R} BREACH {C}]{RS}")
        print(f"         [{B} Found {RS}]{Y}:{RS} {leakcheck_json['found']}")
        print(f"         [{B} Passwords {RS}]{Y}:{RS} {leakcheck_json['passwords']}")
        print(f"         [{B} Sources {RS}]{RS}")
        for sources in leakcheck_json["sources"]:
            print(f"\n{' ' * 5}         └[{B} Name {RS}]{Y}:{RS} {sources['name']}")
            print(f"{' ' * 5}         └[{B} Date {RS}]{Y}:{RS} {sources['date']} \n")

    elif leakcheck_json["success"] == False:
        print(f"         {B}Email{Y} :{RS} {email} {C}[{G} CLEAR {C}]{RS}\n")
