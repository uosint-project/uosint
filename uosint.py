import argparse
from modules.email.leakcheck_net import leakcheck_email
from modules.UserName.username import Username_input
from modules.phone_number.phone import Phone_number_lookup


R = "\033[1;31m"
B = "\033[1;34m"
Y = "\033[1;33m"
G = "\033[1;32m"
RS = "\033[0m"
W = "\033[1;37m"
P = "\033[35m"
C = "\033[36m"
BL = "\033[1m"

parser = argparse.ArgumentParser()
parser.add_argument(
    "-e",
    "--email",
    help=(
        f"Sometime {P}USER{RS} write {P}Email{RS} in there {P}Bio{RS}, in that case you will take that Email {Y}.{RS}"
    ),
)
parser.add_argument(
    "-u",
    "--username",
    help=(
        f"Information will be collected from many website such as {G}Social Media{Y},{G}Dating Platfrom{Y},{G}Music Platfrom{Y},{G}Porn{Y},{RS} etc."
    ),
)
parser.add_argument(
    "-n",
    "--number",
    help=(
        f"Sometime USER write {P}Phone Number{RS} in there {P}Bio{Y},{RS} in that case you will take that phoneNumbe {Y}.{RS}"
    ),
)
parser.add_argument(
    "-i",
    "--info",
    help=(f"You can get a {P}Table{RS} show everything to you need to run this tools"),
    action="store_true",
)
args = parser.parse_args()

email = args.email
username = args.username
number = args.number
info = args.info

if args.email:
    leakcheck_email(email=email)
if args.username:
    Username_input(usernames=username)
if args.number:
    Phone_number_lookup(number=number)
if args.info:
    from modules import info
