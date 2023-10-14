import socket
import requests, time, json, os, urllib3, shutil
from requests.structures import CaseInsensitiveDict

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from bs4 import BeautifulSoup
import cssutils
import re
from datetime import date

#############################
#    COLORING YOUR SHELL    #
#############################
R = "\033[1;31m"
B = "\033[1;34m"
Y = "\033[1;33m"
G = "\033[1;32m"
RS = "\033[0m"
W = "\033[1;37m"
P = "\033[35m"
C = "\033[36m"
BL = "\033[1m"


def Username_input(usernames):

    today = date.today()
    Today_Date = today.strftime("%B %d, %Y")
    print(
        f"""
     {B}_  _ {R}____ ____ _ _  _ ___ {RS}
     {B}|  | {R}|  | [__  | |\ |  |  {RS}
     {B}|__| {R}|__| ___] | | \|  |  {RS}

     Github {Y}:{RS} https://github.com/uosint-project/uosint 
     {B}NOW {Y}:{RS} {Today_Date}  {B}Version {Y}:{C} 1{Y}.{C}0{RS}
     {B}Status {Y}:{RS} This Tool Is Still In Development Mode 〽️
    """
    )

    try:
        ip_address = socket.gethostbyname("facebook.com")
        # print('IP address:', ip_address)
        try:
            response = requests.get("https://www.facebook.com", timeout=5)
            if response.status_code == 200:
                Facebook_Url = f"https://www.facebook.com/{usernames}"

                Facebook_Request = requests.get(Facebook_Url)

                if Facebook_Request.status_code == 200:

                    print(f"\n[{B} FACEBOOK{RS} ]")

                    print(f"{' ' * 5}└[{R}•{RS}] {C}User Url {Y}:{RS} {Facebook_Url}")

                    Facebook_Soup = BeautifulSoup(Facebook_Request.text, "html.parser")

                    full_name_tag = Facebook_Soup.find_all("title")

                    for FULL_NAME in full_name_tag:
                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {FULL_NAME.string}"
                        )

                elif Facebook_Request.status_code == 404:
                    print(f"[{B} FACEBOOK{RS} ]")
                    print(
                        f"{' ' * 5}└[{R}•{RS}] {C}User Info{Y}:{RS} {R}Sorry, we couldn't find that one ❗️{RS}"
                    )
            else:
                print(f"\n[{B} FACEBOOK{RS} ]")
                print(
                    f"{' ' * 5}└[{R}•{RS}] {C}Connection Lost{Y}:{RS} {R}Oops! Unable To Establish A Connection{RS}"
                )
        except requests.exceptions.Timeout:
            print(f"\n[{B} FACEBOOK{RS} ]")
            print(
                f"{' ' * 5}└[{R}•{RS}] {C}Timeout Error{Y}:{RS} {R}Oops! Timed Out{RS}"
            )
    except socket.gaierror:
        print(f"\n[{B} FACEBOOK{RS} ]")
        print(
            f"{' ' * 5}└[{R}•{RS}] {C}DNS LookUp{Y}:{RS} {R}Oops! The {G}Dns Lookup{R} Failed And The Requested Domain Could Not Be Found.{RS}"
        )

    # [ Twitter ]

    try:
        ip_address = socket.gethostbyname("nitter.net")
        # print('IP address:', ip_address)
        try:
            response = requests.get("https://nitter.net", timeout=5)
            if response.status_code == 200:
                Twitter_Url = f"https://nitter.net/{usernames}"

                Twitter_Request = requests.request("GET", Twitter_Url)

                if Twitter_Request.status_code == 200:
                    print(f"\n[{B} TWITTER{RS} ]")

                    Twitter_Soup = BeautifulSoup(Twitter_Request.text, "html.parser")

                    full_name_tag = Twitter_Soup.find_all(
                        class_="profile-card-fullname"
                    )
                    username_tag = Twitter_Soup.find_all(class_="profile-card-username")
                    User_Bio_tag = Twitter_Soup.find_all(class_="profile-bio")
                    User_Joined_tag = Twitter_Soup.find_all(class_="profile-joindate")
                    Tweets_Following_Followers_Likes_tag = Twitter_Soup.find_all(
                        class_="profile-stat-num"
                    )
                    User_Location = Twitter_Soup.find_all(class_="profile-location")
                    User_Website_tag = Twitter_Soup.find_all(class_="profile-website")
                    title = Twitter_Soup.find_all(span_="title")
                    verified_twitter = Twitter_Soup.find_all(
                        class_="icon-ok verified-icon"
                    )
                    suspended_twitters = Twitter_Soup.find_all(class_="error-panel")

                    if not suspended_twitters:

                        print(
                            f"{' ' * 5}└[{R}•{RS}] {C}User Url{Y}:{RS} {f'https://twitter.com/{usernames}'}"
                        )

                        if not full_name_tag:
                            print(
                                f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {R}Not Found ❌ {RS}"
                            )
                        else:
                            print(
                                f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name  {Y}:{RS} {full_name_tag[0].getText()}"
                            )

                        if not username_tag:
                            print(
                                f"{' ' * 5}└[{Y}•{RS}] {C}UserName {Y}:{RS} {R}Not Found ❌ {RS}"
                            )
                        else:
                            print(
                                f"{' ' * 5}└[{Y}•{RS}] {C}UserName {Y}:{RS} {username_tag[0].getText()}"
                            )

                        if not User_Joined_tag:
                            print(
                                f"{' ' * 5}└[{G}•{RS}] {C}User Joined {Y}:{RS} {R}Not Found ❌ {RS}"
                            )
                        else:
                            print(
                                f"{' ' * 5}└[{G}•{RS}] {C}User Joined {Y}:{RS} {User_Joined_tag[0].getText()}"
                            )

                        if not Tweets_Following_Followers_Likes_tag:
                            print(
                                f"{' ' * 5}└[{R}•{RS}] {C}User Tweets {Y}:{RS} {R}Not Found ❌ {RS}"
                            )
                        else:
                            print(
                                f"{' ' * 5}└[{R}•{RS}] {C}User Tweets {Y}:{RS} {Tweets_Following_Followers_Likes_tag[0].getText()}"
                            )

                        if not Tweets_Following_Followers_Likes_tag:
                            print(
                                f"{' ' * 5}└[{B}•{RS}] {C}User Following {Y}:{RS} {R}Not Found ❌ {RS}"
                            )
                        else:
                            print(
                                f"{' ' * 5}└[{B}•{RS}] {C}User Following {Y}:{RS} {Tweets_Following_Followers_Likes_tag[1].getText()}"
                            )

                        if not Tweets_Following_Followers_Likes_tag:
                            print(
                                f"{' ' * 5}└[{Y}•{RS}] {C}User Followers {Y}:{RS} {R}Not Found ❌ {RS}"
                            )
                        else:
                            print(
                                f"{' ' * 5}└[{Y}•{RS}] {C}User Followers {Y}:{RS} {Tweets_Following_Followers_Likes_tag[2].getText()}"
                            )

                        if not Tweets_Following_Followers_Likes_tag:
                            print(
                                f"{' ' * 5}└[{Y}•{RS}] {C}User Likes {Y}:{RS} {R}Not Found ❌ {RS}"
                            )
                        else:
                            print(
                                f"{' ' * 5}└[{Y}•{RS}] {C}User Likes {Y}:{RS} {Tweets_Following_Followers_Likes_tag[3].getText()}"
                            )

                        if not User_Bio_tag:
                            print(
                                f"{' ' * 5}└[{R}•{RS}] {C}User Bio {Y}:{RS} {R}Not Found ❌ {RS}"
                            )
                        else:
                            print(
                                f"{' ' * 5}└[{R}•{RS}] {C}User Bio {Y}:{RS} {User_Bio_tag[0].getText()}"
                            )

                            UserMention_Bio = User_Bio_tag[0].getText()

                            Mention_Bio = re.findall(
                                r"@[A-Za-z0-9.-]+", UserMention_Bio
                            )

                            print(
                                f"{' ' * 5}└[{Y}•{RS}] {C}List Of People Mention On USER Bio{Y}:{RS}"
                            )

                            if not Mention_Bio:
                                print(
                                    f"{' ' * 20}└[{R}•{RS}] {Y}Mention Pople {C}On Bio {Y}:{RS} {R}Not Found ❗️{RS} \n"
                                )
                            else:
                                count = 0
                                for Mention_Bios in Mention_Bio:
                                    count += 1
                                    print(
                                        f"{' ' * 20}└[{R}{count}{RS}] {G}►{RS} {Mention_Bios}"
                                    )

                            UserEmail = User_Bio_tag[0].getText()

                            emails = re.findall(r"[\w\.-]+@[\w\.-]+", UserEmail)

                            print(
                                f"{' ' * 5}└[{G}•{RS}] {C}List Of Email Write On USER Bio{Y}:{RS}"
                            )

                            if not emails:
                                print(
                                    f"{' ' * 20}└[{R}•{RS}] {C}Find {Y}Email {C}On Bio {Y}:{RS} {R}Not Found ❗️{RS} \n"
                                )
                            else:
                                count = 0
                            for email in emails:
                                count += 1
                                print(f"{' ' * 20}└[{R}{count}{RS}] {G}►{RS} {email}")

                            print(
                                f"{' ' * 5}└[{R}•{RS}] {C}List Of PhoneNumber Or Any Digit On USER Bio{Y}:{RS}"
                            )

                            PhoneNumberbio = User_Bio_tag[0].getText()

                            PhoneNumbers = re.findall(r"\d+", PhoneNumberbio)

                            if not PhoneNumbers:
                                print(
                                    f"{' ' * 20}└[{R}•{RS}] {C}Find {Y}PhoneNumber {C}On Bio {Y}:{RS} {R}Not Found ❗️{RS} "
                                )
                            else:
                                count = 0
                            for PhoneNumber in PhoneNumbers:
                                count += 1
                                print(
                                    f"{' ' * 20}└[{R}{count}{RS}] {G}►{RS} {PhoneNumber}"
                                )

                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}User Suspended {Y}:{RS} [ {G}LIVE{RS} ] {RS}"
                        )

                    else:
                        print(
                            f"{' ' * 5}└[{R}•{RS}] {C}User Suspended {Y}:{RS} {suspended_twitters[0].getText()}"
                        )

                elif Twitter_Request.status_code == 404:
                    print(f"\n[{B} TWITTER{RS} ]")
                    print(
                        f"{' ' * 5}└[{R}•{RS}] {C}User Info {Y}:{RS} {R}Not Found ❗️{RS}"
                    )
            else:
                print(f"\n[{B} TWITTER{RS} ]")

                print(
                    f"{' ' * 5}└[{R}•{RS}] {C}Connection Lost{Y}:{RS} {R}Oops! Unable To Establish A Connection{RS}"
                )
        except requests.exceptions.Timeout:
            print(f"\n[{B} TWITTER{RS} ]")

            print(
                f"{' ' * 5}└[{R}•{RS}] {C}Timeout Error{Y}:{RS} {R}Oops! Timed Out{RS}"
            )
    except socket.gaierror:
        print(f"\n[{B} TWITTER{RS} ]")

        print(
            f"{' ' * 5}└[{R}•{RS}] {C}DNS LookUp{Y}:{RS} {R}Oops! The {G}Dns Lookup{R} Failed And The Requested Domain Could Not Be Found.{RS}"
        )

    # [ YouTube ]

    try:
        ip_address = socket.gethostbyname("youtube.com")
        # print('IP address:', ip_address)
        try:
            response = requests.get("https://www.youtube.com", timeout=5)
            if response.status_code == 200:
                YouTube_Url = f"https://www.youtube.com/user/{usernames}"

                YouTube_Request = requests.request("GET", YouTube_Url)

                if YouTube_Request.status_code == 200:
                    print(f"\n[{B} YouTube{RS} ]")
                    print(f"{' ' * 5}└[{R}•{RS}] {C}User Url{Y}:{RS} {YouTube_Url}")

                    YouTube_Soup = BeautifulSoup(YouTube_Request.text, "html.parser")

                    full_name_YouTube_tag = YouTube_Soup.find_all("title")

                    if not full_name_YouTube_tag:
                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}User Name {Y}:{RS} {R}Not Found ❌ {RS}"
                        )
                    else:
                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}User Name {Y}:{RS} {full_name_YouTube_tag[0].getText()}"
                        )

                elif YouTube_Request.status_code == 404:
                    print(f"\n[{B} YouTube{RS} ]")
                    print(
                        f"{' ' * 5}└[{R}•{RS}] {C}User Info{Y}:{RS} {R}Sorry, we couldn't find that one ❗️{RS}"
                    )

            else:
                print(f"\n[{B} YouTube{RS} ]")

                print(
                    f"{' ' * 5}└[{R}•{RS}] {C}Connection Lost{Y}:{RS} {R}Oops! Unable To Establish A Connection{RS}"
                )
        except requests.exceptions.Timeout:
            print(f"\n[{B} YouTube{RS} ]")

            print(
                f"{' ' * 5}└[{R}•{RS}] {C}Timeout Error{Y}:{RS} {R}Oops! Timed Out{RS}"
            )
    except socket.gaierror:
        print(f"\n[{B} YouTube{RS} ]")

        print(
            f"{' ' * 5}└[{R}•{RS}] {C}DNS LookUp{Y}:{RS} {R}Oops! The {G}Dns Lookup{R} Failed And The Requested Domain Could Not Be Found.{RS}"
        )

    # [ VIMEO ]

    try:
        ip_address = socket.gethostbyname("vimeo.com")
        # print('IP address:', ip_address)
        try:
            response = requests.get("https://vimeo.com", timeout=5)
            if response.status_code == 200:
                headers = {
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.33",
                }

                VIMEO_Url = f"https://vimeo.com/{usernames}"

                VIMEO_Request = requests.get(VIMEO_Url, headers=headers)

                if VIMEO_Request.status_code == 200:
                    print(f"\n[{B} VIMEO{RS} ]")

                    print(f"{' ' * 5}└[{R}•{RS}] {C}User Url {Y}:{RS} {VIMEO_Url}")

                    VIMEO_Url = f"https://vimeo.com/{usernames}/collections"

                    VIMEO_Requestss = requests.get(VIMEO_Url, headers=headers)

                    VIMEO_Soupssss = BeautifulSoup(VIMEO_Requestss.text, "html.parser")

                    all = VIMEO_Soupssss.find_all("p", class_="super_link_list_title")

                    VIMEO_SOups = BeautifulSoup(VIMEO_Request.text, "html.parser")

                    VIMEO_Url = (
                        f"https://vimeo.com/{usernames}/following/followers/sort:date"
                    )

                    VIMEO_Requests = requests.get(VIMEO_Url, headers=headers)

                    VIMEO_Soups = BeautifulSoup(VIMEO_Requests.text, "html.parser")

                    Following_Followers = VIMEO_Soups.find_all(
                        "div", class_="js-tabs tab_bar"
                    )

                    Following_Followers = Following_Followers[0].getText()
                    Following_Followers_result = Following_Followers.strip()

                    VIMEO_Soup = BeautifulSoup(VIMEO_Request.text, "html.parser")

                    name_PERISCOPE = VIMEO_Soup.find("meta", property="og:title")

                    Description_PERISCOPE = VIMEO_Soup.find(
                        "meta", property="og:description"
                    )

                    print(
                        f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {name_PERISCOPE['content']}"
                    )
                    print(
                        f"{' ' * 5}└[{Y}•{RS}] {C}User Description {Y}:{RS} {Description_PERISCOPE['content']}"
                    )

                    UserMention_Bio = Description_PERISCOPE["content"]

                    Mention_Bio = re.findall(r"@[A-Za-z0-9.-]+", UserMention_Bio)

                    print(
                        f"{' ' * 5}└[{B}•{RS}] {C}List Of People Mention On USER Description{Y}:{RS}"
                    )

                    if not Mention_Bio:
                        print(
                            f"{' ' * 20}└[{R}•{RS}] {Y}Mention Pople {C}On Description {Y}:{RS} {R}Not Found ❗️{RS} \n"
                        )
                    else:
                        count = 0
                        for Mention_Bios in Mention_Bio:
                            count += 1
                            print(
                                f"{' ' * 20}└[{R}{count}{RS}] {G}►{RS} {Mention_Bios}"
                            )

                    UserEmail = Description_PERISCOPE["content"]

                    emails = re.findall(r"[\w\.-]+@[\w\.-]+", UserEmail)

                    print(
                        f"{' ' * 5}└[{B}•{RS}] {C}List Of Email Write On USER Description{Y}:{RS}"
                    )

                    if not emails:
                        print(
                            f"{' ' * 20}└[{R}•{RS}] {C}Find {Y}Email {C}On Description {Y}:{RS} {R}Not Found ❗️{RS} \n"
                        )
                    else:
                        count = 0
                    for email in emails:
                        count += 1
                        print(f"{' ' * 20}└[{R}{count}{RS}] {G}►{RS} {email}")

                    print(
                        f"{' ' * 5}└[{B}•{RS}] {C}List Of PhoneNumber Or Any Digit On USER Description{Y}:{RS}"
                    )

                    PhoneNumberbio = Description_PERISCOPE["content"]

                    PhoneNumbers = re.findall(r"\d+", PhoneNumberbio)

                    if not PhoneNumbers:
                        print(
                            f"{' ' * 20}└[{R}•{RS}] {C}Find {Y}PhoneNumber {C}On Description {Y}:{RS} {R}Not Found ❗️{RS} "
                        )
                    else:
                        count = 0
                    for PhoneNumber in PhoneNumbers:
                        count += 1
                        print(f"{' ' * 20}└[{R}{count}{RS}] {G}►{RS} {PhoneNumber}")

                if VIMEO_Request.status_code == 404:
                    print(f"\n[{B} VIMEO{RS} ]")
                    print(
                        f"{' ' * 5}└[{R}•{RS}] {C}User Info{Y}:{RS} {R}Sorry, we couldn't find that one ❗️{RS}"
                    )

            else:
                print(f"\n[{B} VIMEO{RS} ]")

                print(
                    f"{' ' * 5}└[{R}•{RS}] {C}Connection Lost{Y}:{RS} {R}Oops! Unable To Establish A Connection{RS}"
                )
        except requests.exceptions.Timeout:
            print(f"\n[{B} VIMEO{RS} ]")

            print(
                f"{' ' * 5}└[{R}•{RS}] {C}Timeout Error{Y}:{RS} {R}Oops! Timed Out{RS}"
            )
    except socket.gaierror:
        print(f"\n[{B} VIMEO{RS} ]")

        print(
            f"{' ' * 5}└[{R}•{RS}] {C}DNS LookUp{Y}:{RS} {R}Oops! The {G}Dns Lookup{R} Failed And The Requested Domain Could Not Be Found.{RS}"
        )

    # [ Caffeine_TV ]

    try:
        ip_address = socket.gethostbyname(f"api.caffeine.tv")
        # print('IP address:', ip_address)
        try:
            response = requests.get(
                f"https://api.caffeine.tv/v1/users/{usernames}", timeout=5
            )
            if response.status_code == 200:
                headers = {
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.33",
                }

                url = f"https://api.caffeine.tv/v1/users/{usernames}"

                Caffeine_TV_Request = requests.request("GET", url, headers=headers)

                if Caffeine_TV_Request.status_code == 200:
                    Caffeine_TV_Data = json.loads(Caffeine_TV_Request.content)
                    print(f"\n[{B} CAFFEINE_TV{RS} ]")
                    print(
                        f"{' ' * 5}└[{R}•{RS}] {C}User Url {Y}:{RS} {f'https://www.caffeine.tv/{usernames}/profile'}"
                    )
                    print(
                        f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {Caffeine_TV_Data['user']['name']}"
                    )
                    print(
                        f"{' ' * 5}└[{Y}•{RS}] {C}UserName {Y}:{RS} {Caffeine_TV_Data['user']['username']}"
                    )
                    print(
                        f"{' ' * 5}└[{G}•{RS}] {C}User Following {Y}:{RS} {Caffeine_TV_Data['user']['following_count']}"
                    )
                    print(
                        f"{' ' * 5}└[{R}•{RS}] {C}User Followers {Y}:{RS} {Caffeine_TV_Data['user']['followers_count']}"
                    )
                    print(
                        f"{' ' * 5}└[{B}•{RS}] {C}User Badge {Y}:{RS} {Caffeine_TV_Data['user']['badge']}"
                    )

                elif Caffeine_TV_Request.status_code == 404:
                    print(f"\n[{B} CAFFEINE_TV{RS} ]")
                    print(
                        f"{' ' * 5}└[{R}•{RS}] {C}User Info{Y}:{RS} {R}Sorry, we couldn't find that one ❗️{RS}"
                    )

            else:
                print(f"\n[{B} CAFFEINE_TV{RS} ]")

                print(
                    f"{' ' * 5}└[{R}•{RS}] {C}Connection Lost{Y}:{RS} {R}Oops! Unable To Establish A Connection{RS}"
                )
        except requests.exceptions.Timeout:
            print(f"\n[{B} CAFFEINE_TV{RS} ]")

            print(
                f"{' ' * 5}└[{R}•{RS}] {C}Timeout Error{Y}:{RS} {R}Oops! Timed Out{RS}"
            )
    except socket.gaierror:
        print(f"\n[{B} CAFFEINE_TV{RS} ]")

        print(
            f"{' ' * 5}└[{R}•{RS}] {C}DNS LookUp{Y}:{RS} {R}Oops! The {G}Dns Lookup{R} Failed And The Requested Domain Could Not Be Found.{RS}"
        )

    # [ GITHUB ]

    try:
        ip_address = socket.gethostbyname("github.com")
        # print('IP address:', ip_address)
        try:
            response = requests.get("https://github.com", timeout=5)
            if response.status_code == 200:
                Github_Url = f"https://github.com/{usernames}"

                Github_Request = requests.get(Github_Url)

                if Github_Request.status_code == 200:

                    print(f"\n[{B} GITHUB{RS} ]")

                    print(f"{' ' * 5}└[{R}•{RS}] {C}User Url {Y}:{RS} {Github_Url}")

                    Github_Soup = BeautifulSoup(Github_Request.text, "html.parser")

                    full_name_Github_tag = Github_Soup.find_all(
                        class_="p-name vcard-fullname d-block overflow-hidden"
                    )
                    user_name_Github_tag = Github_Soup.find_all(
                        class_="p-nickname vcard-username d-block"
                    )
                    user_bio_Github_tag = Github_Soup.find_all(
                        class_="p-note user-profile-bio mb-3 js-user-profile-bio f4"
                    )
                    user_followers_Github_tag = Github_Soup.find_all(
                        class_="text-bold color-fg-default"
                    )
                    user_workfrom_organization_Github_tag = Github_Soup.find_all(
                        class_="p-org"
                    )
                    user_location_Github_tag = Github_Soup.find_all(class_="p-label")

                    # USer Full Name
                    if not full_name_Github_tag:
                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}User FullName {Y}:{RS} {R}Not Found ❌ {RS}"
                        )
                    else:
                        name_THERMI_NAME_SPACE_REMOVE = full_name_Github_tag[
                            0
                        ].getText()

                        name_THERMI_SPACE_REMOVE_RESULT = (
                            name_THERMI_NAME_SPACE_REMOVE.strip()
                        )

                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}User FullName {Y}:{RS} {name_THERMI_SPACE_REMOVE_RESULT}"
                        )

                    # User Followers
                    if not user_followers_Github_tag:
                        print(
                            f"{' ' * 5}└[{Y}•{RS}] {C}User Followers {Y}:{RS} {R}Not Found ❌ {RS}"
                        )
                    else:
                        name_THERMI_NAME_SPACE_REMOVE = user_followers_Github_tag[
                            0
                        ].getText()

                        name_THERMI_SPACE_REMOVE_RESULT = (
                            name_THERMI_NAME_SPACE_REMOVE.strip()
                        )

                        print(
                            f"{' ' * 5}└[{Y}•{RS}] {C}User Followers {Y}:{RS} {name_THERMI_SPACE_REMOVE_RESULT}"
                        )

                    # User location
                    if not user_location_Github_tag:
                        print(
                            f"{' ' * 5}└[{R}•{RS}] {C}User Location {Y}:{RS} {R}Not Found ❌ {RS}"
                        )
                    else:
                        name_THERMI_NAME_SPACE_REMOVE = user_location_Github_tag[
                            0
                        ].getText()

                        name_THERMI_SPACE_REMOVE_RESULT = (
                            name_THERMI_NAME_SPACE_REMOVE.strip()
                        )

                        print(
                            f"{' ' * 5}└[{R}•{RS}] {C}User Location {Y}:{RS} {name_THERMI_SPACE_REMOVE_RESULT}"
                        )

                    # User Working From
                    if not user_workfrom_organization_Github_tag:
                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}User Work Organization {Y}:{RS} {R}Not Found ❌ {RS}"
                        )
                    else:
                        name_THERMI_NAME_SPACE_REMOVE = (
                            user_workfrom_organization_Github_tag[0].getText()
                        )

                        name_THERMI_SPACE_REMOVE_RESULT = (
                            name_THERMI_NAME_SPACE_REMOVE.strip()
                        )

                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}User Work Organization {Y}:{RS} {name_THERMI_SPACE_REMOVE_RESULT}"
                        )

                    # User BIO
                    if not user_bio_Github_tag:
                        print(
                            f"{' ' * 5}└[{Y}•{RS}] {C}User Bio {Y}:{RS} {R}Not Found ❌ {RS}"
                        )
                    else:
                        name_THERMI_NAME_SPACE_REMOVE = user_bio_Github_tag[0].getText()

                        name_THERMI_SPACE_REMOVE_RESULT = (
                            name_THERMI_NAME_SPACE_REMOVE.strip()
                        )

                        print(
                            f"{' ' * 5}└[{Y}•{RS}] {C}User Bio {Y}:{RS} {name_THERMI_SPACE_REMOVE_RESULT}"
                        )

                        UserMention_Bio = name_THERMI_SPACE_REMOVE_RESULT

                        Mention_Bio = re.findall(r"@[A-Za-z0-9.-]+", UserMention_Bio)

                        print(
                            f"{' ' * 5}└[{G}•{RS}] {C}List Of People Mention On USER Bio{Y}:{RS}"
                        )

                        if not Mention_Bio:
                            print(
                                f"{' ' * 20}└[{R}•{RS}] {Y}Mention Pople {C}On Bio {Y}:{RS} {R}Not Found ❗️{RS} \n"
                            )
                        else:
                            count = 0
                            for Mention_Bios in Mention_Bio:
                                count += 1
                                print(
                                    f"{' ' * 20}└[{R}{count}{RS}] {G}►{RS} {Mention_Bios}"
                                )

                        UserEmail = name_THERMI_SPACE_REMOVE_RESULT

                        emails = re.findall(r"[\w\.-]+@[\w\.-]+", UserEmail)

                        print(
                            f"{' ' * 5}└[{R}•{RS}] {C}List Of Email Write On USER Bio{Y}:{RS}"
                        )

                        if not emails:
                            print(
                                f"{' ' * 20}└[{R}•{RS}] {C}Find {Y}Email {C}On Bio {Y}:{RS} {R}Not Found ❗️{RS} \n"
                            )
                        else:
                            count = 0
                        for email in emails:
                            count += 1
                            print(f"{' ' * 20}└[{R}{count}{RS}] {G}►{RS} {email}")

                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}List Of PhoneNumber Or Any Digit On USER Bio{Y}:{RS}"
                        )

                        PhoneNumberbio = name_THERMI_SPACE_REMOVE_RESULT

                        PhoneNumbers = re.findall(r"\d+", PhoneNumberbio)

                        if not PhoneNumbers:
                            print(
                                f"{' ' * 20}└[{R}•{RS}] {C}Find {Y}PhoneNumber {C}On Bio {Y}:{RS} {R}Not Found ❗️{RS} "
                            )
                        else:
                            count = 0
                        for PhoneNumber in PhoneNumbers:
                            count += 1
                            print(f"{' ' * 20}└[{R}{count}{RS}] {G}►{RS} {PhoneNumber}")

                elif Github_Request.status_code == 404:
                    print(f"\n[{B} GITHUB{RS} ]")
                    print(
                        f"{' ' * 5}└[{R}•{RS}] {C}User Info{Y}:{RS} {R}Sorry, we couldn't find that one ❗️{RS}"
                    )

            else:
                print(f"\n[{B} GITHUB{RS} ]")

                print(
                    f"{' ' * 5}└[{R}•{RS}] {C}Connection Lost{Y}:{RS} {R}Oops! Unable To Establish A Connection{RS}"
                )
        except requests.exceptions.Timeout:
            print(f"\n[{B} GITHUB{RS} ]")

            print(
                f"{' ' * 5}└[{R}•{RS}] {C}Timeout Error{Y}:{RS} {R}Oops! Timed Out{RS}"
            )
    except socket.gaierror:
        print(f"\n[{B} GITHUB{RS} ]")

        print(
            f"{' ' * 5}└[{R}•{RS}] {C}DNS LookUp{Y}:{RS} {R}Oops! The {G}Dns Lookup{R} Failed And The Requested Domain Could Not Be Found.{RS}"
        )

    # [ replit ]

    try:
        ip_address = socket.gethostbyname("replit.com")
        # print('IP address:', ip_address)
        try:
            response = requests.get("https://replit.com", timeout=5)
            if response.status_code == 200:
                replit_Url = f"https://replit.com/@{usernames}"

                Replit_Request = requests.request("GET", replit_Url)

                if Replit_Request.status_code == 200:
                    print(f"\n[{B} REPLIT{RS} ]")
                    print(f"{' ' * 5}└[{R}•{RS}] {C}User Url{Y}:{RS} {replit_Url}")
                    Replit_Soup = BeautifulSoup(Replit_Request.text, "html.parser")
                    full_name_Replit_tag = Replit_Soup.find_all("title")
                    print(
                        f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {full_name_Replit_tag[0].getText()}"
                    )

                elif Replit_Request.status_code == 404:
                    print(f"\n[{B} REPLIT{RS} ]")
                    print(
                        f"{' ' * 5}└[{R}•{RS}] {C}User Info{Y}:{RS} {R}Sorry, we couldn't find that one ❗️{RS}"
                    )

            else:
                print(f"\n[{B} REPLIT{RS} ]")

                print(
                    f"{' ' * 5}└[{R}•{RS}] {C}Connection Lost{Y}:{RS} {R}Oops! Unable To Establish A Connection{RS}"
                )
        except requests.exceptions.Timeout:
            print(f"\n[{B} REPLIT{RS} ]")

            print(
                f"{' ' * 5}└[{R}•{RS}] {C}Timeout Error{Y}:{RS} {R}Oops! Timed Out{RS}"
            )
    except socket.gaierror:
        print(f"\n[{B} REPLIT{RS} ]")

        print(
            f"{' ' * 5}└[{R}•{RS}] {C}DNS LookUp{Y}:{RS} {R}Oops! The {G}Dns Lookup{R} Failed And The Requested Domain Could Not Be Found.{RS}"
        )

    # [ Talegram ]

    try:
        ip_address = socket.gethostbyname("t.me")
        # print('IP address:', ip_address)
        try:
            response = requests.get("https://t.me", timeout=5)
            if response.status_code == 200:
                Telegram_Bot_Url = f"https://t.me/{usernames}_bot"

                Telegram_Request = requests.get(Telegram_Bot_Url)

                if Telegram_Request.status_code == 200:

                    print(f"\n[{B} TELEGRAM{RS} ]")

                    print(f"{' ' * 5}└[{G} BOT {RS}]")

                    print(
                        f"{' ' * 8}└[{R}•{RS}]{C}User Url {Y}:{RS} {Telegram_Bot_Url}"
                    )

                    Telegram_Soup = BeautifulSoup(Telegram_Request.text, "html.parser")

                    BOT_full_name_tag = Telegram_Soup.find_all(
                        "span", attrs={"dir": "auto"}
                    )

                    for FULL_NAME in BOT_full_name_tag:
                        print(
                            f"{' ' * 8}└[{B}•{RS}] {C}BOT Name {Y}:{RS} {FULL_NAME.string}"
                        )
                    full_name_tag = Telegram_Soup.find_all(
                        class_="tgme_page_description"
                    )
                    if full_name_tag:

                        def remove(string):
                            return string.replace(
                                """
                  """,
                                "",
                            )

                        string = full_name_tag[0].getText()
                        print(
                            f"{' ' * 8}└[{Y}•{RS}] {C}User Description {Y}:{RS} {remove(string)}"
                        )
                        print(
                            f"{' ' * 5}[{G} NOTE {RS}] [ {C}USER DESCRIPTION{RS} {Y}MEANS {G}NOT SURE THIS USER {R}EXISTS{RS} OR {R}NOT{RS} ] \n"
                        )

                elif Telegram_Request.status_code == 404:
                    print(f"\n└── {B}Telegram {R}✖{RS}")
                    print(f"{' ' * 5}├──{C}User Url {Y}:{RS} {R}Not Found ❗️{RS}")

                Telegram_USER_Url = f"https://t.me/{usernames}"

                Telegram_Request = requests.get(Telegram_USER_Url)

                print(f"{' ' * 5}└[{G} USER {RS}/{G} GROUP {RS}/{G} PAGE {RS}]")

                if Telegram_Request.status_code == 200:

                    print(
                        f"{' ' * 10}└[{R}•{RS}] {C}User Url {Y}:{RS} {Telegram_USER_Url}"
                    )

                    Telegram_Soup = BeautifulSoup(Telegram_Request.text, "html.parser")

                    user_full_name_tag_talegram = Telegram_Soup.find_all(
                        "span", attrs={"dir": "auto"}
                    )
                    full_name_tag_talegram = Telegram_Soup.find_all(
                        class_="tgme_page_description"
                    )
                    Group_member_and_online_talegram = Telegram_Soup.find_all(
                        class_="tgme_page_extra"
                    )

                    if full_name_tag_talegram:

                        def remove(string):
                            return string.replace(
                                """
                  """,
                                "",
                            )

                        string = full_name_tag_talegram[0].getText()
                        print(
                            f"{' ' * 10}└[{B}•{RS}] {C}User Description {Y}:{RS} {remove(string)}"
                        )

                    for FULL_NAME in user_full_name_tag_talegram:
                        print(
                            f"{' ' * 10}└[{Y}•{RS}] {C}User Profile{RS}/{C}Group{RS}/{C}Page Name {Y}:{RS} {FULL_NAME.string}"
                        )

                    if not Group_member_and_online_talegram:
                        print(
                            f"{' ' * 10}└[{G}•{RS}] {C}Group Members & Online {Y}:{RS} {R}Not Found ❌ {RS}"
                        )
                    else:

                        def remove(string):
                            return string.replace(
                                """
                  """,
                                " ",
                            )

                        string = Group_member_and_online_talegram[0].getText()
                        print(
                            f"{' ' * 10}└[{R}•{RS}] {C}Group Members & Online{RS}/{C}Username{RS}/{C}Subscribers{Y}:{RS} {remove(string)}"
                        )

                elif Telegram_Request.status_code == 404:
                    print(f"\n└── {B}Telegram {R}✖{RS}")
                    print(
                        f"{' ' * 5}└[{R}•{RS}] {C}User Url {Y}:{RS} {R}Not Found ❗️{RS}"
                    )

            else:
                print(f"\n[{B} Telegram{RS} ]")

                print(
                    f"{' ' * 5}└[{R}•{RS}] {C}Connection Lost{Y}:{RS} {R}Oops! Unable To Establish A Connection{RS}"
                )
        except requests.exceptions.Timeout:
            print(f"\n[{B} Telegram{RS} ]")

            print(
                f"{' ' * 5}└[{R}•{RS}] {C}Timeout Error{Y}:{RS} {R}Oops! Timed Out{RS}"
            )
    except socket.gaierror:
        print(f"\n[{B} Telegram{RS} ]")

        print(
            f"{' ' * 5}└[{R}•{RS}] {C}DNS LookUp{Y}:{RS} {R}Oops! The {G}Dns Lookup{R} Failed And The Requested Domain Could Not Be Found.{RS}"
        )

    # [ TINDER ]

    try:
        ip_address = socket.gethostbyname("tinder.com")
        # print('IP address:', ip_address)
        try:
            response = requests.get("https://tinder.com", timeout=5)
            if response.status_code == 200:
                Tinder_Url = f"https://tinder.com/@{usernames}"

                Tinder_Request = requests.get(Tinder_Url)

                if Tinder_Request.status_code == 200:

                    print(f"\n[{B} TINDER{RS} ]")

                    Tinder_Soup = BeautifulSoup(Tinder_Request.text, "html.parser")

                    Tinder_title = Tinder_Soup.find(
                        "meta", property="profile:first_name"
                    )
                    Tinder_Image = Tinder_Soup.find("meta", property="og:image")

                    if Tinder_title:
                        print(f"{' ' * 5}└[{R}•{RS}] {C}User Url {Y}:{RS} {Tinder_Url}")
                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {Tinder_title['content']}"
                        )
                        print(
                            f"{' ' * 5}└[{Y}•{RS}] {C}User Profile Image {Y}:{RS} {Tinder_Image['content']}"
                        )
                    else:
                        print(
                            f"{' ' * 5}└[{R}•{RS}] {C}User Info{Y}:{RS} {R}Sorry, we couldn't find that one ❗️{RS}"
                        )

            else:
                print(f"\n[{B} TINDER{RS} ]")

                print(
                    f"{' ' * 5}└[{R}•{RS}] {C}Connection Lost{Y}:{RS} {R}Oops! Unable To Establish A Connection{RS}"
                )
        except requests.exceptions.Timeout:
            print(f"\n[{B} TINDER{RS} ]")

            print(
                f"{' ' * 5}└[{R}•{RS}] {C}Timeout Error{Y}:{RS} {R}Oops! Timed Out{RS}"
            )
    except socket.gaierror:
        print(f"\n[{B} TINDER{RS} ]")

        print(
            f"{' ' * 5}└[{R}•{RS}] {C}DNS LookUp{Y}:{RS} {R}Oops! The {G}Dns Lookup{R} Failed And The Requested Domain Could Not Be Found.{RS}"
        )

    # [ SOUNDCLOUD ]

    try:
        ip_address = socket.gethostbyname("soundcloud.com")
        # print('IP address:', ip_address)
        try:
            response = requests.get("https://soundcloud.com", timeout=5)
            if response.status_code == 200:
                SOUNDCLOUD_Url = f"https://soundcloud.com/{usernames}"

                SOUNDCLOUD_Request = requests.get(SOUNDCLOUD_Url)

                if SOUNDCLOUD_Request.status_code == 200:
                    print(f"\n[{B} SOUNDCLOUD{RS} ]")

                    SOUNDCLOUD_Soup = BeautifulSoup(
                        SOUNDCLOUD_Request.text, "html.parser"
                    )

                    SOUNDCLOUD_title = SOUNDCLOUD_Soup.find("meta", property="og:title")
                    SOUNDCLOUD_FOLLOWER = SOUNDCLOUD_Soup.find(
                        "meta", property="soundcloud:follower_count"
                    )

                    print(f"{' ' * 5}└[{R}•{RS}] {C}User Url {Y}:{RS} {SOUNDCLOUD_Url}")
                    print(
                        f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {SOUNDCLOUD_title['content']}"
                    )
                    print(
                        f"{' ' * 5}└[{B}•{RS}] {C}User Follower {Y}:{RS} {SOUNDCLOUD_FOLLOWER['content']}"
                    )

                if SOUNDCLOUD_Request.status_code == 404:
                    print(f"\n[{B} SOUNDCLOUD{RS} ]")
                    print(
                        f"{' ' * 5}└[{R}•{RS}] {C}User Info {Y}:{RS} {R}Not Found ❗️{RS}"
                    )

            else:
                print(f"\n[{B} SOUNDCLOUD{RS} ]")

                print(
                    f"{' ' * 5}└[{R}•{RS}] {C}Connection Lost{Y}:{RS} {R}Oops! Unable To Establish A Connection{RS}"
                )
        except requests.exceptions.Timeout:
            print(f"\n[{B} SOUNDCLOUD{RS} ]")

            print(
                f"{' ' * 5}└[{R}•{RS}] {C}Timeout Error{Y}:{RS} {R}Oops! Timed Out{RS}"
            )
    except socket.gaierror:
        print(f"\n[{B} SOUNDCLOUD{RS} ]")

        print(
            f"{' ' * 5}└[{R}•{RS}] {C}DNS LookUp{Y}:{RS} {R}Oops! The {G}Dns Lookup{R} Failed And The Requested Domain Could Not Be Found.{RS}"
        )

    # [ STEAM ]

    try:
        ip_address = socket.gethostbyname("steamcommunity.com")
        # print('IP address:', ip_address)
        try:
            response = requests.get("https://steamcommunity.com", timeout=5)
            if response.status_code == 200:
                STEAM_Url = f"https://steamcommunity.com/id/{usernames}"

                STEAM_Request = requests.get(STEAM_Url)

                if STEAM_Request.status_code == 200:

                    print(f"\n[{B} STEAM{RS} ]")

                    STEAM_Soup = BeautifulSoup(STEAM_Request.text, "html.parser")

                    STEAM_name = STEAM_Soup.find_all(
                        "span", attrs={"class": "actual_persona_name"}
                    )

                    STEAM_specified_profile_could_not_be_found = STEAM_Soup.find_all(
                        "div", id="message"
                    )

                    profile_private_info = STEAM_Soup.find_all(
                        "div", class_="profile_private_info"
                    )

                    STEAM_friend_PlayerLevel = STEAM_Soup.find_all(
                        "span", attrs={"class": "friendPlayerLevelNum"}
                    )

                    NOT_FOUND = STEAM_Soup.find_all("p", class_="sectionText")

                    if not profile_private_info:
                        if not NOT_FOUND:
                            print(
                                f"{' ' * 5}└[{R}•{RS}] {C}User Url {Y}:{RS} {STEAM_Url}"
                            )
                            print(
                                f"{' ' * 5}└[{B}•{RS}] {C}User Player Name {Y}:{RS} {STEAM_name[0].getText()}"
                            )
                            print(
                                f"{' ' * 5}└[{Y}•{RS}] {C}User Player LevelNum {Y}:{RS} {STEAM_friend_PlayerLevel[0].getText()}"
                            )
                        else:
                            print(
                                f"{' ' * 5}└[{R}•{RS}] {C}User Info{Y}:{RS} {R}Sorry, we couldn't find that one ❗️{RS}"
                            )
                    else:

                        def remove(string):
                            return string.replace(
                                """
                															""",
                                "        ",
                            )

                        string = profile_private_info[0].getText()
                        str = remove(string)
                        new_str = str.strip()
                        print(
                            f"{' ' * 5}└[{R}•{RS}] {C}User Private {Y}:{RS} {new_str}"
                        )

            else:
                print(f"\n[{B} STEAM{RS} ]")

                print(
                    f"{' ' * 5}└[{R}•{RS}] {C}Connection Lost{Y}:{RS} {R}Oops! Unable To Establish A Connection{RS}"
                )
        except requests.exceptions.Timeout:
            print(f"\n[{B} STEAM{RS} ]")

            print(
                f"{' ' * 5}└[{R}•{RS}] {C}Timeout Error{Y}:{RS} {R}Oops! Timed Out{RS}"
            )
    except socket.gaierror:
        print(f"\n[{B} STEAM{RS} ]")

        print(
            f"{' ' * 5}└[{R}•{RS}] {C}DNS LookUp{Y}:{RS} {R}Oops! The {G}Dns Lookup{R} Failed And The Requested Domain Could Not Be Found.{RS}"
        )

    # [ LINKTR ]

    try:
        ip_address = socket.gethostbyname("linktr.ee")
        # print('IP address:', ip_address)
        try:
            response = requests.get("https://linktr.ee", timeout=5)
            if response.status_code == 200:
                LINKTR_Url = f"https://linktr.ee/{usernames}"

                LINKTR_Request = requests.get(LINKTR_Url)

                if LINKTR_Request.status_code == 200:

                    print(f"\n[{B} LINKTR{RS} ]")

                    print(f"{' ' * 5}└[{R}•{RS}] {C}User Url {Y}:{RS} {LINKTR_Url}")

                    LINKTR_Soup = BeautifulSoup(LINKTR_Request.text, "html.parser")

                    LINKTR_title2 = LINKTR_Soup.find(
                        "span",
                        attrs={
                            "class": "UserDetailsCard_title__trfvf UserDetailsCard_oneLineTruncation__uhOF5"
                        },
                    )

                    NOT_verified = LINKTR_Soup.find("div", class_="sc-bdfBwQ dnZXm")

                    profile_name = LINKTR_Soup.find(
                        "div", class_="sc-bdfBwQ Header__Grid-sc-i98650-0 llgrqs jvyDlw"
                    )

                    profile_description = LINKTR_Soup.find(
                        "div", class_="sc-bdfBwQ hTuoxC"
                    )

                    profile_image = LINKTR_Soup.find("meta", property="og:image")

                    if not NOT_verified:
                        if not profile_name:
                            print(
                                f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {R}Not Found ❗️{RS} "
                            )
                        else:
                            print(
                                f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {profile_name.string}"
                            )

                        if not profile_description:
                            print(
                                f"{' ' * 5}└[{Y}•{RS}] {C}User Description {Y}:{RS} {R}Not Found ❗️{RS} "
                            )
                        else:
                            print(
                                f"{' ' * 5}└[{Y}•{RS}] {C}User Description {Y}:{RS} {profile_description.string}"
                            )

                            UserMention_Bio = profile_description.string

                            Mention_Bio = re.findall(
                                r"@[A-Za-z0-9.-]+", UserMention_Bio
                            )

                            print(
                                f"{' ' * 5}└[{G}•{RS}] {C}List Of People Mention On USER Bio{Y}:{RS}"
                            )

                            if not Mention_Bio:
                                print(
                                    f"{' ' * 20}└[{R}•{RS}] {Y}Mention Pople {C}On Bio {Y}:{RS} {R}Not Found ❗️{RS} \n"
                                )
                            else:
                                count = 0
                                for Mention_Bios in Mention_Bio:
                                    count += 1
                                    print(
                                        f"{' ' * 20}└[{R}{count}{RS}] {G}►{RS} {Mention_Bios}"
                                    )

                            UserEmail = profile_description.string

                            emails = re.findall(r"[\w\.-]+@[\w\.-]+", UserEmail)

                            print(
                                f"{' ' * 5}└[{R}•{RS}] {C}List Of Email Write On USER Bio{Y}:{RS}"
                            )

                            if not emails:
                                print(
                                    f"{' ' * 20}└[{R}•{RS}] {C}Find {Y}Email {C}On Bio {Y}:{RS} {R}Not Found ❗️{RS} \n"
                                )
                            else:
                                count = 0
                            for email in emails:
                                count += 1
                                print(f"{' ' * 20}└[{R}{count}{RS}] {G}►{RS} {email}")

                            print(
                                f"{' ' * 5}└[{B}•{RS}] {C}List Of PhoneNumber Or Any Digit On USER Bio{Y}:{RS}"
                            )

                            PhoneNumberbio = profile_description.string

                            PhoneNumbers = re.findall(r"\d+", PhoneNumberbio)

                            if not PhoneNumbers:
                                print(
                                    f"{' ' * 20}└[{R}•{RS}] {C}Find {Y}PhoneNumber {C}On Bio {Y}:{RS} {R}Not Found ❗️{RS} "
                                )
                            else:
                                count = 0
                            for PhoneNumber in PhoneNumbers:
                                count += 1
                                print(
                                    f"{' ' * 20}└[{R}{count}{RS}] {G}►{RS} {PhoneNumber}"
                                )

                        if not profile_image:
                            print(
                                f"\n{' ' * 5}└[{Y}•{RS}] {C}User Profile Image {Y}:{RS} {R}Not Found ❗️{RS} "
                            )
                        else:
                            print(
                                f"\n{' ' * 5}└[{G}•{RS}] {C}User Profile Image {Y}:{RS} {profile_image['content']}"
                            )
                    else:
                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}User Profile Image {Y}:{RS} {NOT_verified.string}"
                        )

                if LINKTR_Request.status_code == 404:
                    print(f"\n[{B} LINKTR{RS} ]")
                    print(
                        f"{' ' * 5}└[{R}•{RS}] {C}User Info{Y}:{RS} {R}Sorry, we couldn't find that one ❗️{RS}"
                    )

            else:
                print(f"\n[{B} LINKTR{RS} ]")

                print(
                    f"{' ' * 5}└[{R}•{RS}] {C}Connection Lost{Y}:{RS} {R}Oops! Unable To Establish A Connection{RS}"
                )
        except requests.exceptions.Timeout:
            print(f"\n[{B} LINKTR{RS} ]")

            print(
                f"{' ' * 5}└[{R}•{RS}] {C}Timeout Error{Y}:{RS} {R}Oops! Timed Out{RS}"
            )
    except socket.gaierror:
        print(f"\n[{B} LINKTR{RS} ]")

        print(
            f"{' ' * 5}└[{R}•{RS}] {C}DNS LookUp{Y}:{RS} {R}Oops! The {G}Dns Lookup{R} Failed And The Requested Domain Could Not Be Found.{RS}"
        )

    # [ XBOX GAMER ]

    try:
        ip_address = socket.gethostbyname("xbox.com")
        # print('IP address:', ip_address)
        try:
            response = requests.get("https://www.xbox.com", timeout=5)
            if response.status_code == 200:
                headers = {
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.33",
                }

                XBOXGAMERTAG_Url = f"https://www.xboxgamertag.com/search/{usernames}"

                XBOXGAMERTAG_Request = requests.get(XBOXGAMERTAG_Url, headers=headers)

                if XBOXGAMERTAG_Request.status_code == 200:
                    print(f"\n[{B} XBOX GAMER{RS} ]")

                    print(
                        f"{' ' * 5}└[{R}•{RS}] {C}User Url {Y}:{RS} {XBOXGAMERTAG_Url}"
                    )

                    LINKTR_Soup = BeautifulSoup(
                        XBOXGAMERTAG_Request.text, "html.parser"
                    )

                    Gamerscore = LINKTR_Soup.find(
                        "div", class_="col-auto profile-detail-item"
                    )

                    name_XBOX = LINKTR_Soup.find("title")

                    def remove(string):
                        return string.replace(
                            """
                                                """,
                            " ",
                        )

                    string = Gamerscore.getText()
                    str = remove(string)
                    new_str = str.strip()
                    print(
                        f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {name_XBOX.getText()}"
                    )
                    print(
                        f"{' ' * 5}└[{Y}•{RS}] {C}User Gamer Score {Y}:{RS} {new_str}"
                    )

                if XBOXGAMERTAG_Request.status_code == 404:
                    print(f"\n[{B} XBOX GAMER{RS} ]")
                    print(
                        f"{' ' * 5}└[{R}•{RS}] {C}User Info{Y}:{RS} {R}Sorry, we couldn't find that one ❗️{RS}"
                    )

            else:
                print(f"\n[{B} XBOX GAMER{RS} ]")

                print(
                    f"{' ' * 5}└[{R}•{RS}] {C}Connection Lost{Y}:{RS} {R}Oops! Unable To Establish A Connection{RS}"
                )
        except requests.exceptions.Timeout:
            print(f"\n[{B} XBOX GAMER{RS} ]")

            print(
                f"{' ' * 5}└[{R}•{RS}] {C}Timeout Error{Y}:{RS} {R}Oops! Timed Out{RS}"
            )
    except socket.gaierror:
        print(f"\n[{B} XBOX GAMER{RS} ]")

        print(
            f"{' ' * 5}└[{R}•{RS}] {C}DNS LookUp{Y}:{RS} {R}Oops! The {G}Dns Lookup{R} Failed And The Requested Domain Could Not Be Found.{RS}"
        )

    # [ TWITCH ]

    try:
        ip_address = socket.gethostbyname("twitch.tv")
        # print('IP address:', ip_address)
        try:
            response = requests.get("https://www.twitch.tv", timeout=5)
            if response.status_code == 200:
                headers = {
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.33",
                }

                TWITCH_Url = f"https://twitchtracker.com/{usernames}"

                TWITCH_Request = requests.get(TWITCH_Url, headers=headers)

                if TWITCH_Request.status_code == 200:

                    print(f"\n[{B} TWITCH{RS} ]")

                    print(
                        f"{' ' * 5}└[{R}•{RS}] {C}User Url {Y}:{RS} {'https://www.twitch.tv/' + usernames}"
                    )

                    TWITCH_Soup = BeautifulSoup(TWITCH_Request.text, "html.parser")

                    name_TWITCH = TWITCH_Soup.find("div", id="app-title")

                    BIO_TWITCH = TWITCH_Soup.find(
                        "div", style="word-wrap:break-word;font-size:12px;"
                    )

                    PLAYER_RANK_TWITCH = TWITCH_Soup.find("span", class_="to-number")

                    PLAYER_Followers_TWITCHs = TWITCH_Soup.find(
                        "div", style="display: inline-block;"
                    )

                    PLAYER_Avgviewer_TWITCHs = TWITCH_Soup.find(
                        "div", style="display: inline-block;margin-left: 20px;"
                    )

                    name_TWITCH_SPACE_REMOVE = name_TWITCH.getText()
                    name_TWITCH_SPACE_REMOVE_RESULT = name_TWITCH_SPACE_REMOVE.strip()

                    if not BIO_TWITCH:
                        print(
                            f"{' ' * 5}└[{R}•{RS}] {C}User Player Name {Y}:{RS} {R}Not Found ❗️{RS} "
                        )
                    else:
                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}User Player Name {Y}:{RS} {name_TWITCH_SPACE_REMOVE_RESULT}"
                        )

                    if not BIO_TWITCH:
                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}User Description {Y}:{RS} {R}Not Found ❗️{RS} "
                        )
                    else:
                        print(
                            f"{' ' * 5}└[{Y}•{RS}] {C}User Description {Y}:{RS} {BIO_TWITCH.get_text()}"
                        )

                        UserMention_Bio = BIO_TWITCH.get_text()

                        Mention_Bio = re.findall(r"@[A-Za-z0-9.-]+", UserMention_Bio)

                        print(
                            f"{' ' * 5}└[{G}•{RS}] {C}List Of People Mention On USER Bio{Y}:{RS}"
                        )

                        if not Mention_Bio:
                            print(
                                f"{' ' * 20}└[{R}•{RS}] {Y}Mention Pople {C}On Bio {Y}:{RS} {R}Not Found ❗️{RS} \n"
                            )
                        else:
                            count = 0
                            for Mention_Bios in Mention_Bio:
                                count += 1
                                print(
                                    f"{' ' * 20}└[{R}{count}{RS}] {G}►{RS} {Mention_Bios}"
                                )

                        UserEmail = BIO_TWITCH.get_text()

                        emails = re.findall(r"[\w\.-]+@[\w\.-]+", UserEmail)

                        print(
                            f"{' ' * 5}└[{R}•{RS}] {C}List Of Email Write On USER Bio{Y}:{RS}"
                        )

                        if not emails:
                            print(
                                f"{' ' * 20}└[{R}•{RS}] {C}Find {Y}Email {C}On Bio {Y}:{RS} {R}Not Found ❗️{RS} \n"
                            )
                        else:
                            count = 0
                        for email in emails:
                            count += 1
                            print(f"{' ' * 20}└[{R}{count}{RS}] {G}►{RS} {email}")

                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}List Of PhoneNumber Or Any Digit On USER Bio{Y}:{RS}"
                        )

                        PhoneNumberbio = BIO_TWITCH.get_text()

                        PhoneNumbers = re.findall(r"\d+", PhoneNumberbio)

                        if not PhoneNumbers:
                            print(
                                f"{' ' * 20}└[{R}•{RS}] {C}Find {Y}PhoneNumber {C}On Bio {Y}:{RS} {R}Not Found ❗️{RS} "
                            )
                        else:
                            count = 0
                        for PhoneNumber in PhoneNumbers:
                            count += 1
                            print(f"{' ' * 20}└[{R}{count}{RS}] {G}►{RS} {PhoneNumber}")

                    if not PLAYER_Followers_TWITCHs:
                        print(
                            f"\n{' ' * 5}└[{Y}•{RS}] {C}User Player Followers {Y}:{RS} {R}Not Found ❗️{RS} "
                        )
                    else:
                        PLAYER_FOLLOWERSS_TWITCHs = TWITCH_Soup.find(
                            "div", style="display: inline-block;"
                        ).find("span", class_="to-number")
                        print(
                            f"\n{' ' * 5}└[{G}•{RS}] {C}User Player Followers {Y}:{RS} {PLAYER_FOLLOWERSS_TWITCHs.string}"
                        )

                    if not PLAYER_RANK_TWITCH:
                        print(
                            f"{' ' * 5}└[{Y}•{RS}] {C}User Player RANK {Y}:{RS} {R}Not Found ❗️{RS} "
                        )
                    else:
                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}User Player RANK {Y}:{RS} {PLAYER_RANK_TWITCH.getText()}"
                        )

                if TWITCH_Request.status_code == 404:
                    print(f"\n[{B} TWITCH{RS} ]")
                    print(
                        f"{' ' * 5}└[{R}•{RS}] {C}User Info{Y}:{RS} {R}Sorry, we couldn't find that one ❗️{RS}"
                    )

            else:
                print(f"\n[{B} TWITCH{RS} ]")

                print(
                    f"{' ' * 5}└[{R}•{RS}] {C}Connection Lost{Y}:{RS} {R}Oops! Unable To Establish A Connection{RS}"
                )
        except requests.exceptions.Timeout:
            print(f"\n[{B} TWITCH{RS} ]")

            print(
                f"{' ' * 5}└[{R}•{RS}] {C}Timeout Error{Y}:{RS} {R}Oops! Timed Out{RS}"
            )
    except socket.gaierror:
        print(f"\n[{B} TWITCH{RS} ]")

        print(
            f"{' ' * 5}└[{R}•{RS}] {C}DNS LookUp{Y}:{RS} {R}Oops! The {G}Dns Lookup{R} Failed And The Requested Domain Could Not Be Found.{RS}"
        )

    # [ PROFILES WORDPRESS ]

    try:
        ip_address = socket.gethostbyname("profiles.wordpress.org")
        # print('IP address:', ip_address)
        try:
            response = requests.get("https://profiles.wordpress.org", timeout=5)
            if response.status_code == 200:
                PROFILESWORDPRESS_Url = f"https://profiles.wordpress.org/{usernames}/"

                PROFILESWORDPRESS_Request = requests.get(PROFILESWORDPRESS_Url)

                if PROFILESWORDPRESS_Request.status_code == 200:

                    print(f"\n[{B} PROFILES WORDPRESS{RS} ]")

                    print(
                        f"{' ' * 5}└[{R}•{RS}] {C}User Url {Y}:{RS} {PROFILESWORDPRESS_Url}"
                    )

                    PROFILESWORDPRESS_Soup = BeautifulSoup(
                        PROFILESWORDPRESS_Request.text, "html.parser"
                    )

                    NAME_title = PROFILESWORDPRESS_Soup.find(
                        "h2", attrs={"class": "fn"}
                    )

                    username_slack_title = PROFILESWORDPRESS_Soup.find(
                        "p", attrs={"id": "slack-username"}
                    )

                    Member_Since_title = PROFILESWORDPRESS_Soup.find(
                        "li", attrs={"id": "user-member-since"}
                    )

                    location_name = PROFILESWORDPRESS_Soup.find(
                        "li", attrs={"id": "user-location"}
                    )

                    USER_GITHUB_USERNAME = PROFILESWORDPRESS_Soup.find(
                        "li", attrs={"id": "user-github"}
                    )

                    user_job = PROFILESWORDPRESS_Soup.find(
                        "li", attrs={"id": "user-job"}
                    )

                    user_company = PROFILESWORDPRESS_Soup.find(
                        "li", attrs={"id": "user-company"}
                    )

                    Interests = PROFILESWORDPRESS_Soup.find(
                        "div", attrs={"class": "item-meta-interests"}
                    )

                    BIO = PROFILESWORDPRESS_Soup.find(
                        "div", attrs={"class": "item-meta-about"}
                    )

                    if not NAME_title:
                        print(
                            f"{' ' * 5}└[{Y}•{RS}] {C}User Profile Name {Y}:{RS} {R}Not Found ❗️{RS} "
                        )
                    else:
                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {NAME_title.string}"
                        )

                    if not username_slack_title:
                        print(
                            f"{' ' * 5}└[{Y}•{RS}] {C}User Slack Username {Y}:{RS} {R}Not Found ❗️{RS} "
                        )
                    else:
                        name_PROFILESWORDPRESS_SPACE_REMOVE = (
                            username_slack_title.get_text()
                        )
                        name_PROFILESWORDPRESS_SPACE_REMOVE_RESULT = (
                            name_PROFILESWORDPRESS_SPACE_REMOVE.strip()
                        )
                        print(
                            f"{' ' * 5}└[{Y}•{RS}] {C}User Slack Username {Y}:{RS} {name_PROFILESWORDPRESS_SPACE_REMOVE_RESULT}"
                        )

                    if not BIO:
                        print(
                            f"{' ' * 5}└[{G}•{RS}] {C}User Bio {Y}:{RS} {R}Not Found ❗️{RS} "
                        )
                    else:
                        BIOS = PROFILESWORDPRESS_Soup.find(
                            "div", attrs={"class": "item-meta-about"}
                        ).find("p")
                        print(
                            f"{' ' * 5}└[{G}•{RS}] {C}User Bio {Y}:{RS} {BIOS.getText()}"
                        )

                        UserMention_Bio = BIOS.getText()

                        Mention_Bio = re.findall(r"@[A-Za-z0-9.-]+", UserMention_Bio)

                        print(
                            f"{' ' * 5}└[{R}•{RS}] {C}List Of People Mention On USER Bio{Y}:{RS}"
                        )

                        if not Mention_Bio:
                            print(
                                f"{' ' * 20}└[{R}•{RS}] {Y}Mention Pople {C}On Bio {Y}:{RS} {R}Not Found ❗️{RS} \n"
                            )
                        else:
                            count = 0
                            for Mention_Bios in Mention_Bio:
                                count += 1
                                print(
                                    f"{' ' * 20}└[{R}{count}{RS}] {G}►{RS} {Mention_Bios}"
                                )

                        UserEmail = BIOS.getText()

                        emails = re.findall(r"[\w\.-]+@[\w\.-]+", UserEmail)

                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}List Of Email Write On USER Bio{Y}:{RS}"
                        )

                        if not emails:
                            print(
                                f"{' ' * 20}└[{R}•{RS}] {C}Find {Y}Email {C}On Bio {Y}:{RS} {R}Not Found ❗️{RS} \n"
                            )
                        else:
                            count = 0
                        for email in emails:
                            count += 1
                            print(f"{' ' * 20}└[{R}{count}{RS}] {G}►{RS} {email}")

                        print(
                            f"{' ' * 5}└[{Y}•{RS}] {C}List Of PhoneNumber Or Any Digit On USER Bio{Y}:{RS}"
                        )

                        PhoneNumberbio = BIOS.getText()

                        PhoneNumbers = re.findall(r"\d+", PhoneNumberbio)

                        if not PhoneNumbers:
                            print(
                                f"{' ' * 20}└[{R}•{RS}] {C}Find {Y}PhoneNumber {C}On Bio {Y}:{RS} {R}Not Found ❗️{RS} "
                            )
                        else:
                            count = 0
                        for PhoneNumber in PhoneNumbers:
                            count += 1
                            print(f"{' ' * 20}└[{R}{count}{RS}] {G}►{RS} {PhoneNumber}")

                    if not Member_Since_title:
                        print(
                            f"\n{' ' * 5}└[{R}•{RS}] {C}User Member Since {Y}:{RS} {R}Not Found ❗️{RS} "
                        )
                    else:
                        Member_Since_titleS = PROFILESWORDPRESS_Soup.find(
                            "li", attrs={"id": "user-member-since"}
                        ).find("strong")
                        print(
                            f"\n{' ' * 5}└[{R}•{RS}] {C}User Member Since {Y}:{RS} {Member_Since_titleS.get_text()}"
                        )

                    if not location_name:
                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}User Location {Y}:{RS} {R}Not Found ❗️{RS} "
                        )
                    else:
                        location_names = PROFILESWORDPRESS_Soup.find(
                            "li", attrs={"id": "user-location"}
                        ).find("strong")
                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}User Location {Y}:{RS} {location_names.get_text()}"
                        )

                    if not USER_GITHUB_USERNAME:
                        print(
                            f"{' ' * 5}└[{Y}•{RS}] {C}User GitHub {Y}:{RS} {R}Not Found ❗️{RS} "
                        )
                    else:
                        USER_GITHUB_USERNAMES = PROFILESWORDPRESS_Soup.find(
                            "li", attrs={"id": "user-github"}
                        ).find("strong")
                        print(
                            f"{' ' * 5}└[{Y}•{RS}] {C}User GitHub {Y}:{RS} {USER_GITHUB_USERNAMES.get_text()}"
                        )

                    if not user_job:
                        print(
                            f"{' ' * 5}└[{G}•{RS}] {C}User Job Title {Y}:{RS} {R}Not Found ❗️{RS} "
                        )
                    else:
                        USER_JOB = PROFILESWORDPRESS_Soup.find(
                            "li", attrs={"id": "user-job"}
                        ).find("strong")
                        print(
                            f"{' ' * 5}└[{G}•{RS}] {C}User Job Title {Y}:{RS} {USER_JOB.get_text()}"
                        )

                    if not user_company:
                        print(
                            f"{' ' * 5}└[{R}•{RS}] {C}User Employer {Y}:{RS} {R}Not Found ❗️{RS} "
                        )
                    else:
                        USER_COMPANY = PROFILESWORDPRESS_Soup.find(
                            "li", attrs={"id": "user-company"}
                        ).find("strong")
                        print(
                            f"{' ' * 5}└[{R}•{RS}] {C}User Employer {Y}:{RS} {USER_COMPANY.get_text()}"
                        )

                    if not Interests:
                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}User Interests {Y}:{RS} {R}Not Found ❗️{RS} "
                        )
                    else:
                        InterestsS = PROFILESWORDPRESS_Soup.find(
                            "div", attrs={"class": "item-meta-interests"}
                        ).find("p")
                        name_Interests_SPACE_REMOVE = InterestsS.getText()
                        name_Interests_SPACE_REMOVE_RESULT = (
                            name_Interests_SPACE_REMOVE.strip()
                        )
                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}User Interests {Y}:{RS} {name_Interests_SPACE_REMOVE_RESULT}"
                        )

                if PROFILESWORDPRESS_Request.status_code == 404:
                    print(f"\n[{B} PROFILES WORDPRESS{RS} ]")
                    print(
                        f"{' ' * 5}└[{R}•{RS}] {C}User Info{Y}:{RS} {R}Sorry, we couldn't find that one ❗️{RS}"
                    )

            else:
                print(f"\n[{B} PROFILES WORDPRESS{RS} ]")

                print(
                    f"{' ' * 5}└[{R}•{RS}] {C}Connection Lost{Y}:{RS} {R}Oops! Unable To Establish A Connection{RS}"
                )
        except requests.exceptions.Timeout:
            print(f"\n[{B} PROFILES WORDPRESS{RS} ]")

            print(
                f"{' ' * 5}└[{R}•{RS}] {C}Timeout Error{Y}:{RS} {R}Oops! Timed Out{RS}"
            )
    except socket.gaierror:
        print(f"\n[{B} PROFILES WORDPRESS{RS} ]")

        print(
            f"{' ' * 5}└[{R}•{RS}] {C}DNS LookUp{Y}:{RS} {R}Oops! The {G}Dns Lookup{R} Failed And The Requested Domain Could Not Be Found.{RS}"
        )

    # [ THERMI ]

    try:
        ip_address = socket.gethostbyname(f"thermi.com")
        # print('IP address:', ip_address)
        try:
            response = requests.get(f"https://thermi.com", timeout=5)
            if response.status_code == 200:
                THERMI_Url = f"https://thermi.com/providers_profiles/{usernames}/"

                THERMI_Request = requests.get(THERMI_Url)

                if THERMI_Request.status_code == 200:

                    print(f"\n[{B} THERMI{RS} ]")

                    print(f"{' ' * 5}└[{R}•{RS}] {C}User Url {Y}:{RS} {THERMI_Url}")

                    THERMI_Soup = BeautifulSoup(THERMI_Request.text, "html.parser")

                    THERMI_NAME = THERMI_Soup.find(
                        "div", attrs={"class": "provider_name"}
                    )

                    specialty_NAME = THERMI_Soup.find(
                        "div", attrs={"class": "provider_specialty"}
                    )

                    Address_NAME = THERMI_Soup.find(
                        "div", attrs={"class": "content_container"}
                    )

                    PHONE_NUMBER = THERMI_Soup.find(
                        "a", attrs={"class": "provider_phone"}
                    )

                    if not THERMI_NAME:
                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {R}Not Found ❗️{RS} "
                        )
                    else:
                        name_THERMI_NAME_SPACE_REMOVE = THERMI_NAME.get_text()
                        name_THERMI_SPACE_REMOVE_RESULT = (
                            name_THERMI_NAME_SPACE_REMOVE.strip()
                        )
                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {name_THERMI_SPACE_REMOVE_RESULT}"
                        )

                    if not specialty_NAME:
                        print(
                            f"{' ' * 5}└[{Y}•{RS}] {C}User Specialty {Y}:{RS} {R}Not Found ❗️{RS} "
                        )
                    else:
                        name_THERMI_NAME_SPACE_REMOVE = specialty_NAME.get_text()
                        name_THERMI_SPACE_REMOVE_RESULT = (
                            name_THERMI_NAME_SPACE_REMOVE.strip()
                        )
                        print(
                            f"{' ' * 5}└[{Y}•{RS}] {C}User Specialty {Y}:{RS} {name_THERMI_SPACE_REMOVE_RESULT}"
                        )

                    if not Address_NAME:
                        print(
                            f"{' ' * 5}└[{G}•{RS}] {C}User Address {Y}:{RS} {R}Not Found ❗️{RS} "
                        )
                    else:
                        Address_NAMES = THERMI_Soup.find(
                            "div", attrs={"class": "content_container"}
                        ).find("address")
                        name_THERMI_NAME_SPACE_REMOVE = Address_NAMES.get_text()
                        name_THERMI_SPACE_REMOVE_RESULT = (
                            name_THERMI_NAME_SPACE_REMOVE.strip()
                        )
                        print(
                            f"{' ' * 5}└[{G}•{RS}] {C}User Address {Y}:{RS} {name_THERMI_SPACE_REMOVE_RESULT}"
                        )

                    if not PHONE_NUMBER:
                        print(
                            f"{' ' * 5}└[{R}•{RS}] {C}User Address {Y}:{RS} {R}Not Found ❗️{RS} "
                        )
                    else:
                        name_THERMI_NAME_SPACE_REMOVE = PHONE_NUMBER.get_text()
                        name_THERMI_SPACE_REMOVE_RESULT = (
                            name_THERMI_NAME_SPACE_REMOVE.strip()
                        )
                        print(
                            f"{' ' * 5}└[{R}•{RS}] {C}User PhoneNumber{RS}/{C}Telephone {Y}:{RS} {name_THERMI_SPACE_REMOVE_RESULT}"
                        )

                    print(
                        f"{' ' * 5}[{G} NOTE {RS}] [ {C}YOU SEE THE {R}INFO{C} ON{RS},{C} THIS A {Y}DOCTORE{C} INFO{G}{RS} ] \n"
                    )

                if THERMI_Request.status_code == 404:
                    print(f"\n[{B} THERMI{RS} ]")
                    print(
                        f"{' ' * 5}└[{R}•{RS}] {C}User Info{Y}:{RS} {R}Sorry, we couldn't find that one ❗️{RS}"
                    )

            else:
                print(f"\n[{B} THERMI{RS} ]")

                print(
                    f"{' ' * 5}└[{R}•{RS}] {C}Connection Lost{Y}:{RS} {R}Oops! Unable To Establish A Connection{RS}"
                )
        except requests.exceptions.Timeout:
            print(f"\n[{B} THERMI{RS} ]")

            print(
                f"{' ' * 5}└[{R}•{RS}] {C}Timeout Error{Y}:{RS} {R}Oops! Timed Out{RS}"
            )
    except socket.gaierror:
        print(f"\n[{B} THERMI{RS} ]")

        print(
            f"{' ' * 5}└[{R}•{RS}] {C}DNS LookUp{Y}:{RS} {R}Oops! The {G}Dns Lookup{R} Failed And The Requested Domain Could Not Be Found.{RS}"
        )

    # [ FREELANCER ]

    try:
        ip_address = socket.gethostbyname("freelancer.com")
        # print('IP address:', ip_address)
        try:
            response = requests.get("https://www.freelancer.com", timeout=5)
            if response.status_code == 200:
                headers = {
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.33",
                }

                FREELANCER_Url = f"https://www.freelancer.com/u/{usernames}"

                FREELANCER_Request = requests.get(FREELANCER_Url, headers=headers)

                if FREELANCER_Request.status_code == 200:

                    print(f"\n[{B} FREELANCER{RS} ]")

                    print(f"{' ' * 5}└[{R}•{RS}] {C}User Url {Y}:{RS} {FREELANCER_Url}")

                    FREELANCER_Soup = BeautifulSoup(
                        FREELANCER_Request.text, "html.parser"
                    )

                    FREELANCER_NAME = FREELANCER_Soup.find(
                        "fl-col", class_="SummaryHeader"
                    )

                    FREELANCER_TAGLINE = FREELANCER_Soup.find(
                        "fl-heading", class_="Tagline ng-star-inserted"
                    )

                    FREELANCER_STAR = FREELANCER_Soup.find(
                        "fl-bit", class_="ValueBlock ng-star-inserted"
                    )

                    FREELANCER_REVIEW = FREELANCER_Soup.find(
                        "fl-bit", class_="ReviewCount ng-star-inserted"
                    )

                    FREELANCER_PER_HOURS = FREELANCER_Soup.find(
                        "fl-bit", class_="Row ng-star-inserted"
                    )

                    FREELANCER_ADDRESS = FREELANCER_Soup.find(
                        "fl-col", class_="SupplementaryInfo"
                    )

                    FREELANCER_JOBS_COMPLETED = FREELANCER_Soup.find(
                        "fl-text", class_="ReputationItemAmount"
                    )

                    if not FREELANCER_NAME:
                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {R}Not Found ❗️{RS} "
                        )
                    else:
                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {FREELANCER_NAME.find('h3').get_text()}"
                        )

                    if not FREELANCER_TAGLINE:
                        print(
                            f"{' ' * 5}└[{Y}•{RS}] {C}User TagLine {Y}:{RS} {R}Not Found ❗️{RS} "
                        )
                    else:
                        print(
                            f"{' ' * 5}└[{Y}•{RS}] {C}User TagLine {Y}:{RS} {FREELANCER_TAGLINE.find('h2').get_text()}"
                        )

                    if not FREELANCER_STAR:
                        print(
                            f"{' ' * 5}└[{G}•{RS}] {C}User Average Rating {Y}:{RS} {R}Not Found ❗️{RS} "
                        )
                    else:
                        print(
                            f"{' ' * 5}└[{G}•{RS}] {C}User Average Rating {Y}:{RS} {FREELANCER_STAR.string}"
                        )

                    if not FREELANCER_REVIEW:
                        print(
                            f"{' ' * 5}└[{R}•{RS}] {C}User Review {Y}:{RS} {R}Not Found ❗️{RS} "
                        )
                    else:
                        print(
                            f"{' ' * 5}└[{R}•{RS}] {C}User Review {Y}:{RS} {FREELANCER_REVIEW.get_text()}"
                        )

                    if not FREELANCER_PER_HOURS:
                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}User Charge {G}$USD{C} Hour{Y}:{RS} {R}Not Found ❗️{RS} "
                        )
                    else:
                        FREELANCER_PER_HOURS_REMOVE = FREELANCER_PER_HOURS.getText()
                        FREELANCER_PER_HOURS_REMOVE_RESULT = (
                            FREELANCER_PER_HOURS_REMOVE.strip()
                        )
                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}User Charge {G}$USD{C} Hour{Y}:{RS} {FREELANCER_PER_HOURS_REMOVE_RESULT}"
                        )

                    if not FREELANCER_ADDRESS:
                        print(
                            f"{' ' * 5}└[{Y}•{RS}] {C}User Address {Y}:{RS} {R}Not Found ❗️{RS} "
                        )
                    else:
                        print(
                            f"{' ' * 5}└[{Y}•{RS}] {C}User Address {Y}:{RS} {FREELANCER_ADDRESS.get_text()}"
                        )

                    if not FREELANCER_ADDRESS:
                        print(
                            f"{' ' * 5}└[{G}•{RS}] {C}User Jobs Completed {Y}:{RS} {R}Not Found ❗️{RS} "
                        )
                    else:
                        print(
                            f"{' ' * 5}└[{G}•{RS}] {C}User Jobs Completed {Y}:{RS} {FREELANCER_JOBS_COMPLETED.get_text()}"
                        )

                    url = f"https://www.freelancer.com/api/users/0.1/users?limit=1&usernames[]={usernames}&avatar=true&online_offline_details=true&status=true&support_status_details=true&limited_account=true&webapp=1&compact=true&new_errors=true&new_pools=true"

                    freelancer_Verifications_Request = requests.request("GET", url)

                    freelancer_Verifications_Data_Json = json.loads(
                        freelancer_Verifications_Request.content
                    )

                    freelancer_Verifications_ID = list(
                        freelancer_Verifications_Data_Json["result"]["users"].keys()
                    )[0]

                    print(
                        f"\n{' ' * 5}[{G} NOTE {RS}] [ {B}Freelancer {Y}Verified{C} Checker You Can Find {R}USER{Y} Facebook{RS}, {Y}Linkedin{C} IF YOUR {R}USER{Y} LINK {C}THIS {Y}ACCOUNT {C}WITH HIS {B}Freelancer Account{RS} ]\n"
                    )

                    if (
                        freelancer_Verifications_Data_Json["result"]["users"][
                            freelancer_Verifications_ID
                        ]["status"]["payment_verified"]
                        == True
                    ):
                        print(
                            f"{' ' * 5}└[{R}•{RS}] {C}User Payment Verified {Y}:{RS} {G} True ✔️️{RS} "
                        )
                    else:
                        print(
                            f"{' ' * 5}└[{R}•{RS}] {C}User Payment Verified {Y}:{RS} {R} False {R}❌️️{RS} "
                        )

                    if (
                        freelancer_Verifications_Data_Json["result"]["users"][
                            freelancer_Verifications_ID
                        ]["status"]["email_verified"]
                        == True
                    ):
                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}User Email Verified {Y}:{RS} {G} True ✔️️{RS} "
                        )
                    else:
                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}User Email Verified {Y}:{RS} {R} False {R}❌️️{RS} "
                        )

                    if (
                        freelancer_Verifications_Data_Json["result"]["users"][
                            freelancer_Verifications_ID
                        ]["status"]["deposit_made"]
                        == True
                    ):
                        print(
                            f"{' ' * 5}└[{Y}•{RS}] {C}User Deposit Made {Y}:{RS} {G} True ✔️️{RS} "
                        )
                    else:
                        print(
                            f"{' ' * 5}└[{Y}•{RS}] {C}User Deposit Made {Y}:{RS} {R} False {R}❌️️{RS} "
                        )

                    if (
                        freelancer_Verifications_Data_Json["result"]["users"][
                            freelancer_Verifications_ID
                        ]["status"]["profile_complete"]
                        == True
                    ):
                        print(
                            f"{' ' * 5}└[{G}•{RS}] {C}User Profile Complete {Y}:{RS} {G} True ✔️️{RS} "
                        )
                    else:
                        print(
                            f"{' ' * 5}└[{G}•{RS}] {C}User Profile Complete {Y}:{RS} {R} False {R}❌️️{RS} "
                        )

                    if (
                        freelancer_Verifications_Data_Json["result"]["users"][
                            freelancer_Verifications_ID
                        ]["status"]["phone_verified"]
                        == True
                    ):
                        print(
                            f"{' ' * 5}└[{R}•{RS}] {C}User Phone Verified {Y}:{RS} {G} True ✔️️{RS} "
                        )
                    else:
                        print(
                            f"{' ' * 5}└[{R}•{RS}] {C}User Phone Verified {Y}:{RS} {R} False {R}❌️️{RS} "
                        )

                    if (
                        freelancer_Verifications_Data_Json["result"]["users"][
                            freelancer_Verifications_ID
                        ]["status"]["identity_verified"]
                        == True
                    ):
                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}User Identity Verified {Y}:{RS} {G} True ✔️️{RS} "
                        )
                    else:
                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}User Identity Verified {Y}:{RS} {R} False {R}❌️️{RS} "
                        )

                    if (
                        freelancer_Verifications_Data_Json["result"]["users"][
                            freelancer_Verifications_ID
                        ]["status"]["facebook_connected"]
                        == True
                    ):
                        print(
                            f"{' ' * 5}└[{Y}•{RS}] {C}User Facebook Connected {Y}:{RS} {G} True ✔️️{RS} "
                        )
                    else:
                        print(
                            f"{' ' * 5}└[{Y}•{RS}] {C}User Facebook Connected {Y}:{RS} {R} False {R}❌️️{RS} "
                        )

                    if (
                        freelancer_Verifications_Data_Json["result"]["users"][
                            freelancer_Verifications_ID
                        ]["status"]["freelancer_verified_user"]
                        == True
                    ):
                        print(
                            f"{' ' * 5}└[{G}•{RS}] {C}User Freelancer Verified_user {Y}:{RS} {G} True ✔️️{RS} "
                        )
                    else:
                        print(
                            f"{' ' * 5}└[{G}•{RS}] {C}User Freelancer Verified_user {Y}:{RS} {R} False {R}❌️️{RS} "
                        )

                    if (
                        freelancer_Verifications_Data_Json["result"]["users"][
                            freelancer_Verifications_ID
                        ]["status"]["linkedin_connected"]
                        == True
                    ):
                        print(
                            f"{' ' * 5}└[{R}•{RS}] {C}User Linkedin Connected {Y}:{RS} {G} True ✔️️{RS} "
                        )
                    else:
                        print(
                            f"{' ' * 5}└[{R}•{RS}] {C}User Linkedin Connected {Y}:{RS} {R} False {R}❌️️{RS} "
                        )

                    if (
                        freelancer_Verifications_Data_Json["result"]["users"][
                            freelancer_Verifications_ID
                        ]["status"]["custom_charge_verified"]
                        == True
                    ):
                        print(
                            f"{' ' * 5}└[{Y}•{RS}] {C}User Custom Charge Verified {Y}:{RS} {G} True ✔️️{RS} "
                        )
                    else:
                        print(
                            f"{' ' * 5}└[{Y}•{RS}] {C}User Custom Charge Verified {Y}:{RS} {R} False {R}❌️️{RS} "
                        )

                if FREELANCER_Request.status_code == 404:
                    print(f"\n[{B} FREELANCER{RS} ]")
                    print(
                        f"{' ' * 5}└[{R}•{RS}] {C}User Info{Y}:{RS} {R}Sorry, we couldn't find that one ❗️{RS}"
                    )

            else:
                print(f"\n[{B} FREELANCER{RS} ]")

                print(
                    f"{' ' * 5}└[{R}•{RS}] {C}Connection Lost{Y}:{RS} {R}Oops! Unable To Establish A Connection{RS}"
                )
        except requests.exceptions.Timeout:
            print(f"\n[{B} FREELANCER{RS} ]")

            print(
                f"{' ' * 5}└[{R}•{RS}] {C}Timeout Error{Y}:{RS} {R}Oops! Timed Out{RS}"
            )
    except socket.gaierror:
        print(f"\n[{B} FREELANCER{RS} ]")

        print(
            f"{' ' * 5}└[{R}•{RS}] {C}DNS LookUp{Y}:{RS} {R}Oops! The {G}Dns Lookup{R} Failed And The Requested Domain Could Not Be Found.{RS}"
        )

    # [ TradingView ]

    try:
        ip_address = socket.gethostbyname("tradingview.com")
        # print('IP address:', ip_address)
        try:
            response = requests.get("https://www.tradingview.com", timeout=5)
            if response.status_code == 200:
                headers = {
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.33",
                }

                TradingView_Url = f"https://www.tradingview.com/u/{usernames}"

                TradingView_Request = requests.get(TradingView_Url, headers=headers)

                if TradingView_Request.status_code == 200:

                    print(f"\n[{B} TradingView{RS} ]")

                    print(
                        f"{' ' * 5}└[{R}•{RS}] {C}User Url {Y}:{RS} {TradingView_Url}"
                    )

                    TradingView_Soup = BeautifulSoup(
                        TradingView_Request.text, "html.parser"
                    )

                    TradingView_IMAGE = TradingView_Soup.find(
                        "meta", property="og:image:secure_url"
                    )

                    TradingView_NAME = TradingView_Soup.find(
                        "div", class_="tv-profile__main-block--container"
                    )

                    if not TradingView_NAME:
                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {R}Not Found ❗️{RS} "
                        )
                    else:
                        TradingView_NAMES = TradingView_NAME.find(
                            "h1", class_="tv-profile__name-text"
                        ).get_text()
                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {TradingView_NAMES}"
                        )

                    if not TradingView_IMAGE:
                        print(
                            f"{' ' * 5}└[{G}•{RS}] {C}User Profile Image {Y}:{RS} {R}Not Found ❗️{RS} "
                        )
                    else:
                        print(
                            f"{' ' * 5}└[{G}•{RS}] {C}User Image {Y}:{RS} {TradingView_IMAGE['content']}"
                        )

                if TradingView_Request.status_code == 404:
                    print(f"\n[{B} TradingView{RS} ]")
                    print(
                        f"{' ' * 5}└[{R}•{RS}] {C}User Info{Y}:{RS} {R}Sorry, we couldn't find that one ❗️{RS}"
                    )

            else:
                print(f"\n[{B} TradingView{RS} ]")

                print(
                    f"{' ' * 5}└[{R}•{RS}] {C}Connection Lost{Y}:{RS} {R}Oops! Unable To Establish A Connection{RS}"
                )
        except requests.exceptions.Timeout:
            print(f"\n[{B} TradingView{RS} ]")

            print(
                f"{' ' * 5}└[{R}•{RS}] {C}Timeout Error{Y}:{RS} {R}Oops! Timed Out{RS}"
            )
    except socket.gaierror:
        print(f"\n[{B} TradingView{RS} ]")

        print(
            f"{' ' * 5}└[{R}•{RS}] {C}DNS LookUp{Y}:{RS} {R}Oops! The {G}Dns Lookup{R} Failed And The Requested Domain Could Not Be Found.{RS}"
        )

    # [ GAANA ]

    try:
        ip_address = socket.gethostbyname("gaana.com")
        # print('IP address:', ip_address)
        try:
            response = requests.get("https://gaana.com", timeout=5)
            if response.status_code == 200:
                headers = {
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.33",
                }

                GAANA_Url = f"https://gaana.com/artist/{usernames}"

                GAANA_Request = requests.request("GET", GAANA_Url, headers=headers)

                if GAANA_Request.status_code == 200:
                    print(f"\n[{B} GAANA{RS} ]")
                    print(f"{' ' * 5}└[{R}•{RS}] {C}User Url{Y}:{RS} {GAANA_Url}")
                    GAANA_Soup = BeautifulSoup(GAANA_Request.text, "html.parser")

                    GAANA_USER_NAME = GAANA_Soup.find("div", attrs={"class": "info"})

                    if not GAANA_USER_NAME:
                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {R}Not Found ❗️{RS} "
                        )
                    else:
                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {GAANA_USER_NAME.find('div', attrs={'class': '_a'}).find('h1', attrs={'class': 'title t_over'}).string}"
                        )

                elif GAANA_Request.status_code == 404:
                    print(f"\n[{B} GAANA{RS} ]")
                    print(
                        f"{' ' * 5}└[{R}•{RS}] {C}User Info{Y}:{RS} {R}Sorry, we couldn't find that one ❗️{RS}"
                    )

            else:
                print(f"\n[{B} GAANA{RS} ]")

                print(
                    f"{' ' * 5}└[{R}•{RS}] {C}Connection Lost{Y}:{RS} {R}Oops! Unable To Establish A Connection{RS}"
                )
        except requests.exceptions.Timeout:
            print(f"\n[{B} GAANA{RS} ]")

            print(
                f"{' ' * 5}└[{R}•{RS}] {C}Timeout Error{Y}:{RS} {R}Oops! Timed Out{RS}"
            )
    except socket.gaierror:
        print(f"\n[{B} GAANA{RS} ]")

        print(
            f"{' ' * 5}└[{R}•{RS}] {C}DNS LookUp{Y}:{RS} {R}Oops! The {G}Dns Lookup{R} Failed And The Requested Domain Could Not Be Found.{RS}"
        )

    # [ FLICKR ]

    try:
        ip_address = socket.gethostbyname("flickr.com")
        # print('IP address:', ip_address)
        try:
            response = requests.get("https://www.flickr.com", timeout=5)
            if response.status_code == 200:
                FLICKR_Url = f"https://www.flickr.com/people/{usernames}/"

                FLICKR_Request = requests.get(FLICKR_Url)

                if FLICKR_Request.status_code == 200:

                    print(f"\n[{B} FLICKR{RS} ]")

                    print(f"{' ' * 5}└[{R}•{RS}] {C}User Url {Y}:{RS} {FLICKR_Url}")

                    FLICKR_Soup = BeautifulSoup(FLICKR_Request.text, "html.parser")

                    FLICKR_PROFILE_NAME = FLICKR_Soup.find(
                        "div", attrs={"class": "title-container"}
                    )
                    FLICKR_JOIN_DATE = FLICKR_Soup.find(
                        "div", attrs={"class": "infos-view-container"}
                    )
                    FLICKR_FOLLOWERS_FOLLOWING = FLICKR_Soup.find(
                        "div", attrs={"class": "metadata-container"}
                    )

                    if not FLICKR_PROFILE_NAME:
                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}User Seeking {Y}:{RS} {R}Not Found ❗️{RS} "
                        )
                    else:
                        seeking_space_remove = FLICKR_PROFILE_NAME.find("h1").getText()
                        After_remove_seeking_space = seeking_space_remove.strip()
                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {After_remove_seeking_space}"
                        )

                    if not FLICKR_JOIN_DATE:
                        print(
                            f"{' ' * 5}└[{Y}•{RS}] {C}User Seeking {Y}:{RS} {R}Not Found ❗️{RS} "
                        )
                    else:
                        seeking_space_remove = (
                            FLICKR_JOIN_DATE.find("ul")
                            .find("li")
                            .find("a", attrs={"class": "archives-link"})
                            .getText()
                        )
                        After_remove_seeking_space = seeking_space_remove.strip()
                        print(
                            f"{' ' * 5}└[{Y}•{RS}] {C}User Join FLICKR {Y}:{RS} {After_remove_seeking_space}"
                        )

                    if not FLICKR_FOLLOWERS_FOLLOWING:
                        print(
                            f"{' ' * 5}└[{G}•{RS}] {C}User Seeking {Y}:{RS} {R}Not Found ❗️{RS} "
                        )
                    else:
                        seeking_space_remove = (
                            FLICKR_FOLLOWERS_FOLLOWING.find(
                                "div", attrs={"class": "coverphoto-stats"}
                            )
                            .find("p")
                            .getText()
                        )
                        After_remove_seeking_space = seeking_space_remove.strip()
                        print(
                            f"{' ' * 5}└[{G}•{RS}] {C}User Followers & Following {Y}:{RS} {After_remove_seeking_space}"
                        )

                elif FLICKR_Request.status_code == 404:
                    print(f"\n[{B} FLICKR{RS} ]")
                    print(
                        f"{' ' * 5}└[{R}•{RS}] {C}User Info{Y}:{RS} {R}Sorry, we couldn't find that one ❗️{RS}"
                    )

            else:
                print(f"\n[{B} FLICKR{RS} ]")

                print(
                    f"{' ' * 5}└[{R}•{RS}] {C}Connection Lost{Y}:{RS} {R}Oops! Unable To Establish A Connection{RS}"
                )
        except requests.exceptions.Timeout:
            print(f"\n[{B} FLICKR{RS} ]")

            print(
                f"{' ' * 5}└[{R}•{RS}] {C}Timeout Error{Y}:{RS} {R}Oops! Timed Out{RS}"
            )
    except socket.gaierror:
        print(f"\n[{B} FLICKR{RS} ]")

        print(
            f"{' ' * 5}└[{R}•{RS}] {C}DNS LookUp{Y}:{RS} {R}Oops! The {G}Dns Lookup{R} Failed And The Requested Domain Could Not Be Found.{RS}"
        )

    # [ INDEPENDENT ACADEMIA ]

    try:
        ip_address = socket.gethostbyname("academia.edu")
        # print('IP address:', ip_address)
        try:
            response = requests.get("https://www.academia.edu", timeout=5)
            if response.status_code == 200:
                INDEPENDENT_ACADEMIA_URL = (
                    f"https://independent.academia.edu/{usernames}"
                )

                INDEPENDENT_ACADEMIA_Request = requests.get(INDEPENDENT_ACADEMIA_URL)

                if INDEPENDENT_ACADEMIA_Request.status_code == 200:

                    print(f"\n[{B} INDEPENDENT ACADEMIA{RS} ]")

                    INDEPENDENT_ACADEMIA_Soup = BeautifulSoup(
                        INDEPENDENT_ACADEMIA_Request.text, "html.parser"
                    )

                    INDEPENDENT_ACADEMIA_FULL_NAME = INDEPENDENT_ACADEMIA_Soup.find(
                        "div", attrs={"class": "profile-info-container"}
                    ).find("h1", attrs={"class": "ds-product-heading-lg"})

                    print(
                        f"{' ' * 5}└[{R}•{RS}] {C}User Url {Y}:{RS} {INDEPENDENT_ACADEMIA_URL}"
                    )

                    if not INDEPENDENT_ACADEMIA_FULL_NAME:
                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {R}Not Found ❗️{RS} "
                        )
                    else:
                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {INDEPENDENT_ACADEMIA_FULL_NAME.string}"
                        )

                elif INDEPENDENT_ACADEMIA_Request.status_code == 404:
                    print(f"\n[{B} INDEPENDENT ACADEMIA{RS} ]")
                    print(
                        f"{' ' * 5}└[{R}•{RS}] {C}User Info{Y}:{RS} {R}Sorry, we couldn't find that one ❗️{RS}"
                    )

            else:
                print(f"\n[{B} INDEPENDENT ACADEMIA{RS} ]")

                print(
                    f"{' ' * 5}└[{R}•{RS}] {C}Connection Lost{Y}:{RS} {R}Oops! Unable To Establish A Connection{RS}"
                )
        except requests.exceptions.Timeout:
            print(f"\n[{B} INDEPENDENT ACADEMIA{RS} ]")

            print(
                f"{' ' * 5}└[{R}•{RS}] {C}Timeout Error{Y}:{RS} {R}Oops! Timed Out{RS}"
            )
    except socket.gaierror:
        print(f"\n[{B} INDEPENDENT ACADEMIA{RS} ]")

        print(
            f"{' ' * 5}└[{R}•{RS}] {C}DNS LookUp{Y}:{RS} {R}Oops! The {G}Dns Lookup{R} Failed And The Requested Domain Could Not Be Found.{RS}"
        )

    # [ DEVELOPER APPLE ]

    try:
        ip_address = socket.gethostbyname("developer.apple.com")
        # print('IP address:', ip_address)
        try:
            response = requests.get("https://developer.apple.com", timeout=5)
            if response.status_code == 200:
                DEVELOPER_APPLE_URL = (
                    f"https://developer.apple.com/forums/profile/{usernames}"
                )

                DEVELOPER_APPLE_Request = requests.get(DEVELOPER_APPLE_URL)

                if DEVELOPER_APPLE_Request.status_code == 200:

                    print(f"\n[{B} DEVELOPER APPLE{RS} ]")

                    ANILIST_Soup = BeautifulSoup(
                        DEVELOPER_APPLE_Request.text, "html.parser"
                    )

                    DEVELOPER_APPLE_NAME = ANILIST_Soup.find(
                        "section", attrs={"class": "user-info-box"}
                    )

                    print(
                        f"{' ' * 5}└[{R}•{RS}] {C}User Url {Y}:{RS} {DEVELOPER_APPLE_URL}"
                    )

                    if not DEVELOPER_APPLE_NAME:
                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {R}Not Found ❗️{RS} "
                        )
                    else:
                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {DEVELOPER_APPLE_NAME.find('div', attrs={'class': 'user-name-reputation'}).find('h2').getText()}"
                        )

                elif DEVELOPER_APPLE_Request.status_code == 404:
                    print(f"\n[{B} DEVELOPER APPLE{RS} ]")
                    print(
                        f"{' ' * 5}└[{R}•{RS}] {C}User Info{Y}:{RS} {R}Sorry, we couldn't find that one ❗️{RS}"
                    )

            else:
                print(f"\n[{B} DEVELOPER APPLE{RS} ]")

                print(
                    f"{' ' * 5}└[{R}•{RS}] {C}Connection Lost{Y}:{RS} {R}Oops! Unable To Establish A Connection{RS}"
                )
        except requests.exceptions.Timeout:
            print(f"\n[{B} DEVELOPER APPLE{RS} ]")

            print(
                f"{' ' * 5}└[{R}•{RS}] {C}Timeout Error{Y}:{RS} {R}Oops! Timed Out{RS}"
            )
    except socket.gaierror:
        print(f"\n[{B} DEVELOPER APPLE{RS} ]")

        print(
            f"{' ' * 5}└[{R}•{RS}] {C}DNS LookUp{Y}:{RS} {R}Oops! The {G}Dns Lookup{R} Failed And The Requested Domain Could Not Be Found.{RS}"
        )

    # [ VIDEOHIVE NET ]

    try:
        ip_address = socket.gethostbyname("videohive.net")
        # print('IP address:', ip_address)
        try:
            response = requests.get("https://videohive.net", timeout=5)
            if response.status_code == 200:
                VIDEOHIVE_URL = f"https://videohive.net/user/{usernames}"

                headers = {
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.33",
                }

                VIDEOHIVE_URL_Request = requests.request(
                    "GET", VIDEOHIVE_URL, headers=headers
                )

                if VIDEOHIVE_URL_Request.status_code == 200:

                    print(f"\n[{B} VIDEOHIVE NET{RS} ]")

                    VIDEOHIVE_Soup = BeautifulSoup(
                        VIDEOHIVE_URL_Request.text, "html.parser"
                    )

                    VIDEOHIVE_NAME = VIDEOHIVE_Soup.find(
                        "div", attrs={"class": "user-info-header h-mb0"}
                    ).find("h1")
                    VIDEOHIVE_LOCATION = VIDEOHIVE_Soup.find(
                        "div", attrs={"class": "user-info-header h-mb0"}
                    ).find("p")
                    VIDEOHIVE_SALES = VIDEOHIVE_Soup.find(
                        "div", attrs={"class": "user-info-header h-mb0"}
                    ).find("strong", attrs={"class": "t-heading -size-m"})

                    print(f"{' ' * 5}└[{R}•{RS}] {C}User Url {Y}:{RS} {VIDEOHIVE_URL}")

                    if not VIDEOHIVE_NAME:
                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {R}Not Found ❗️{RS} "
                        )
                    else:
                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {VIDEOHIVE_NAME.getText()}"
                        )

                    if not VIDEOHIVE_LOCATION:
                        print(
                            f"{' ' * 5}└[{Y}•{RS}] {C}User Location {Y}:{RS} {R}Not Found ❗️{RS} "
                        )
                    else:
                        name_THERMI_NAME_SPACE_REMOVE = VIDEOHIVE_LOCATION.getText()

                        name_THERMI_SPACE_REMOVE_RESULT = (
                            name_THERMI_NAME_SPACE_REMOVE.strip()
                        )

                        print(
                            f"{' ' * 5}└[{Y}•{RS}] {C}User Location {Y}:{RS} {name_THERMI_SPACE_REMOVE_RESULT}"
                        )

                    if not VIDEOHIVE_SALES:
                        print(
                            f"{' ' * 5}└[{G}•{RS}] {C}User Sales {Y}:{RS} {R}Not Found ❗️{RS} "
                        )
                    else:
                        name_THERMI_NAME_SPACE_REMOVE = VIDEOHIVE_SALES.getText()

                        name_THERMI_SPACE_REMOVE_RESULT = (
                            name_THERMI_NAME_SPACE_REMOVE.strip()
                        )

                        print(
                            f"{' ' * 5}└[{G}•{RS}] {C}User Sales {Y}:{RS} {name_THERMI_SPACE_REMOVE_RESULT}"
                        )

                elif VIDEOHIVE_URL_Request.status_code == 404:
                    print(f"\n[{B} VIDEOHIVE NET{RS} ]")
                    print(
                        f"{' ' * 5}└[{R}•{RS}] {C}User Info{Y}:{RS} {R}Sorry, we couldn't find that one ❗️{RS}"
                    )

            else:
                print(f"\n[{B} VIDEOHIVE NET{RS} ]")

                print(
                    f"{' ' * 5}└[{R}•{RS}] {C}Connection Lost{Y}:{RS} {R}Oops! Unable To Establish A Connection{RS}"
                )
        except requests.exceptions.Timeout:
            print(f"\n[{B} VIDEOHIVE NET{RS} ]")

            print(
                f"{' ' * 5}└[{R}•{RS}] {C}Timeout Error{Y}:{RS} {R}Oops! Timed Out{RS}"
            )
    except socket.gaierror:
        print(f"\n[{B} VIDEOHIVE NET{RS} ]")

        print(
            f"{' ' * 5}└[{R}•{RS}] {C}DNS LookUp{Y}:{RS} {R}Oops! The {G}Dns Lookup{R} Failed And The Requested Domain Could Not Be Found.{RS}"
        )

    # [ BANDCAMP ]

    try:
        ip_address = socket.gethostbyname("bandcamp.com")
        # print('IP address:', ip_address)
        try:
            response = requests.get("https://bandcamp.com", timeout=5)
            if response.status_code == 200:
                BANDCAMP_URL = f"https://bandcamp.com/{usernames}"

                headers = {
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.33",
                }

                BANDCAMP_URL_Request = requests.request(
                    "GET", BANDCAMP_URL, headers=headers
                )

                if BANDCAMP_URL_Request.status_code == 200:

                    print(f"\n[{B} BANDCAMP{RS} ]")

                    BANDCAMP_Soup = BeautifulSoup(
                        BANDCAMP_URL_Request.text, "html.parser"
                    )

                    BANDCAMP_NAME = BANDCAMP_Soup.find(
                        "div", attrs={"class": "name"}
                    ).find("h1")
                    BANDCAMP_LOCATION = BANDCAMP_Soup.find(
                        "div", attrs={"class": "info"}
                    ).find("li")

                    print(f"{' ' * 5}└[{R}•{RS}] {C}User Url {Y}:{RS} {BANDCAMP_URL}")

                    if not BANDCAMP_NAME:
                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {R}Not Found ❗️{RS} "
                        )
                    else:
                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {BANDCAMP_NAME.getText()}"
                        )

                    if not BANDCAMP_LOCATION:
                        print(
                            f"{' ' * 5}└[{Y}•{RS}] {C}User Location {Y}:{RS} {R}Not Found ❗️{RS} "
                        )
                    else:
                        print(
                            f"{' ' * 5}└[{Y}•{RS}] {C}User Location {Y}:{RS} {BANDCAMP_LOCATION.getText()}"
                        )

                elif BANDCAMP_URL_Request.status_code == 404:
                    print(f"\n[{B} BANDCAMP{RS} ]")
                    print(
                        f"{' ' * 5}└[{R}•{RS}] {C}User Info{Y}:{RS} {R}Sorry, we couldn't find that one ❗️{RS}"
                    )

            else:
                print(f"\n[{B} BANDCAMP{RS} ]")

                print(
                    f"{' ' * 5}└[{R}•{RS}] {C}Connection Lost{Y}:{RS} {R}Oops! Unable To Establish A Connection{RS}"
                )
        except requests.exceptions.Timeout:
            print(f"\n[{B} BANDCAMP{RS} ]")

            print(
                f"{' ' * 5}└[{R}•{RS}] {C}Timeout Error{Y}:{RS} {R}Oops! Timed Out{RS}"
            )
    except socket.gaierror:
        print(f"\n[{B} BANDCAMP{RS} ]")

        print(
            f"{' ' * 5}└[{R}•{RS}] {C}DNS LookUp{Y}:{RS} {R}Oops! The {G}Dns Lookup{R} Failed And The Requested Domain Could Not Be Found.{RS}"
        )

    # [ BEZUZYTECZNA ]

    try:
        ip_address = socket.gethostbyname("bezuzyteczna.pl")
        # print('IP address:', ip_address)
        try:
            response = requests.get("https://bezuzyteczna.pl", timeout=5)
            if response.status_code == 200:
                BEHANCE_URL = f"https://bezuzyteczna.pl/uzytkownicy/{usernames}"

                headers = {
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.33",
                }

                BEHANCE_URL_Request = requests.request(
                    "GET", BEHANCE_URL, headers=headers
                )

                if BEHANCE_URL_Request.status_code == 200:

                    print(f"\n[{B} BEZUZYTECZNA{RS} ]")

                    BEHANCE_Soup = BeautifulSoup(
                        BEHANCE_URL_Request.text, "html.parser"
                    )

                    BANDCAMP_NAME = BEHANCE_Soup.find(
                        "div", attrs={"class": "p-panel__name"}
                    )
                    BANDCAMP_JOINED = BEHANCE_Soup.find(
                        "div", attrs={"class": "p-panel__info-line"}
                    ).find("span", attrs={"p-panel__info-right"})

                    print(f"{' ' * 5}└[{R}•{RS}] {C}User Url {Y}:{RS} {BEHANCE_URL}")

                    if not BANDCAMP_NAME:
                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {R}Not Found ❗️{RS} "
                        )
                    else:
                        name_THERMI_NAME_SPACE_REMOVE = BANDCAMP_NAME.getText()

                        name_THERMI_SPACE_REMOVE_RESULT = (
                            name_THERMI_NAME_SPACE_REMOVE.strip()
                        )
                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {name_THERMI_SPACE_REMOVE_RESULT}"
                        )

                    if not BANDCAMP_JOINED:
                        print(
                            f"{' ' * 5}└[{Y}•{RS}] {C}User Joined {Y}:{RS} {R}Not Found ❗️{RS} "
                        )
                    else:
                        print(
                            f"{' ' * 5}└[{Y}•{RS}] {C}User Joined {Y}:{RS} {BANDCAMP_JOINED.getText()}"
                        )

                elif BEHANCE_URL_Request.status_code == 404:
                    print(f"\n[{B} BEZUZYTECZNA{RS} ]")
                    print(
                        f"{' ' * 5}└[{R}•{RS}] {C}User Info{Y}:{RS} {R}Sorry, we couldn't find that one ❗️{RS}"
                    )

            else:
                print(f"\n[{B} BEZUZYTECZNA{RS} ]")

                print(
                    f"{' ' * 5}└[{R}•{RS}] {C}Connection Lost{Y}:{RS} {R}Oops! Unable To Establish A Connection{RS}"
                )
        except requests.exceptions.Timeout:
            print(f"\n[{B} BEZUZYTECZNA{RS} ]")

            print(
                f"{' ' * 5}└[{R}•{RS}] {C}Timeout Error{Y}:{RS} {R}Oops! Timed Out{RS}"
            )
    except socket.gaierror:
        print(f"\n[{B} BEZUZYTECZNA{RS} ]")

        print(
            f"{' ' * 5}└[{R}•{RS}] {C}DNS LookUp{Y}:{RS} {R}Oops! The {G}Dns Lookup{R} Failed And The Requested Domain Could Not Be Found.{RS}"
        )

    # [ BIKEMAP ]

    try:
        ip_address = socket.gethostbyname("bikemap.net")
        # print('IP address:', ip_address)
        try:
            response = requests.get("https://www.bikemap.net", timeout=5)
            if response.status_code == 200:
                BIKEMAP_URL = (
                    f"https://www.bikemap.net/en/u/{usernames}/routes/created/"
                )

                headers = {
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.33",
                }

                BIKEMAP_URL_Request = requests.request(
                    "GET", BIKEMAP_URL, headers=headers
                )

                if BIKEMAP_URL_Request.status_code == 200:

                    print(f"\n[{B} BIKEMAP{RS} ]")

                    BIKEMAP_Soup = BeautifulSoup(
                        BIKEMAP_URL_Request.text, "html.parser"
                    )

                    BIKEMAP_NAME = BIKEMAP_Soup.find(
                        "div", attrs={"class": "col-sm-10"}
                    ).find("h1", attrs={"class": "title mr"})
                    BIKEMAP_JOIN = BIKEMAP_Soup.find(
                        "div", attrs={"class": "title-info"}
                    ).find("span", attrs={"class": "member-since"})
                    BIKEMAP_LOCATION = BIKEMAP_Soup.find(
                        "div", attrs={"class": "title-info"}
                    ).find("span", attrs={"class": "location"})
                    BIKEMAP_PROFILE_PIC = BIKEMAP_Soup.find(
                        "div", attrs={"class": "col-sm-2"}
                    ).findAll("img")

                    BIKEMAP_PROFILE_PICS = BIKEMAP_PROFILE_PIC[0]

                    print(f"{' ' * 5}└[{R}•{RS}] {C}User Url {Y}:{RS} {BIKEMAP_URL}")

                    if not BIKEMAP_NAME:
                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {R}Not Found ❗️{RS} "
                        )
                    else:
                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {BIKEMAP_NAME.getText()}"
                        )

                    if not BIKEMAP_JOIN:
                        print(
                            f"{' ' * 5}└[{Y}•{RS}] {C}User Joined {Y}:{RS} {R}Not Found ❗️{RS} "
                        )
                    else:
                        print(
                            f"{' ' * 5}└[{Y}•{RS}] {C}User Joined {Y}:{RS} {BIKEMAP_JOIN.getText()}"
                        )

                    if not BIKEMAP_LOCATION:
                        print(
                            f"{' ' * 5}└[{G}•{RS}] {C}User Location {Y}:{RS} {R}Not Found ❗️{RS} "
                        )
                    else:
                        print(
                            f"{' ' * 5}└[{G}•{RS}] {C}User Location {Y}:{RS} {BIKEMAP_LOCATION.getText()}"
                        )

                    if not BIKEMAP_PROFILE_PICS:
                        print(
                            f"{' ' * 5}└[{R}•{RS}] {C}User Profile Photo {Y}:{RS} {R}Not Found ❗️{RS} "
                        )
                    else:
                        print(
                            f"{' ' * 5}└[{R}•{RS}] {C}User Profile Photo {Y}:{RS} {BIKEMAP_PROFILE_PICS.attrs['src']}"
                        )

                elif BIKEMAP_URL_Request.status_code == 404:
                    print(f"\n[{B} BIKEMAP{RS} ]")
                    print(
                        f"{' ' * 5}└[{R}•{RS}] {C}User Info{Y}:{RS} {R}Sorry, we couldn't find that one ❗️{RS}"
                    )

            else:
                print(f"\n[{B} BIKEMAP{RS} ]")

                print(
                    f"{' ' * 5}└[{R}•{RS}] {C}Connection Lost{Y}:{RS} {R}Oops! Unable To Establish A Connection{RS}"
                )
        except requests.exceptions.Timeout:
            print(f"\n[{B} BIKEMAP{RS} ]")

            print(
                f"{' ' * 5}└[{R}•{RS}] {C}Timeout Error{Y}:{RS} {R}Oops! Timed Out{RS}"
            )
    except socket.gaierror:
        print(f"\n[{B} BIKEMAP{RS} ]")

        print(
            f"{' ' * 5}└[{R}•{RS}] {C}DNS LookUp{Y}:{RS} {R}Oops! The {G}Dns Lookup{R} Failed And The Requested Domain Could Not Be Found.{RS}"
        )

    # [ FORUM DANGEROUSTHINGS ]

    try:
        ip_address = socket.gethostbyname("forum.dangerousthings.com")
        # print('IP address:', ip_address)
        try:
            response = requests.get("https://forum.dangerousthings.com", timeout=5)
            if response.status_code == 200:
                FORUM_DANGEROUSTHINGS_URL = (
                    f"https://forum.dangerousthings.com/u/{usernames}"
                )

                headers = {
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.33",
                }

                FORUM_DANGEROUSTHINGS_URL_Request = requests.request(
                    "GET", FORUM_DANGEROUSTHINGS_URL, headers=headers
                )

                if FORUM_DANGEROUSTHINGS_URL_Request.status_code == 200:
                    print(f"\n[{B} FORUM DANGEROUSTHINGS{RS} ]")
                    print(
                        f"{' ' * 5}└[{R}•{RS}] {C}User Url{Y}:{RS} {FORUM_DANGEROUSTHINGS_URL}"
                    )

                    FORUM_DANGEROUSTHINGS_Soup = BeautifulSoup(
                        FORUM_DANGEROUSTHINGS_URL_Request.text, "html.parser"
                    )

                    FORUM_DANGEROUSTHINGS_NAME = FORUM_DANGEROUSTHINGS_Soup.find(
                        "div", attrs={"class": "user-crawler"}
                    ).find("h2", attrs={"class": "username"})

                    FORUM_DANGEROUSTHINGS_BIO = FORUM_DANGEROUSTHINGS_Soup.find("p")

                    if not FORUM_DANGEROUSTHINGS_NAME:
                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {R}Not Found ❗️{RS} "
                        )
                    else:
                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {FORUM_DANGEROUSTHINGS_NAME.getText()}"
                        )

                    if not FORUM_DANGEROUSTHINGS_BIO:
                        print(
                            f"{' ' * 5}└[{Y}•{RS}] {C}User Bio {Y}:{RS} {R}Not Found ❗️{RS} "
                        )
                    else:
                        print(
                            f"{' ' * 5}└[{Y}•{RS}] {C}User Bio {Y}:{RS} {FORUM_DANGEROUSTHINGS_BIO.getText()}"
                        )

                        UserMention_Bio = FORUM_DANGEROUSTHINGS_BIO.getText()

                        Mention_Bio = re.findall(r"@[A-Za-z0-9.-]+", UserMention_Bio)

                        print(
                            f"{' ' * 5}└[{G}•{RS}] {C}List Of People Mention On USER Bio{Y}:{RS}"
                        )

                        if not Mention_Bio:
                            print(
                                f"{' ' * 20}└[{R}•{RS}] {Y}Mention Pople {C}On Bio {Y}:{RS} {R}Not Found ❗️{RS} \n"
                            )
                        else:
                            count = 0
                            for Mention_Bios in Mention_Bio:
                                count += 1
                                print(
                                    f"{' ' * 20}└[{R}{count}{RS}] {G}►{RS} {Mention_Bios}"
                                )

                        UserEmail = FORUM_DANGEROUSTHINGS_BIO.getText()

                        emails = re.findall(r"[\w\.-]+@[\w\.-]+", UserEmail)

                        print(
                            f"{' ' * 5}└[{R}•{RS}] {C}List Of Email Write On USER Bio{Y}:{RS}"
                        )

                        if not emails:
                            print(
                                f"{' ' * 20}└[{R}•{RS}] {C}Find {Y}Email {C}On Bio {Y}:{RS} {R}Not Found ❗️{RS} \n"
                            )
                        else:
                            count = 0
                        for email in emails:
                            count += 1
                            print(f"{' ' * 20}└[{R}{count}{RS}] {G}►{RS} {email}")

                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}List Of PhoneNumber Or Any Digit On USER Bio{Y}:{RS}"
                        )

                        PhoneNumberbio = FORUM_DANGEROUSTHINGS_BIO.getText()

                        PhoneNumbers = re.findall(r"\d+", PhoneNumberbio)

                        if not PhoneNumbers:
                            print(
                                f"{' ' * 20}└[{B}•{RS}] {C}Find {Y}PhoneNumber {C}On Bio {Y}:{RS} {R}Not Found ❗️{RS} "
                            )
                        else:
                            count = 0
                        for PhoneNumber in PhoneNumbers:
                            count += 1
                            print(f"{' ' * 20}└[{R}{count}{RS}] {G}►{RS} {PhoneNumber}")

                elif FORUM_DANGEROUSTHINGS_URL_Request.status_code == 404:
                    print(f"\n[{B} FORUM DANGEROUSTHINGS{RS} ]")
                    print(
                        f"{' ' * 5}└[{R}•{RS}] {C}User Info{Y}:{RS} {R}Sorry, we couldn't find that one ❗️{RS}"
                    )

            else:
                print(f"\n[{B} FORUM DANGEROUSTHINGS{RS} ]")

                print(
                    f"{' ' * 5}└[{R}•{RS}] {C}Connection Lost{Y}:{RS} {R}Oops! Unable To Establish A Connection{RS}"
                )
        except requests.exceptions.Timeout:
            print(f"\n[{B} FORUM DANGEROUSTHINGS{RS} ]")

            print(
                f"{' ' * 5}└[{R}•{RS}] {C}Timeout Error{Y}:{RS} {R}Oops! Timed Out{RS}"
            )
    except socket.gaierror:
        print(f"\n[{B} FORUM DANGEROUSTHINGS{RS} ]")

        print(
            f"{' ' * 5}└[{R}•{RS}] {C}DNS LookUp{Y}:{RS} {R}Oops! The {G}Dns Lookup{R} Failed And The Requested Domain Could Not Be Found.{RS}"
        )

    # [ COMMUNITY BITWARDEN ]

    try:
        ip_address = socket.gethostbyname("community.bitwarden.com")
        # print('IP address:', ip_address)
        try:
            response = requests.get("https://community.bitwarden.com", timeout=5)
            if response.status_code == 200:
                COMMUNITY_BITWARDEN_URL = (
                    f"https://community.bitwarden.com/u/{usernames}/summary"
                )

                headers = {
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.33",
                }

                COMMUNITY_BITWARDEN_URL_Request = requests.request(
                    "GET", COMMUNITY_BITWARDEN_URL, headers=headers
                )

                if COMMUNITY_BITWARDEN_URL_Request.status_code == 200:
                    print(f"\n[{B} COMMUNITY BITWARDEN{RS} ]")
                    print(
                        f"{' ' * 5}└[{R}•{RS}] {C}User Url{Y}:{RS} {COMMUNITY_BITWARDEN_URL}"
                    )

                    COMMUNITY_BITWARDEN_Soup = BeautifulSoup(
                        COMMUNITY_BITWARDEN_URL_Request.text, "html.parser"
                    )

                    COMMUNITY_BITWARDEN_PROFILE_PICS = COMMUNITY_BITWARDEN_Soup.find(
                        "div", attrs={"id": "main-outlet"}
                    ).findAll("img")

                    COMMUNITY_BITWARDEN_PROFILE_NAME = COMMUNITY_BITWARDEN_Soup.find(
                        "div", attrs={"id": "main-outlet"}
                    ).find("h2", attrs={"class": "username"})

                    COMMUNITY_BITWARDEN_PROFILE_PICS = COMMUNITY_BITWARDEN_PROFILE_PICS[
                        0
                    ]

                    if not COMMUNITY_BITWARDEN_PROFILE_NAME:
                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {R}Not Found ❗️{RS} "
                        )
                    else:
                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {COMMUNITY_BITWARDEN_PROFILE_NAME.getText()}"
                        )

                    if not COMMUNITY_BITWARDEN_PROFILE_PICS:
                        print(
                            f"{' ' * 5}└[{Y}•{RS}] {C}User Profile Photo {Y}:{RS} {R}Not Found ❗️{RS} "
                        )
                    else:
                        print(
                            f"{' ' * 5}└[{Y}•{RS}] {C}User Profile Photo {Y}:{RS} {COMMUNITY_BITWARDEN_PROFILE_PICS.attrs['src']}"
                        )

                elif COMMUNITY_BITWARDEN_URL_Request.status_code == 404:
                    print(f"\n[{B} COMMUNITY BITWARDEN{RS} ]")
                    print(
                        f"{' ' * 5}└[{R}•{RS}] {C}User Info{Y}:{RS} {R}Sorry, we couldn't find that one ❗️{RS}"
                    )

            else:
                print(f"\n[{B} COMMUNITY BITWARDEN{RS} ]")

                print(
                    f"{' ' * 5}└[{R}•{RS}] {C}Connection Lost{Y}:{RS} {R}Oops! Unable To Establish A Connection{RS}"
                )
        except requests.exceptions.Timeout:
            print(f"\n[{B} COMMUNITY BITWARDEN{RS} ]")

            print(
                f"{' ' * 5}└[{R}•{RS}] {C}Timeout Error{Y}:{RS} {R}Oops! Timed Out{RS}"
            )
    except socket.gaierror:
        print(f"\n[{B} COMMUNITY BITWARDEN{RS} ]")

        print(
            f"{' ' * 5}└[{R}•{RS}] {C}DNS LookUp{Y}:{RS} {R}Oops! The {G}Dns Lookup{R} Failed And The Requested Domain Could Not Be Found.{RS}"
        )

    # [ BOOKCROSSING ]

    try:
        ip_address = socket.gethostbyname("facebook.com")
        # print('IP address:', ip_address)
        try:
            response = requests.get("https://www.facebook.com", timeout=5)
            if response.status_code == 200:
                BOOKCROSSING_URL = (
                    f"https://www.bookcrossing.com/mybookshelf/{usernames}/"
                )

                headers = {
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.33",
                }

                BOOKCROSSING_URL_Request = requests.request(
                    "GET", BOOKCROSSING_URL, headers=headers
                )

                if BOOKCROSSING_URL_Request.status_code == 200:
                    print(f"\n[{B} BOOKCROSSING{RS} ]")
                    print(
                        f"{' ' * 5}└[{R}•{RS}] {C}User Url{Y}:{RS} {BOOKCROSSING_URL}"
                    )

                    BOOKCROSSING_Soup = BeautifulSoup(
                        BOOKCROSSING_URL_Request.text, "html.parser"
                    )

                    BOOKCROSSING_NAME = BOOKCROSSING_Soup.find(
                        "div", attrs={"class": "col small"}
                    ).find("h2")

                    if not BOOKCROSSING_NAME:
                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {R}Not Found ❗️{RS} "
                        )
                    else:
                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {BOOKCROSSING_NAME.getText()}"
                        )

                elif BOOKCROSSING_URL_Request.status_code == 404:
                    print(f"\n[{B} BOOKCROSSING{RS} ]")
                    print(
                        f"{' ' * 5}└[{R}•{RS}] {C}User Info{Y}:{RS} {R}Sorry, we couldn't find that one ❗️{RS}"
                    )

            else:
                print(f"\n[{B} BOOKCROSSING{RS} ]")

                print(
                    f"{' ' * 5}└[{R}•{RS}] {C}Connection Lost{Y}:{RS} {R}Oops! Unable To Establish A Connection{RS}"
                )
        except requests.exceptions.Timeout:
            print(f"\n[{B} BOOKCROSSING{RS} ]")

            print(
                f"{' ' * 5}└[{R}•{RS}] {C}Timeout Error{Y}:{RS} {R}Oops! Timed Out{RS}"
            )
    except socket.gaierror:
        print(f"\n[{B} BOOKCROSSING{RS} ]")

        print(
            f"{' ' * 5}└[{R}•{RS}] {C}DNS LookUp{Y}:{RS} {R}Oops! The {G}Dns Lookup{R} Failed And The Requested Domain Could Not Be Found.{RS}"
        )

    # [ BUY ME A COFFEE ]

    try:
        ip_address = socket.gethostbyname("buymeacoffee.com")
        # print('IP address:', ip_address)
        try:
            response = requests.get("https://www.buymeacoffee.com", timeout=5)
            if response.status_code == 200:
                BUY_ME_A_COFFEE_URL = f"https://www.buymeacoffee.com/{usernames}"

                headers = {
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.33",
                }

                BUY_ME_A_COFFEE_URL_Request = requests.request(
                    "GET", BUY_ME_A_COFFEE_URL, headers=headers
                )

                if BUY_ME_A_COFFEE_URL_Request.status_code == 200:
                    print(f"\n[{B} BUY ME A COFFEE{RS} ]")
                    print(
                        f"{' ' * 5}└[{R}•{RS}] {C}User Url{Y}:{RS} {BUY_ME_A_COFFEE_URL}"
                    )

                    BUY_ME_A_COFFEE_Soup = BeautifulSoup(
                        BUY_ME_A_COFFEE_URL_Request.text, "html.parser"
                    )

                    BUY_ME_A_COFFEE_NAME = (
                        BUY_ME_A_COFFEE_Soup.find(
                            "div",
                            attrs={
                                "class": "p-relative dis-inline-block w-100 xs-pd-l-16 xs-pd-r-16"
                            },
                        )
                        .find("h1")
                        .find_all("span")
                    )
                    BUY_ME_A_COFFEE_DESCRIPTION = (
                        BUY_ME_A_COFFEE_Soup.find(
                            "div",
                            attrs={
                                "class": "p-relative dis-inline-block w-100 xs-pd-l-16 xs-pd-r-16"
                            },
                        )
                        .find("h1")
                        .find_all("span")
                    )
                    BUY_ME_A_COFFEE_PROFILE_PHOTO = BUY_ME_A_COFFEE_Soup.find(
                        "div", attrs={"class": "ctr-img-w-h mg-0-a"}
                    ).findAll("img")

                    BUY_ME_A_COFFEE_PROFILE_PROFILE_PICS = (
                        BUY_ME_A_COFFEE_PROFILE_PHOTO[0]
                    )

                    if not BUY_ME_A_COFFEE_NAME:
                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {R}Not Found ❗️{RS} "
                        )
                    else:
                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {BUY_ME_A_COFFEE_NAME[0].getText()}"
                        )

                    if not BUY_ME_A_COFFEE_DESCRIPTION:
                        print(
                            f"{' ' * 5}└[{Y}•{RS}] {C}User Description {Y}:{RS} {R}Not Found ❗️{RS} "
                        )
                    else:
                        print(
                            f"{' ' * 5}└[{Y}•{RS}] {C}User Description {Y}:{RS} {BUY_ME_A_COFFEE_DESCRIPTION[1].getText()}"
                        )

                        UserMention_Bio = BUY_ME_A_COFFEE_DESCRIPTION[1].getText()

                        Mention_Bio = re.findall(r"@[A-Za-z0-9.-]+", UserMention_Bio)

                        print(
                            f"{' ' * 5}└[{G}•{RS}] {C}List Of People Mention On USER Bio{Y}:{RS}"
                        )

                        if not Mention_Bio:
                            print(
                                f"{' ' * 20}└[{R}•{RS}] {Y}Mention Pople {C}On Bio {Y}:{RS} {R}Not Found ❗️{RS} \n"
                            )
                        else:
                            count = 0
                            for Mention_Bios in Mention_Bio:
                                count += 1
                                print(
                                    f"{' ' * 20}└[{R}{count}{RS}] {G}►{RS} {Mention_Bios}"
                                )

                        UserEmail = BUY_ME_A_COFFEE_DESCRIPTION[1].getText()

                        emails = re.findall(r"[\w\.-]+@[\w\.-]+", UserEmail)

                        print(
                            f"{' ' * 5}└[{R}•{RS}] {C}List Of Email Write On USER Bio{Y}:{RS}"
                        )

                        if not emails:
                            print(
                                f"{' ' * 20}└[{R}•{RS}] {C}Find {Y}Email {C}On Bio {Y}:{RS} {R}Not Found ❗️{RS} \n"
                            )
                        else:
                            count = 0
                        for email in emails:
                            count += 1
                            print(f"{' ' * 20}└[{R}{count}{RS}] {G}►{RS} {email}")

                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}List Of PhoneNumber Or Any Digit On USER Bio{Y}:{RS}"
                        )

                        PhoneNumberbio = BUY_ME_A_COFFEE_DESCRIPTION[1].getText()

                        PhoneNumbers = re.findall(r"\d+", PhoneNumberbio)

                        if not PhoneNumbers:
                            print(
                                f"{' ' * 20}└[{R}•{RS}] {C}Find {Y}PhoneNumber {C}On Bio {Y}:{RS} {R}Not Found ❗️{RS} "
                            )
                        else:
                            count = 0
                        for PhoneNumber in PhoneNumbers:
                            count += 1
                            print(f"{' ' * 20}└[{R}{count}{RS}] {G}►{RS} {PhoneNumber}")

                    if not BUY_ME_A_COFFEE_PROFILE_PROFILE_PICS:
                        print(
                            f"\n{' ' * 5}└[{G}•{RS}] {C}User Profile Photo {Y}:{RS} {R}Not Found ❗️{RS} "
                        )
                    else:
                        print(
                            f"\n{' ' * 5}└[{G}•{RS}] {C}User Profile Photo {Y}:{RS} {BUY_ME_A_COFFEE_PROFILE_PROFILE_PICS.attrs['data-src']}"
                        )

                elif BUY_ME_A_COFFEE_URL_Request.status_code == 404:
                    print(f"\n[{B} BUY ME A COFFEE{RS} ]")
                    print(
                        f"{' ' * 5}└[{R}•{RS}] {C}User Info{Y}:{RS} {R}Sorry, we couldn't find that one ❗️{RS}"
                    )

            else:
                print(f"\n[{B} BUY ME A COFFEE{RS} ]")

                print(
                    f"{' ' * 5}└[{R}•{RS}] {C}Connection Lost{Y}:{RS} {R}Oops! Unable To Establish A Connection{RS}"
                )
        except requests.exceptions.Timeout:
            print(f"\n[{B} BUY ME A COFFEE{RS} ]")

            print(
                f"{' ' * 5}└[{R}•{RS}] {C}Timeout Error{Y}:{RS} {R}Oops! Timed Out{RS}"
            )
    except socket.gaierror:
        print(f"\n[{B} BUY ME A COFFEE{RS} ]")

        print(
            f"{' ' * 5}└[{R}•{RS}] {C}DNS LookUp{Y}:{RS} {R}Oops! The {G}Dns Lookup{R} Failed And The Requested Domain Could Not Be Found.{RS}"
        )

    # [ BUZZFEED ]

    try:
        ip_address = socket.gethostbyname("buzzfeed.com")
        # print('IP address:', ip_address)
        try:
            response = requests.get("https://www.buzzfeed.com", timeout=5)
            if response.status_code == 200:
                BUZZFEED_URL = f"https://www.buzzfeed.com/{usernames}"

                headers = {
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.33",
                }

                BUZZFEED_URL_Request = requests.request(
                    "GET", BUZZFEED_URL, headers=headers
                )

                if BUZZFEED_URL_Request.status_code == 200:
                    print(f"\n[{B} BUZZFEED{RS} ]")
                    print(f"{' ' * 5}└[{R}•{RS}] {C}User Url{Y}:{RS} {BUZZFEED_URL}")

                    BUZZFEED_Soup = BeautifulSoup(
                        BUZZFEED_URL_Request.text, "html.parser"
                    )

                    BUZZFEED_NAME = BUZZFEED_Soup.find(
                        "div", attrs={"class": "userNameContainer__3Ba3D0bepv"}
                    ).find("h1")
                    BUZZFEED_JOIN = BUZZFEED_Soup.find(
                        "dl", attrs={"class": "userMetaList__3R_19D6l1X"}
                    ).find("dd")

                    if not BUZZFEED_NAME:
                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {R}Not Found ❗️{RS} "
                        )
                    else:
                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {BUZZFEED_NAME.getText()}"
                        )

                    if not BUZZFEED_JOIN:
                        print(
                            f"{' ' * 5}└[{Y}•{RS}] {C}User Joined {Y}:{RS} {R}Not Found ❗️{RS} "
                        )
                    else:
                        print(
                            f"{' ' * 5}└[{Y}•{RS}] {C}User Joined {Y}:{RS} {BUZZFEED_JOIN.getText()}"
                        )

                elif BUZZFEED_URL_Request.status_code == 404:
                    print(f"\n[{B} BUZZFEED{RS} ]")
                    print(
                        f"{' ' * 5}└[{R}•{RS}] {C}User Info{Y}:{RS} {R}Sorry, we couldn't find that one ❗️{RS}"
                    )
            else:
                print(f"\n[{B} BUZZFEED{RS} ]")

                print(
                    f"{' ' * 5}└[{R}•{RS}] {C}Connection Lost{Y}:{RS} {R}Oops! Unable To Establish A Connection{RS}"
                )
        except requests.exceptions.Timeout:
            print(f"\n[{B} BUZZFEED{RS} ]")

            print(
                f"{' ' * 5}└[{R}•{RS}] {C}Timeout Error{Y}:{RS} {R}Oops! Timed Out{RS}"
            )
    except socket.gaierror:
        print(f"\n[{B} BUZZFEED{RS} ]")

        print(
            f"{' ' * 5}└[{R}•{RS}] {C}DNS LookUp{Y}:{RS} {R}Oops! The {G}Dns Lookup{R} Failed And The Requested Domain Could Not Be Found.{RS}"
        )

    # [ CNET ]

    try:
        ip_address = socket.gethostbyname("cnet.com")
        # print('IP address:', ip_address)
        try:
            response = requests.get("https://www.cnet.com", timeout=5)
            if response.status_code == 200:
                CNET_URL = f"https://www.cnet.com/profiles/{usernames}/"

                headers = {
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.33",
                }

                CNET_URL_Request = requests.request("GET", CNET_URL, headers=headers)

                if CNET_URL_Request.status_code == 200:
                    print(f"\n[{B} CNET{RS} ]")
                    print(f"{' ' * 5}└[{R}•{RS}] {C}User Url{Y}:{RS} {CNET_URL}")

                    CNET_Soup = BeautifulSoup(CNET_URL_Request.text, "html.parser")

                    CNET_NAME = (
                        CNET_Soup.find("div", attrs={"id": "profile-info"})
                        .find("h1")
                        .find("span", attrs={"itemprop": "name"})
                    )
                    CNET_LOCATION = (
                        CNET_Soup.find("div", attrs={"id": "profile-info"})
                        .find("div", attrs={"class": "col-5"})
                        .find("span", attrs={"itemprop": "locality"})
                    )
                    CNET_PROFILE_PHOTO = CNET_Soup.find(
                        "div", attrs={"class": "headshot big"}
                    )

                    if not CNET_NAME:
                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {R}Not Found ❗️{RS} "
                        )
                    else:
                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {CNET_NAME.getText()}"
                        )

                    if not CNET_LOCATION:
                        print(
                            f"{' ' * 5}└[{Y}•{RS}] {C}User Location {Y}:{RS} {R}Not Found ❗️{RS} "
                        )
                    else:
                        print(
                            f"{' ' * 5}└[{Y}•{RS}] {C}User Location {Y}:{RS} {CNET_LOCATION.getText()}"
                        )

                    if not CNET_PROFILE_PHOTO:
                        print(
                            f"{' ' * 5}└[{G}•{RS}] {C}User Profile Photo {Y}:{RS} {R}Not Found ❗️{RS} "
                        )
                    else:
                        CNET_PHOTO = CNET_PROFILE_PHOTO.find(
                            "figure", attrs={"class": "img"}
                        ).findAll("img")

                        CNETS_PHOTO = CNET_PHOTO[0]

                        print(
                            f"{' ' * 5}└[{G}•{RS}] {C}User Profile Photo {Y}:{RS} {CNETS_PHOTO.attrs['src']}"
                        )

                elif CNET_URL_Request.status_code == 404:
                    print(f"\n[{B} CNET{RS} ]")
                    print(
                        f"{' ' * 5}└[{R}•{RS}] {C}User Info{Y}:{RS} {R}Sorry, we couldn't find that one ❗️{RS}"
                    )
            else:
                print(f"\n[{B} CNET{RS} ]")

                print(
                    f"{' ' * 5}└[{R}•{RS}] {C}Connection Lost{Y}:{RS} {R}Oops! Unable To Establish A Connection{RS}"
                )
        except requests.exceptions.Timeout:
            print(f"\n[{B} CNET{RS} ]")

            print(
                f"{' ' * 5}└[{R}•{RS}] {C}Timeout Error{Y}:{RS} {R}Oops! Timed Out{RS}"
            )
    except socket.gaierror:
        print(f"\n[{B} CNET{RS} ]")

        print(
            f"{' ' * 5}└[{R}•{RS}] {C}DNS LookUp{Y}:{RS} {R}Oops! The {G}Dns Lookup{R} Failed And The Requested Domain Could Not Be Found.{RS}"
        )

    # [ COROFLOT ]

    try:
        ip_address = socket.gethostbyname("coroflot.com")
        # print('IP address:', ip_address)
        try:
            response = requests.get("https://www.coroflot.com", timeout=5)
            if response.status_code == 200:
                COROFLOT_URL = f"https://www.coroflot.com/{usernames}/profile"

                headers = {
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.33",
                }

                COROFLOT_URL_Request = requests.request(
                    "GET", COROFLOT_URL, headers=headers
                )

                if COROFLOT_URL_Request.status_code == 200:

                    print(f"\n[{B} COROFLOT{RS} ]")

                    print(f"{' ' * 5}└[{R}•{RS}] {C}User Url {Y}:{RS} {COROFLOT_URL}")

                    COROFLOT_Soup = BeautifulSoup(
                        COROFLOT_URL_Request.text, "html.parser"
                    )

                    COROFLOT_NAME = COROFLOT_Soup.find(
                        "div", attrs={"class": "right_side"}
                    ).find("h1", attrs={"class": "name_full"})
                    COROFLOT_LOCATION = COROFLOT_Soup.find(
                        "div", attrs={"class": "right_side"}
                    ).find("div", attrs={"class": "location"})
                    COROFLOT_JOIN = COROFLOT_Soup.find(
                        "div", attrs={"class": "member_since_block"}
                    )

                    if not COROFLOT_NAME:
                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {R}Not Found ❗️{RS} "
                        )
                    else:
                        SPACE_REMOVE = COROFLOT_NAME.get_text()
                        SPACE_REMOVE_RESULT = SPACE_REMOVE.strip()
                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {SPACE_REMOVE_RESULT}"
                        )

                    if not COROFLOT_LOCATION:
                        print(
                            f"{' ' * 5}└[{Y}•{RS}] {C}User Location {Y}:{RS} {R}Not Found ❗️{RS} "
                        )
                    else:
                        print(
                            f"{' ' * 5}└[{Y}•{RS}] {C}User Location {Y}:{RS} {COROFLOT_LOCATION.getText()}"
                        )

                    if not COROFLOT_JOIN:
                        print(
                            f"{' ' * 5}└[{G}•{RS}] {C}User Joined {Y}:{RS} {R}Not Found ❗️{RS} "
                        )
                    else:
                        SPACE_REMOVE = COROFLOT_JOIN.get_text()
                        SPACE_REMOVE_RESULT = SPACE_REMOVE.strip()
                        print(
                            f"{' ' * 5}└[{G}•{RS}] {C}User Joined {Y}:{RS} {SPACE_REMOVE_RESULT}"
                        )

                elif COROFLOT_URL_Request.status_code == 404:
                    print(f"\n[{B} COROFLOT{RS} ]")
                    print(
                        f"{' ' * 5}└[{R}•{RS}] {C}User Info{Y}:{RS} {R}Sorry, we couldn't find that one ❗️{RS}"
                    )
            else:
                print(f"\n[{B} COROFLOT{RS} ]")

                print(
                    f"{' ' * 5}└[{R}•{RS}] {C}Connection Lost{Y}:{RS} {R}Oops! Unable To Establish A Connection{RS}"
                )
        except requests.exceptions.Timeout:
            print(f"\n[{B} COROFLOT{RS} ]")

            print(
                f"{' ' * 5}└[{R}•{RS}] {C}Timeout Error{Y}:{RS} {R}Oops! Timed Out{RS}"
            )
    except socket.gaierror:
        print(f"\n[{B} COROFLOT{RS} ]")

        print(
            f"{' ' * 5}└[{R}•{RS}] {C}DNS LookUp{Y}:{RS} {R}Oops! The {G}Dns Lookup{R} Failed And The Requested Domain Could Not Be Found.{RS}"
        )

    # [ DRIBBBLE ]

    try:
        ip_address = socket.gethostbyname("dribbble.com")
        # print('IP address:', ip_address)
        try:
            response = requests.get("https://dribbble.com", timeout=5)
            if response.status_code == 200:
                DRIBBBLE_Url = f"https://dribbble.com/{usernames}/about"

                DRIBBBLE_Request = requests.get(DRIBBBLE_Url)

                if DRIBBBLE_Request.status_code == 200:

                    print(f"\n[{B} DRIBBBLE{RS} ]")

                    print(f"{' ' * 5}└[{R}•{RS}] {C}User Url{Y}:{RS} {DRIBBBLE_Url}")

                    DRIBBBLE_Soup = BeautifulSoup(DRIBBBLE_Request.text, "html.parser")

                    DRIBBBLE_NAME = DRIBBBLE_Soup.find(
                        "div", attrs={"class": "masthead-content"}
                    ).find("h1", attrs={"class": "masthead-profile-name"})

                    DRIBBBLE_ADDRESS = DRIBBBLE_Soup.find(
                        "div", attrs={"class": "masthead-content"}
                    ).find("p", attrs={"class": "masthead-profile-locality"})

                    DRIBBBLE_JOIN = DRIBBBLE_Soup.find(
                        "div", attrs={"class": "about-content-main"}
                    ).find("p", attrs={"class": "info-item created"})

                    DRIBBBLE_BIO = DRIBBBLE_Soup.find(
                        "div", attrs={"class": "about-content-main"}
                    ).find("p", attrs={"class": "empty-bio"})

                    DRIBBBLE_PROFILE_PHOTO = DRIBBBLE_Soup.find(
                        "div", attrs={"class": "masthead-avatar"}
                    )

                    if not DRIBBBLE_NAME:
                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {R}Not Found ❗️{RS} "
                        )
                    else:
                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {DRIBBBLE_NAME.string}"
                        )

                    if not DRIBBBLE_ADDRESS:
                        print(
                            f"{' ' * 5}└[{Y}•{RS}] {C}User Location {Y}:{RS} {R}Not Found ❗️{RS} "
                        )
                    else:
                        print(
                            f"{' ' * 5}└[{Y}•{RS}] {C}User Location {Y}:{RS} {DRIBBBLE_ADDRESS.string}"
                        )

                    if not DRIBBBLE_JOIN:
                        print(
                            f"{' ' * 5}└[{G}•{RS}] {C}User Joined Date {Y}:{RS} {R}Not Found ❗️{RS} "
                        )
                    else:
                        DRIBBBLE_JOINED = DRIBBBLE_JOIN.find("span").string.replace(
                            "Member since ", " "
                        )
                        print(
                            f"{' ' * 5}└[{G}•{RS}] {C}User Joined Date {Y}:{RS} {DRIBBBLE_JOINED}"
                        )

                    if not DRIBBBLE_PROFILE_PHOTO:
                        print(
                            f"{' ' * 5}└[{P}•{RS}] {C}User Profile Photo {Y}:{RS} {R}Not Found ❗️{RS} "
                        )
                    else:
                        print(
                            f"{' ' * 5}└[{P}•{RS}] {C}User Profile Photo {Y}:{RS} {DRIBBBLE_PROFILE_PHOTO.find_all('img')[0].attrs['src']}"
                        )

                    if not DRIBBBLE_BIO:
                        print(
                            f"{' ' * 5}└[{R}•{RS}] {C}User Biography {Y}:{RS} {R}Not Found ❗️{RS} "
                        )
                    else:
                        print(
                            f"{' ' * 5}└[{R}•{RS}] {C}User Biography {Y}:{RS} {DRIBBBLE_BIO.string}"
                        )

                        UserMention_Bio = DRIBBBLE_BIO.string

                        Mention_Bio = re.findall(r"@[A-Za-z0-9.-]+", UserMention_Bio)

                        print(
                            f"{' ' * 5}└[{R}•{RS}] {C}List Of People Mention On USER Bio{Y}:{RS}"
                        )

                        if not Mention_Bio:
                            print(
                                f"{' ' * 10}└[{R}•{RS}] {Y}Mention Pople {C}On Bio {Y}:{RS} {R}Not Found ❗️{RS} \n"
                            )
                        else:
                            count = 0
                            for Mention_Bios in Mention_Bio:
                                count += 1
                                print(
                                    f"{' ' * 20}└[{R}{count}{RS}] {G}►{RS} {Mention_Bios}"
                                )

                        UserEmail = DRIBBBLE_BIO.string

                        emails = re.findall(r"[\w\.-]+@[\w\.-]+", UserEmail)

                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}List Of Email Write On USER Bio{Y}:{RS}"
                        )

                        if not emails:
                            print(
                                f"{' ' * 10}└[{R}•{RS}] {C}Find {Y}Email {C}On Bio {Y}:{RS} {R}Not Found ❗️{RS} \n"
                            )
                        else:
                            count = 0
                        for email in emails:
                            count += 1
                            print(f"{' ' * 20}└[{R}{count}{RS}] {G}►{RS} {email}")

                        print(
                            f"{' ' * 5}└[{Y}•{RS}] {C}List Of PhoneNumber Or Any Digit On USER Bio{Y}:{RS}"
                        )

                        PhoneNumberbio = DRIBBBLE_BIO.string

                        PhoneNumbers = re.findall(r"\d+", PhoneNumberbio)

                        if not PhoneNumbers:
                            print(
                                f"{' ' * 10}└[{R}•{RS}] {C}Find {Y}PhoneNumber {C}On Bio {Y}:{RS} {R}Not Found ❗️{RS} "
                            )
                        else:
                            count = 0
                        for PhoneNumber in PhoneNumbers:
                            count += 1
                            print(f"{' ' * 20}└[{R}{count}{RS}] {G}►{RS} {PhoneNumber}")

                elif DRIBBBLE_Request.status_code == 404:
                    print(f"\n[{B} DRIBBBLE{RS} ]")
                    print(
                        f"{' ' * 5}└[{R}•{RS}] {C}User Info{Y}:{RS} {R}Sorry, we couldn't find that one ❗️{RS}"
                    )
            else:
                print(f"\n[{B} DRIBBBLE{RS} ]")

                print(
                    f"{' ' * 5}└[{R}•{RS}] {C}Connection Lost{Y}:{RS} {R}Oops! Unable To Establish A Connection{RS}"
                )
        except requests.exceptions.Timeout:
            print(f"\n[{B} DRIBBBLE{RS} ]")

            print(
                f"{' ' * 5}└[{R}•{RS}] {C}Timeout Error{Y}:{RS} {R}Oops! Timed Out{RS}"
            )
    except socket.gaierror:
        print(f"\n[{B} DRIBBBLE{RS} ]")

        print(
            f"{' ' * 5}└[{R}•{RS}] {C}DNS LookUp{Y}:{RS} {R}Oops! The {G}Dns Lookup{R} Failed And The Requested Domain Could Not Be Found.{RS}"
        )

    # [ COMMUNITY CRYPTOMATOR ]

    try:
        ip_address = socket.gethostbyname("community.cryptomator.org")
        # print('IP address:', ip_address)
        try:
            response = requests.get("https://community.cryptomator.org", timeout=5)
            if response.status_code == 200:
                COMMUNITY_CRYPTOMATOR_Url = (
                    f"https://community.cryptomator.org/u/{usernames}/summary"
                )

                COMMUNITY_CRYPTOMATOR_Request = requests.get(COMMUNITY_CRYPTOMATOR_Url)

                if COMMUNITY_CRYPTOMATOR_Request.status_code == 200:

                    print(f"\n[{B} COMMUNITY CRYPTOMATOR{RS} ]")

                    print(
                        f"{' ' * 5}└[{R}•{RS}] {C}User Url{Y}:{RS} {COMMUNITY_CRYPTOMATOR_Url}"
                    )

                    COMMUNITY_CRYPTOMATOR_Soup = BeautifulSoup(
                        COMMUNITY_CRYPTOMATOR_Request.text, "html.parser"
                    )

                    COMMUNITY_CRYPTOMATOR_NAME = COMMUNITY_CRYPTOMATOR_Soup.find(
                        "div", attrs={"class": "user-crawler"}
                    )

                    COMMUNITY_CRYPTOMATOR_DESCRIPTION = COMMUNITY_CRYPTOMATOR_Soup.find(
                        "meta", property="og:description"
                    )

                    COMMUNITY_CRYPTOMATOR_PHOTO = COMMUNITY_CRYPTOMATOR_Soup.find(
                        "meta", property="og:image"
                    )

                    if not COMMUNITY_CRYPTOMATOR_NAME:
                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {R}Not Found ❗️{RS} "
                        )
                    else:
                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {COMMUNITY_CRYPTOMATOR_NAME.find('h2', attrs={'class': 'username'}).getText()}"
                        )

                    if not COMMUNITY_CRYPTOMATOR_DESCRIPTION:
                        print(
                            f"{' ' * 5}└[{Y}•{RS}] {C}User Description {Y}:{RS} {R}Not Found ❗️{RS} "
                        )
                    else:
                        print(
                            f"{' ' * 5}└[{Y}•{RS}] {C}User Description {Y}:{RS} {COMMUNITY_CRYPTOMATOR_DESCRIPTION['content']}"
                        )

                        UserMention_Bio = COMMUNITY_CRYPTOMATOR_DESCRIPTION["content"]

                        Mention_Bio = re.findall(r"@[A-Za-z0-9.-]+", UserMention_Bio)

                        print(
                            f"{' ' * 5}└[{G}•{RS}] {C}List Of People Mention On USER Bio{Y}:{RS}"
                        )

                        if not Mention_Bio:
                            print(
                                f"{' ' * 20}└[{R}•{RS}] {Y}Mention Pople {C}On Bio {Y}:{RS} {R}Not Found ❗️{RS} \n"
                            )
                        else:
                            count = 0
                            for Mention_Bios in Mention_Bio:
                                count += 1
                                print(
                                    f"{' ' * 20}└[{R}{count}{RS}] {G}►{RS} {Mention_Bios}"
                                )

                        UserEmail = COMMUNITY_CRYPTOMATOR_DESCRIPTION["content"]

                        emails = re.findall(r"[\w\.-]+@[\w\.-]+", UserEmail)

                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}List Of Email Write On USER Bio{Y}:{RS}"
                        )

                        if not emails:
                            print(
                                f"{' ' * 20}└[{R}•{RS}] {C}Find {Y}Email {C}On Bio {Y}:{RS} {R}Not Found ❗️{RS} \n"
                            )
                        else:
                            count = 0
                        for email in emails:
                            count += 1
                            print(f"{' ' * 20}└[{R}{count}{RS}] {G}►{RS} {email}")

                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}List Of PhoneNumber Or Any Digit On USER Bio{Y}:{RS}"
                        )

                        PhoneNumberbio = COMMUNITY_CRYPTOMATOR_DESCRIPTION["content"]

                        PhoneNumbers = re.findall(r"\d+", PhoneNumberbio)

                        if not PhoneNumbers:
                            print(
                                f"{' ' * 20}└[{R}•{RS}] {C}Find {Y}PhoneNumber {C}On Bio {Y}:{RS} {R}Not Found ❗️{RS} "
                            )
                        else:
                            count = 0
                        for PhoneNumber in PhoneNumbers:
                            count += 1
                            print(f"{' ' * 20}└[{R}{count}{RS}] {G}►{RS} {PhoneNumber}")

                    if not COMMUNITY_CRYPTOMATOR_PHOTO:
                        print(
                            f"\n{' ' * 5}└[{G}•{RS}] {C}User Profile Photo {Y}:{RS} {R}Not Found ❗️{RS} "
                        )
                    else:
                        print(
                            f"\n{' ' * 5}└[{G}•{RS}] {C}User Profile Photo {Y}:{RS} {COMMUNITY_CRYPTOMATOR_PHOTO['content']}"
                        )

                elif COMMUNITY_CRYPTOMATOR_Request.status_code == 404:
                    print(f"\n[{B} COMMUNITY CRYPTOMATOR{RS} ]")
                    print(
                        f"{' ' * 5}└[{R}•{RS}] {C}User Info{Y}:{RS} {R}Sorry, we couldn't find that one ❗️{RS}"
                    )

            else:
                print(f"\n[{B} COMMUNITY CRYPTOMATOR{RS} ]")

                print(
                    f"{' ' * 5}└[{R}•{RS}] {C}Connection Lost{Y}:{RS} {R}Oops! Unable To Establish A Connection{RS}"
                )
        except requests.exceptions.Timeout:
            print(f"\n[{B} COMMUNITY CRYPTOMATOR{RS} ]")

            print(
                f"{' ' * 5}└[{R}•{RS}] {C}Timeout Error{Y}:{RS} {R}Oops! Timed Out{RS}"
            )
    except socket.gaierror:
        print(f"\n[{B} COMMUNITY CRYPTOMATOR{RS} ]")

        print(
            f"{' ' * 5}└[{R}•{RS}] {C}DNS LookUp{Y}:{RS} {R}Oops! The {G}Dns Lookup{R} Failed And The Requested Domain Could Not Be Found.{RS}"
        )

    # [ DEV.TO ]

    try:
        ip_address = socket.gethostbyname("dev.to")
        # print('IP address:', ip_address)
        try:
            response = requests.get("https://dev.to", timeout=5)
            if response.status_code == 200:
                DEV_TO_Url = f"https://dev.to/{usernames}"

                DEV_TO_Request = requests.get(DEV_TO_Url)

                if DEV_TO_Request.status_code == 200:

                    print(f"\n[{B} DEV.TO{RS} ]")

                    print(f"{' ' * 5}└[{R}•{RS}] {C}User Url{Y}:{RS} {DEV_TO_Url}")

                    DEV_TO_Soup = BeautifulSoup(DEV_TO_Request.text, "html.parser")

                    DEV_TO_NAME = DEV_TO_Soup.find(
                        "div", attrs={"class": "profile-header__details"}
                    )

                    DEV_TO_BIO = DEV_TO_Soup.find("meta", property="og:description")

                    DEV_TO_WEBSITE = (
                        DEV_TO_Soup.find("div", attrs={"class": "profile-header__meta"})
                        .find("a")
                        .find("span")
                    )

                    if not DEV_TO_NAME:
                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {R}Not Found ❗️{RS} "
                        )
                    else:
                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {DEV_TO_NAME.find('h1', attrs={'class': 'crayons-title fw-heavy mb-2'}).getText()}"
                        )

                    if not DEV_TO_BIO:
                        print(
                            f"{' ' * 5}└[{Y}•{RS}] {C}User Bio {Y}:{RS} {R}Not Found ❗️{RS} "
                        )
                    else:
                        print(
                            f"{' ' * 5}└[{Y}•{RS}] {C}User Bio {Y}:{RS} {DEV_TO_BIO['content']}"
                        )

                        UserMention_Bio = DEV_TO_BIO["content"]

                        Mention_Bio = re.findall(r"@[A-Za-z0-9.-]+", UserMention_Bio)

                        print(
                            f"{' ' * 5}└[{G}•{RS}] {C}List Of People Mention On USER Bio{Y}:{RS}"
                        )

                        if not Mention_Bio:
                            print(
                                f"{' ' * 20}└[{R}•{RS}] {Y}Mention Pople {C}On Bio {Y}:{RS} {R}Not Found ❗️{RS} \n"
                            )
                        else:
                            count = 0
                            for Mention_Bios in Mention_Bio:
                                count += 1
                                print(
                                    f"{' ' * 20}└[{R}{count}{RS}] {G}►{RS} {Mention_Bios}"
                                )

                        UserEmail = DEV_TO_BIO["content"]

                        emails = re.findall(r"[\w\.-]+@[\w\.-]+", UserEmail)

                        print(
                            f"{' ' * 5}└[{R}•{RS}] {C}List Of Email Write On USER Bio{Y}:{RS}"
                        )

                        if not emails:
                            print(
                                f"{' ' * 20}└[{R}•{RS}] {C}Find {Y}Email {C}On Bio {Y}:{RS} {R}Not Found ❗️{RS} \n"
                            )
                        else:
                            count = 0
                        for email in emails:
                            count += 1
                            print(f"{' ' * 20}└[{R}{count}{RS}] {G}►{RS} {email}")

                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}List Of PhoneNumber Or Any Digit On USER Bio{Y}:{RS}"
                        )

                        PhoneNumberbio = DEV_TO_BIO["content"]

                        PhoneNumbers = re.findall(r"\d+", PhoneNumberbio)

                        if not PhoneNumbers:
                            print(
                                f"{' ' * 20}└[{R}•{RS}] {C}Find {Y}PhoneNumber {C}On Bio {Y}:{RS} {R}Not Found ❗️{RS} "
                            )
                        else:
                            count = 0
                        for PhoneNumber in PhoneNumbers:
                            count += 1
                            print(f"{' ' * 20}└[{R}{count}{RS}] {G}►{RS} {PhoneNumber}")

                    if not DEV_TO_WEBSITE:
                        print(
                            f"{' ' * 5}└[{G}•{RS}] {C}User Website {Y}:{RS} {R}Not Found ❗️{RS} "
                        )
                    else:
                        space_remove = DEV_TO_WEBSITE.getText()
                        After_remove_space = space_remove.strip()
                        print(
                            f"{' ' * 5}└[{G}•{RS}] {C}User Website {Y}:{RS} {After_remove_space}"
                        )

                elif DEV_TO_Request.status_code == 404:
                    print(f"\n[{B} DEV.TO{RS} ]")
                    print(
                        f"{' ' * 5}└[{R}•{RS}] {C}User Info{Y}:{RS} {R}Sorry, we couldn't find that one ❗️{RS}"
                    )

            else:
                print(f"\n[{B} DEV.TO{RS} ]")

                print(
                    f"{' ' * 5}└[{R}•{RS}] {C}Connection Lost{Y}:{RS} {R}Oops! Unable To Establish A Connection{RS}"
                )
        except requests.exceptions.Timeout:
            print(f"\n[{B} DEV.TO{RS} ]")

            print(
                f"{' ' * 5}└[{R}•{RS}] {C}Timeout Error{Y}:{RS} {R}Oops! Timed Out{RS}"
            )
    except socket.gaierror:
        print(f"\n[{B} DEV.TO{RS} ]")

        print(
            f"{' ' * 5}└[{R}•{RS}] {C}DNS LookUp{Y}:{RS} {R}Oops! The {G}Dns Lookup{R} Failed And The Requested Domain Could Not Be Found.{RS}"
        )

    # [ DEVIANTART ]

    try:
        ip_address = socket.gethostbyname("deviantart.com")
        # print('IP address:', ip_address)
        try:
            response = requests.get("https://www.deviantart.com", timeout=5)
            if response.status_code == 200:
                DEVIANTART_Url = f"https://www.deviantart.com/{usernames}"

                DEVIANTART_Request = requests.get(DEVIANTART_Url)

                if DEVIANTART_Request.status_code == 200:

                    print(f"\n[{B} DEVIANTART{RS} ]")

                    print(f"{' ' * 5}└[{R}•{RS}] {C}User Url{Y}:{RS} {DEVIANTART_Url}")

                    DEVIANTART_Soup = BeautifulSoup(
                        DEVIANTART_Request.text, "html.parser"
                    )

                    DEVIANTART_NAME = (
                        DEVIANTART_Soup.find("div", attrs={"class": "_2Ofv6"})
                        .find("div", attrs={"class": "_3oLE7"})
                        .find("span", attrs={"class": "_2UI2c"})
                    )

                    DEVIANTART_BIO = DEVIANTART_Soup.find(
                        "div", attrs={"class": "_2Ofv6"}
                    ).find("div", attrs={"class": "_33syq"})

                    if not DEVIANTART_NAME:
                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {R}Not Found ❗️{RS} "
                        )
                    else:
                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {DEVIANTART_NAME.string}"
                        )

                    if not DEVIANTART_BIO:
                        print(
                            f"{' ' * 5}└[{Y}•{RS}] {C}User Bio {Y}:{RS} {R}Not Found ❗️{RS} "
                        )
                    else:
                        print(
                            f"{' ' * 5}└[{Y}•{RS}] {C}User Bio {Y}:{RS} {DEVIANTART_BIO.string}"
                        )

                        UserMention_Bio = DEVIANTART_BIO.string

                        Mention_Bio = re.findall(r"@[A-Za-z0-9.-]+", UserMention_Bio)

                        print(
                            f"{' ' * 5}└[{G}•{RS}] {C}List Of People Mention On USER Bio{Y}:{RS}"
                        )

                        if not Mention_Bio:
                            print(
                                f"{' ' * 20}└[{R}•{RS}] {Y}Mention Pople {C}On Bio {Y}:{RS} {R}Not Found ❗️{RS} \n"
                            )
                        else:
                            count = 0
                            for Mention_Bios in Mention_Bio:
                                count += 1
                                print(
                                    f"{' ' * 20}└[{R}{count}{RS}] {G}►{RS} {Mention_Bios}"
                                )

                        UserEmail = DEVIANTART_BIO.string

                        emails = re.findall(r"[\w\.-]+@[\w\.-]+", UserEmail)

                        print(
                            f"{' ' * 5}└[{R}•{RS}] {C}List Of Email Write On USER Bio{Y}:{RS}"
                        )

                        if not emails:
                            print(
                                f"{' ' * 20}└[{R}•{RS}] {C}Find {Y}Email {C}On Bio {Y}:{RS} {R}Not Found ❗️{RS} \n"
                            )
                        else:
                            count = 0
                        for email in emails:
                            count += 1
                            print(f"{' ' * 20}└[{R}{count}{RS}] {G}►{RS} {email}")

                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}List Of PhoneNumber Or Any Digit On USER Bio{Y}:{RS}"
                        )

                        PhoneNumberbio = DEVIANTART_BIO.string

                        PhoneNumbers = re.findall(r"\d+", PhoneNumberbio)

                        if not PhoneNumbers:
                            print(
                                f"{' ' * 20}└[{R}•{RS}] {C}Find {Y}PhoneNumber {C}On Bio {Y}:{RS} {R}Not Found ❗️{RS} "
                            )
                        else:
                            count = 0
                        for PhoneNumber in PhoneNumbers:
                            count += 1
                            print(f"{' ' * 20}└[{R}{count}{RS}] {G}►{RS} {PhoneNumber}")

                elif DEVIANTART_Request.status_code == 404:
                    print(f"\n[{B} DEVIANTART{RS} ]")
                    print(
                        f"{' ' * 5}└[{R}•{RS}] {C}User Info{Y}:{RS} {R}Sorry, we couldn't find that one ❗️{RS}"
                    )
            else:
                print(f"\n[{B} DEVIANTART{RS} ]")

                print(
                    f"{' ' * 5}└[{R}•{RS}] {C}Connection Lost{Y}:{RS} {R}Oops! Unable To Establish A Connection{RS}"
                )
        except requests.exceptions.Timeout:
            print(f"\n[{B} DEVIANTART{RS} ]")

            print(
                f"{' ' * 5}└[{R}•{RS}] {C}Timeout Error{Y}:{RS} {R}Oops! Timed Out{RS}"
            )
    except socket.gaierror:
        print(f"\n[{B} DEVIANTART{RS} ]")

        print(
            f"{' ' * 5}└[{R}•{RS}] {C}DNS LookUp{Y}:{RS} {R}Oops! The {G}Dns Lookup{R} Failed And The Requested Domain Could Not Be Found.{RS}"
        )

    # [ EGPU ]

    try:
        ip_address = socket.gethostbyname("egpu.io")
        # print('IP address:', ip_address)
        try:
            response = requests.get("http://egpu.io", timeout=5)
            if response.status_code == 200:
                EGPU_Url = f"http://egpu.io/forums/profile/{usernames}/"

                EGPU_Request = requests.get(EGPU_Url)

                if EGPU_Request.status_code == 200:

                    print(f"\n[{B} EGPU{RS} ]")

                    print(f"{' ' * 5}└[{R}•{RS}] {C}User Url{Y}:{RS} {EGPU_Url}")

                    EGPU_Soup = BeautifulSoup(EGPU_Request.text, "html.parser")

                    EGPU_NAME = EGPU_Soup.find(
                        "div", attrs={"class": "wpf-breadcrumb"}
                    ).find("div", attrs={"class": "wpf-item-element active"})

                    if not EGPU_NAME:
                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {R}Not Found ❗️{RS} "
                        )
                    else:
                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {EGPU_NAME.string}"
                        )

                elif EGPU_Request.status_code == 404:
                    print(f"\n[{B} EGPU{RS} ]")
                    print(
                        f"{' ' * 5}└[{R}•{RS}] {C}User Info{Y}:{RS} {R}Sorry, we couldn't find that one ❗️{RS}"
                    )
            else:
                print(f"\n[{B} EGPU{RS} ]")

                print(
                    f"{' ' * 5}└[{R}•{RS}] {C}Connection Lost{Y}:{RS} {R}Oops! Unable To Establish A Connection{RS}"
                )
        except requests.exceptions.Timeout:
            print(f"\n[{B} EGPU{RS} ]")

            print(
                f"{' ' * 5}└[{R}•{RS}] {C}Timeout Error{Y}:{RS} {R}Oops! Timed Out{RS}"
            )
    except socket.gaierror:
        print(f"\n[{B} EGPU{RS} ]")

        print(
            f"{' ' * 5}└[{R}•{RS}] {C}DNS LookUp{Y}:{RS} {R}Oops! The {G}Dns Lookup{R} Failed And The Requested Domain Could Not Be Found.{RS}"
        )

    # [ COMMUNITY EINTRACHT ]

    try:
        ip_address = socket.gethostbyname("community.eintracht.de")
        # print('IP address:', ip_address)
        try:
            response = requests.get("https://community.eintracht.de", timeout=5)
            if response.status_code == 200:
                COMMUNITY_EINTRACHT_Url = (
                    f"https://community.eintracht.de/fans/{usernames}"
                )

                COMMUNITY_EINTRACHT_Request = requests.get(COMMUNITY_EINTRACHT_Url)

                if COMMUNITY_EINTRACHT_Request.status_code == 200:

                    print(f"\n[{B} COMMUNITY EINTRACHT{RS} ]")

                    print(
                        f"{' ' * 5}└[{R}•{RS}] {C}User Url{Y}:{RS} {COMMUNITY_EINTRACHT_Url}"
                    )

                    COMMUNITY_EINTRACHT_Soup = BeautifulSoup(
                        COMMUNITY_EINTRACHT_Request.text, "html.parser"
                    )

                    COMMUNITY_EINTRACHT_NAME = COMMUNITY_EINTRACHT_Soup.find(
                        "div", attrs={"class": "page-header"}
                    )

                    if not COMMUNITY_EINTRACHT_NAME:
                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {R}Not Found ❗️{RS} "
                        )
                    else:
                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {COMMUNITY_EINTRACHT_NAME.string}"
                        )

                elif COMMUNITY_EINTRACHT_Request.status_code == 404:
                    print(f"\n[{B} COMMUNITY EINTRACHT{RS} ]")
                    print(
                        f"{' ' * 5}└[{R}•{RS}] {C}User Info{Y}:{RS} {R}Sorry, we couldn't find that one ❗️{RS}"
                    )

            else:
                print(f"\n[{B} COMMUNITY EINTRACHT{RS} ]")

                print(
                    f"{' ' * 5}└[{R}•{RS}] {C}Connection Lost{Y}:{RS} {R}Oops! Unable To Establish A Connection{RS}"
                )
        except requests.exceptions.Timeout:
            print(f"\n[{B} COMMUNITY EINTRACHT{RS} ]")

            print(
                f"{' ' * 5}└[{R}•{RS}] {C}Timeout Error{Y}:{RS} {R}Oops! Timed Out{RS}"
            )
    except socket.gaierror:
        print(f"\n[{B} COMMUNITY EINTRACHT{RS} ]")

        print(
            f"{' ' * 5}└[{R}•{RS}] {C}DNS LookUp{Y}:{RS} {R}Oops! The {G}Dns Lookup{R} Failed And The Requested Domain Could Not Be Found.{RS}"
        )

    # [ HACKSTER.IO ]

    try:
        ip_address = socket.gethostbyname("hackster.io")
        # print('IP address:', ip_address)
        try:
            response = requests.get("https://www.hackster.io", timeout=5)
            if response.status_code == 200:
                HACKSTER_IO_Url = f"https://www.hackster.io/{usernames}"

                HACKSTER_IO_Request = requests.get(HACKSTER_IO_Url)

                if HACKSTER_IO_Request.status_code == 200:

                    print(f"\n[{B} HACKSTER IO{RS} ]")

                    print(f"{' ' * 5}└[{R}•{RS}] {C}User Url{Y}:{RS} {HACKSTER_IO_Url}")

                    HACKSTER_IO_Soup = BeautifulSoup(
                        HACKSTER_IO_Request.text, "html.parser"
                    )

                    HACKSTER_IO_NAME = HACKSTER_IO_Soup.find(
                        "div", attrs={"class": "user_card__userInfo__wid7E"}
                    )

                    if not HACKSTER_IO_NAME:
                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {R}Not Found ❗️{RS} "
                        )
                    else:
                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {HACKSTER_IO_NAME.find('h1', attrs={'class': 'user_card__name__1QI2z'}).string}"
                        )

                elif HACKSTER_IO_Request.status_code == 404:
                    print(f"\n[{B} HACKSTER IO{RS} ]")
                    print(
                        f"{' ' * 5}└[{R}•{RS}] {C}User Info{Y}:{RS} {R}Sorry, we couldn't find that one ❗️{RS}"
                    )

            else:
                print(f"\n[{B} HACKSTER IO{RS} ]")

                print(
                    f"{' ' * 5}└[{R}•{RS}] {C}Connection Lost{Y}:{RS} {R}Oops! Unable To Establish A Connection{RS}"
                )
        except requests.exceptions.Timeout:
            print(f"\n[{B} HACKSTER IO{RS} ]")

            print(
                f"{' ' * 5}└[{R}•{RS}] {C}Timeout Error{Y}:{RS} {R}Oops! Timed Out{RS}"
            )
    except socket.gaierror:
        print(f"\n[{B} HACKSTER IO{RS} ]")

        print(
            f"{' ' * 5}└[{R}•{RS}] {C}DNS LookUp{Y}:{RS} {R}Oops! The {G}Dns Lookup{R} Failed And The Requested Domain Could Not Be Found.{RS}"
        )

    # [ SATSIS_INFO ]

    try:
        ip_address = socket.gethostbyname("satsis.info")
        # print('IP address:', ip_address)
        try:
            response = requests.get("https://satsis.info", timeout=5)
            if response.status_code == 200:
                SATSIS_INFO_Url = f"https://satsis.info/user/{usernames}"

                SATSIS_INFO_Request = requests.get(SATSIS_INFO_Url)

                if SATSIS_INFO_Request.status_code == 200:

                    print(f"\n[{B} SATSIS INFO{RS} ]")

                    print(f"{' ' * 5}└[{R}•{RS}] {C}User Url{Y}:{RS} {SATSIS_INFO_Url}")

                    SATSIS_INFO_Soup = BeautifulSoup(
                        SATSIS_INFO_Request.text, "html.parser"
                    )

                    SATSIS_INFO_NAME = SATSIS_INFO_Soup.find(
                        "div", attrs={"class": "rcol"}
                    ).find_all("li")[0]

                    REGISTRATION_DATE_NAME = SATSIS_INFO_Soup.find(
                        "div", attrs={"class": "rcol"}
                    ).find_all("li")[2]

                    LAST_VISITED = SATSIS_INFO_Soup.find(
                        "div", attrs={"class": "rcol"}
                    ).find_all("li")[3]

                    if not SATSIS_INFO_NAME:
                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {R}Not Found ❗️{RS} "
                        )
                    else:
                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {SATSIS_INFO_NAME.find_all_next('b')[0].getText()}"
                        )

                    if not REGISTRATION_DATE_NAME:
                        print(
                            f"{' ' * 5}└[{Y}•{RS}] {C}User Registration Date {Y}:{RS} {R}Not Found ❗️{RS} "
                        )
                    else:
                        print(
                            f"{' ' * 5}└[{Y}•{RS}] {C}User Registration Date {Y}:{RS} {REGISTRATION_DATE_NAME.find_all_next('b')[0].getText()}"
                        )

                    if not LAST_VISITED:
                        print(
                            f"{' ' * 5}└[{G}•{RS}] {C}User Last Visited {Y}:{RS} {R}Not Found ❗️{RS} "
                        )
                    else:
                        print(
                            f"{' ' * 5}└[{G}•{RS}] {C}User Last Visited {Y}:{RS} {LAST_VISITED.find_all_next('b')[0].getText()}"
                        )

                elif SATSIS_INFO_Request.status_code == 404:
                    print(f"\n[{B} SATSIS INFO{RS} ]")
                    print(
                        f"{' ' * 5}└[{R}•{RS}] {C}User Info{Y}:{RS} {R}Sorry, we couldn't find that one ❗️{RS}"
                    )
            else:
                print(f"\n[{B} SATSIS INFO{RS} ]")

                print(
                    f"{' ' * 5}└[{R}•{RS}] {C}Connection Lost{Y}:{RS} {R}Oops! Unable To Establish A Connection{RS}"
                )
        except requests.exceptions.Timeout:
            print(f"\n[{B} SATSIS INFO{RS} ]")

            print(
                f"{' ' * 5}└[{R}•{RS}] {C}Timeout Error{Y}:{RS} {R}Oops! Timed Out{RS}"
            )
    except socket.gaierror:
        print(f"\n[{B} SATSIS INFO{RS} ]")

        print(
            f"{' ' * 5}└[{R}•{RS}] {C}DNS LookUp{Y}:{RS} {R}Oops! The {G}Dns Lookup{R} Failed And The Requested Domain Could Not Be Found.{RS}"
        )

    # [ SESSIONIZE ]

    try:
        ip_address = socket.gethostbyname("sessionize.com")
        # print('IP address:', ip_address)
        try:
            response = requests.get("https://sessionize.com", timeout=5)
            if response.status_code == 200:
                SESSIONIZE_Url = f"https://sessionize.com/{usernames}/"

                SESSIONIZE_Request = requests.get(SESSIONIZE_Url)

                if SESSIONIZE_Request.status_code == 200:

                    print(f"\n[{B} SESSIONIZE{RS} ]")

                    print(f"{' ' * 5}└[{R}•{RS}] {C}User Url{Y}:{RS} {SESSIONIZE_Url}")

                    SESSIONIZE_Soup = BeautifulSoup(
                        SESSIONIZE_Request.text, "html.parser"
                    )

                    PROFILE_IS_PRIVATE = SESSIONIZE_Soup.find(
                        "div", attrs={"class": "panel-body"}
                    )

                    SESSIONIZE_NAME = SESSIONIZE_Soup.find(
                        "div",
                        attrs={"class": "c-s-speaker-info c-s-speaker-info--full"},
                    )

                    SESSIONIZE_ADDRESS = SESSIONIZE_Soup.find(
                        "div",
                        attrs={"class": "c-s-speaker-info c-s-speaker-info--full"},
                    )

                    SESSIONIZE_TAGLINE = SESSIONIZE_Soup.find(
                        "div",
                        attrs={"class": "c-s-speaker-info c-s-speaker-info--full"},
                    )

                    SESSIONIZE_PROFILE_PHOTO = SESSIONIZE_Soup.find(
                        "div",
                        attrs={"class": "c-s-speaker-info c-s-speaker-info--full"},
                    )

                    if not PROFILE_IS_PRIVATE:

                        if not SESSIONIZE_NAME:
                            print(
                                f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {R}Not Found ❗️{RS} "
                            )
                        else:
                            print(
                                f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {SESSIONIZE_NAME.find('h1', attrs={'class': 'c-s-speaker-info__name'}).string}"
                            )
                        if not SESSIONIZE_PROFILE_PHOTO:
                            print(
                                f"{' ' * 5}└[{Y}•{RS}] {C}User Profile Photo {Y}:{RS} {R}Not Found ❗️{RS} "
                            )
                        else:
                            print(
                                f"{' ' * 5}└[{Y}•{RS}] {C}User Profile Photo {Y}:{RS} {SESSIONIZE_PROFILE_PHOTO.find('figure', attrs={'class': 'c-s-speaker-info__avatar'}).findAll('img')[0].attrs['src']}"
                            )

                        if not SESSIONIZE_TAGLINE:
                            print(
                                f"{' ' * 5}└[{G}•{RS}] {C}User Profile TagLine {Y}:{RS} {R}Not Found ❗️{RS} "
                            )
                        else:
                            print(
                                f"{' ' * 5}└[{G}•{RS}] {C}User Profile TagLine {Y}:{RS} {SESSIONIZE_TAGLINE.find('p', attrs={'class': 'c-s-speaker-info__tagline'}).string}"
                            )

                        if not SESSIONIZE_ADDRESS:
                            print(
                                f"{' ' * 5}└[{R}•{RS}] {C}User Location {Y}:{RS} {R}Not Found ❗️{RS} "
                            )
                        else:
                            TEXT_TO_SPACE_REMOVE = SESSIONIZE_ADDRESS.find(
                                "p", attrs={"class": "c-s-speaker-info__location"}
                            ).getText()
                            After_remove_seeking_space = TEXT_TO_SPACE_REMOVE.strip()
                            print(
                                f"{' ' * 5}└[{R}•{RS}] {C}User Location {Y}:{RS} {After_remove_seeking_space}"
                            )
                    else:
                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}User Account {Y}:{RS} [ {R}{PROFILE_IS_PRIVATE.find('h3').getText()}{RS} ] {RS}"
                        )

                elif SESSIONIZE_Request.status_code == 404:
                    print(f"\n[{B} SESSIONIZE{RS} ]")
                    print(
                        f"{' ' * 5}└[{R}•{RS}] {C}User Info{Y}:{RS} {R}Sorry, we couldn't find that one ❗️{RS}"
                    )
            else:
                print(f"\n[{B} SESSIONIZE{RS} ]")

                print(
                    f"{' ' * 5}└[{R}•{RS}] {C}Connection Lost{Y}:{RS} {R}Oops! Unable To Establish A Connection{RS}"
                )
        except requests.exceptions.Timeout:
            print(f"\n[{B} SESSIONIZE{RS} ]")

            print(
                f"{' ' * 5}└[{R}•{RS}] {C}Timeout Error{Y}:{RS} {R}Oops! Timed Out{RS}"
            )
    except socket.gaierror:
        print(f"\n[{B} SESSIONIZE{RS} ]")

        print(
            f"{' ' * 5}└[{R}•{RS}] {C}DNS LookUp{Y}:{RS} {R}Oops! The {G}Dns Lookup{R} Failed And The Requested Domain Could Not Be Found.{RS}"
        )

    # [ CLUBHOUSE ]

    try:
        ip_address = socket.gethostbyname("clubhouse.com")
        # print('IP address:', ip_address)
        try:
            response = requests.get("https://www.clubhouse.com", timeout=5)
            if response.status_code == 200:
                CLUBHOUSE_Url = f"https://www.clubhouse.com/@{usernames}"

                CLUBHOUSE_Request = requests.get(CLUBHOUSE_Url)

                if CLUBHOUSE_Request.status_code == 200:

                    print(f"\n[{B} CLUBHOUSE{RS} ]")

                    print(f"{' ' * 5}└[{R}•{RS}] {C}User Url{Y}:{RS} {CLUBHOUSE_Url}")

                    CLUBHOUSE_Soup = BeautifulSoup(
                        CLUBHOUSE_Request.text, "html.parser"
                    )

                    PROFILE_NAME = CLUBHOUSE_Soup.find(
                        "p", attrs={"class": "Text-sc-12iul02-0 qEvAJ"}
                    )

                    FOLLOWER_PROFILE = CLUBHOUSE_Soup.find(
                        "div", attrs={"class": "Box-sc-jpzo4c-0 bVSHve"}
                    ).find("p", attrs={"class": "Text-sc-12iul02-0 kRCqoT"})

                    FOLLOWING_PROFILE = CLUBHOUSE_Soup.find(
                        "div", attrs={"class": "Box-sc-jpzo4c-0 hCFXoz"}
                    ).find("p", attrs={"class": "Text-sc-12iul02-0 kRCqoT"})

                    PROFILE_BIO = CLUBHOUSE_Soup.find(
                        "div",
                        attrs={
                            "class": "mt-5 sm:mt-4 text-sm sm:text-md text-gray-800"
                        },
                    )

                    if not PROFILE_NAME:
                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {R}Not Found ❗️{RS} "
                        )
                    else:
                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {PROFILE_NAME.string}"
                        )

                    if not FOLLOWER_PROFILE:
                        print(
                            f"{' ' * 5}└[{Y}•{RS}] {C}User Followers {Y}:{RS} {R}Not Found ❗️{RS} "
                        )
                    else:
                        print(
                            f"{' ' * 5}└[{Y}•{RS}] {C}User Followers {Y}:{RS} {FOLLOWER_PROFILE.string}"
                        )

                    if not FOLLOWING_PROFILE:
                        print(
                            f"{' ' * 5}└[{G}•{RS}] {C}User Following {Y}:{RS} {R}Not Found ❗️{RS} "
                        )
                    else:
                        print(
                            f"{' ' * 5}└[{G}•{RS}] {C}User Following {Y}:{RS} {FOLLOWING_PROFILE.string}"
                        )

                    if not PROFILE_BIO:
                        print(
                            f"{' ' * 5}└[{R}•{RS}] {C}User Bio {Y}:{RS} {R}Not Found ❗️{RS} "
                        )
                    else:
                        TEXT_TO_SPACE_REMOVE = PROFILE_BIO.getText()
                        After_remove_seeking_space = TEXT_TO_SPACE_REMOVE.strip()
                        print(
                            f"{' ' * 5}└[{R}•{RS}] {C}User Bio {Y}:{RS} {After_remove_seeking_space}"
                        )

                        UserMention_Bio = After_remove_seeking_space

                        Mention_Bio = re.findall(r"@[A-Za-z0-9.-]+", UserMention_Bio)

                        print(
                            f"{' ' * 5}└[{B}•{RS}] {C}List Of People Mention On USER Bio{Y}:{RS}"
                        )

                        if not Mention_Bio:
                            print(
                                f"{' ' * 20}└[{R}•{RS}] {Y}Mention Pople {C}On Bio {Y}:{RS} {R}Not Found ❗️{RS} \n"
                            )
                        else:
                            count = 0
                            for Mention_Bios in Mention_Bio:
                                count += 1
                                print(
                                    f"{' ' * 20}└[{R}{count}{RS}] {G}►{RS} {Mention_Bios}"
                                )

                        UserEmail = After_remove_seeking_space

                        emails = re.findall(r"[\w\.-]+@[\w\.-]+", UserEmail)

                        print(
                            f"{' ' * 5}└[{Y}•{RS}] {C}List Of Email Write On USER Bio{Y}:{RS}"
                        )

                        if not emails:
                            print(
                                f"{' ' * 20}└[{R}•{RS}] {C}Find {Y}Email {C}On Bio {Y}:{RS} {R}Not Found ❗️{RS} \n"
                            )
                        else:
                            count = 0
                        for email in emails:
                            count += 1
                            print(f"{' ' * 20}└[{R}{count}{RS}] {G}►{RS} {email}")

                        print(
                            f"{' ' * 5}└[{G}•{RS}] {C}List Of PhoneNumber Or Any Digit On USER Bio{Y}:{RS}"
                        )

                        PhoneNumberbio = After_remove_seeking_space

                        PhoneNumbers = re.findall(r"\d+", PhoneNumberbio)

                        if not PhoneNumbers:
                            print(
                                f"{' ' * 20}└[{R}•{RS}] {C}Find {Y}PhoneNumber {C}On Bio {Y}:{RS} {R}Not Found ❗️{RS} "
                            )
                        else:
                            count = 0
                        for PhoneNumber in PhoneNumbers:
                            count += 1
                            print(f"{' ' * 20}└[{R}{count}{RS}] {G}►{RS} {PhoneNumber}")

                elif CLUBHOUSE_Request.status_code == 404:
                    print(f"\n[{B} CLUBHOUSE{RS} ]")
                    print(
                        f"{' ' * 5}└[{R}•{RS}] {C}User Info{Y}:{RS} {R}Sorry, we couldn't find that one ❗️{RS}"
                    )

            else:
                print(f"\n[{B} CLUBHOUSE{RS} ]")

                print(
                    f"{' ' * 5}└[{R}•{RS}] {C}Connection Lost{Y}:{RS} {R}Oops! Unable To Establish A Connection{RS}"
                )
        except requests.exceptions.Timeout:
            print(f"\n[{B} CLUBHOUSE{RS} ]")

            print(
                f"{' ' * 5}└[{R}•{RS}] {C}Timeout Error{Y}:{RS} {R}Oops! Timed Out{RS}"
            )
    except socket.gaierror:
        print(f"\n[{B} CLUBHOUSE{RS} ]")

        print(
            f"{' ' * 5}└[{R}•{RS}] {C}DNS LookUp{Y}:{RS} {R}Oops! The {G}Dns Lookup{R} Failed And The Requested Domain Could Not Be Found.{RS}"
        )

    # [ CONTENTLY ]

    CONTENTLY_Url = f"https://{usernames}.contently.com/"

    CONTENTLY_Request = requests.get(CONTENTLY_Url)

    if CONTENTLY_Request.status_code == 200:

        print(f"\n[{B} CONTENTLY{RS} ]")

        print(f"{' ' * 5}└[{R}•{RS}] {C}User Url{Y}:{RS} {CONTENTLY_Url}")

        CONTENTLY_Soup = BeautifulSoup(CONTENTLY_Request.text, "html.parser")

        CONTENTLY_NAME = CONTENTLY_Soup.find("meta", attrs={"name": "author"})
        CONTENTLY_DESCRIPTION = CONTENTLY_Soup.find(
            "meta", attrs={"name": "description"}
        )
        CONTENTLY_IMAGE = CONTENTLY_Soup.find("meta", attrs={"property": "og:image"})

        if not CONTENTLY_NAME:
            print(
                f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {R}Not Found ❗️{RS} "
            )
        else:
            print(
                f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {CONTENTLY_NAME['content']}"
            )

        if not CONTENTLY_DESCRIPTION:
            print(
                f"{' ' * 5}└[{Y}•{RS}] {C}User Description {Y}:{RS} {R}Not Found ❗️{RS} "
            )
        else:
            print(
                f"{' ' * 5}└[{Y}•{RS}] {C}User Description {Y}:{RS} {CONTENTLY_DESCRIPTION['content']}"
            )

            UserMention_Bio = CONTENTLY_DESCRIPTION["content"]

            Mention_Bio = re.findall(r"@[A-Za-z0-9.-]+", UserMention_Bio)

            print(
                f"{' ' * 5}└[{B}•{RS}] {C}List Of People Mention On USER Description{Y}:{RS}"
            )

            if not Mention_Bio:
                print(
                    f"{' ' * 10}└[{R}•{RS}] {Y}Mention Pople {C}On Description {Y}:{RS} {R}Not Found ❗️{RS} \n"
                )
            else:
                count = 0
                for Mention_Bios in Mention_Bio:
                    count += 1
                    print(f"{' ' * 20}└[{R}{count}{RS}] {G}►{RS} {Mention_Bios}")

            UserEmail = CONTENTLY_DESCRIPTION["content"]

            emails = re.findall(r"[\w\.-]+@[\w\.-]+", UserEmail)

            print(
                f"{' ' * 5}└[{B}•{RS}] {C}List Of Email Write On USER Description{Y}:{RS}"
            )

            if not emails:
                print(
                    f"{' ' * 10}└[{R}•{RS}] {C}Find {Y}Email {C}On Description {Y}:{RS} {R}Not Found ❗️{RS} \n"
                )
            else:
                count = 0
            for email in emails:
                count += 1
                print(f"{' ' * 20}└[{R}{count}{RS}] {G}►{RS} {email}")

            print(
                f"{' ' * 5}└[{B}•{RS}] {C}List Of PhoneNumber Or Any Digit On USER Description{Y}:{RS}"
            )

            PhoneNumberbio = CONTENTLY_DESCRIPTION["content"]

            PhoneNumbers = re.findall(r"\d+", PhoneNumberbio)

            if not PhoneNumbers:
                print(
                    f"{' ' * 10}└[{R}•{RS}] {C}Find {Y}PhoneNumber {C}On Description {Y}:{RS} {R}Not Found ❗️{RS} "
                )
            else:
                count = 0
            for PhoneNumber in PhoneNumbers:
                count += 1
                print(f"{' ' * 20}└[{R}{count}{RS}] {G}►{RS} {PhoneNumber}")

        if not CONTENTLY_IMAGE:
            print(
                f"{' ' * 5}└[{Y}•{RS}] {C}User Profile Photo {Y}:{RS} {R}Not Found ❗️{RS} "
            )
        else:
            print(
                f"{' ' * 5}└[{Y}•{RS}] {C}User Profile Photo {Y}:{RS} {CONTENTLY_IMAGE['content']}"
            )

    elif CONTENTLY_Request.status_code == 404:
        print(f"\n[{B} CONTENTLY{RS} ]")
        print(
            f"{' ' * 5}└[{R}•{RS}] {C}User Info{Y}:{RS} {R}Sorry, we couldn't find that one ❗️{RS}"
        )

    # [ DISCOGS ]

    DISCOGS_Url = f"https://www.discogs.com/user/{usernames}"

    DISCOGS_Request = requests.get(DISCOGS_Url)

    if DISCOGS_Request.status_code == 200:

        print(f"\n[{B} DISCOGS{RS} ]")

        print(f"{' ' * 5}└[{R}•{RS}] {C}User Url{Y}:{RS} {DISCOGS_Url}")

        DISCOGS_Soup = BeautifulSoup(DISCOGS_Request.text, "html.parser")

        DISCOGS_Joined = DISCOGS_Soup.find(
            "div", attrs={"class": "aside_left aside_narrow"}
        )

        if not DISCOGS_Joined:
            print(f"{' ' * 5}└[{B}•{RS}] {C}User Joined {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            Joined_REPLACE = (
                DISCOGS_Joined.find("ul").find("li").string.replace("Joined on ", " ")
            )
            print(f"{' ' * 5}└[{B}•{RS}] {C}User Joined {Y}:{RS} {Joined_REPLACE}")

    elif DISCOGS_Request.status_code == 404:
        print(f"\n[{B} DISCOGS{RS} ]")
        print(
            f"{' ' * 5}└[{R}•{RS}] {C}User Info{Y}:{RS} {R}Sorry, we couldn't find that one ❗️{RS}"
        )

    # [ DOCKER ]

    docker_url = f"https://hub.docker.com/v2/users/{usernames}/"

    docker_request = requests.get(docker_url)

    docker_json = json.loads(docker_request.content)

    if docker_request.status_code == 404:
        print(f"\n[{B} DOCKER{RS} ]")

        print(f"{' ' * 5}└[{R}•{RS}] {C}User Info{Y}:{RS} {R}User not found ❗️{RS}")

    if docker_request.status_code == 200:
        print(f"\n[{B} DOCKER{RS} ]")

        print(
            f"{' ' * 5}└[{R}•{RS}] {C}User Url {Y}:{RS} {f'https://hub.docker.com/u/{usernames}'}"
        )

        if not docker_json["full_name"]:
            print(
                f"{' ' * 5}└[{B}•{RS}] {C}User FullName {Y}:{RS} {R}Not Found ❗️{RS} "
            )
        else:
            print(
                f"{' ' * 5}└[{B}•{RS}] {C}User FullName {Y}:{RS} {docker_json['full_name']}"
            )

        if not docker_json["location"]:
            print(
                f"{' ' * 5}└[{Y}•{RS}] {C}User Location {Y}:{RS} {R}Not Found ❗️{RS} "
            )
        else:
            print(
                f"{' ' * 5}└[{Y}•{RS}] {C}User Location {Y}:{RS} {docker_json['location']}"
            )

        if not docker_json["company"]:
            print(f"{' ' * 5}└[{G}•{RS}] {C}User Company {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(
                f"{' ' * 5}└[{G}•{RS}] {C}User Company {Y}:{RS} {docker_json['company']}"
            )

        if not docker_json["profile_url"]:
            print(
                f"{' ' * 5}└[{R}•{RS}] {C}User Profile Url {Y}:{RS} {R}Not Found ❗️{RS} "
            )
        else:
            print(
                f"{' ' * 5}└[{R}•{RS}] {C}User Profile Url {Y}:{RS} {docker_json['profile_url']}"
            )

        if not docker_json["date_joined"]:
            print(
                f"{' ' * 5}└[{B}•{RS}] {C}User Joined Date {Y}:{RS} {R}Not Found ❗️{RS} "
            )
        else:
            print(
                f"{' ' * 5}└[{B}•{RS}] {C}User Joined Date {Y}:{RS} {docker_json['date_joined']}"
            )

        if not docker_json["gravatar_url"]:
            print(
                f"{' ' * 5}└[{Y}•{RS}] {C}User Profile Photo {Y}:{RS} {R}Not Found ❗️{RS} "
            )
        else:
            print(
                f"{' ' * 5}└[{Y}•{RS}] {C}User Profile Photo {Y}:{RS} {docker_json['gravatar_url']}"
            )

        if not docker_json["gravatar_email"]:
            print(f"{' ' * 5}└[{G}•{RS}] {C}User Email {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(
                f"{' ' * 5}└[{G}•{RS}] {C}User Email {Y}:{RS} {docker_json['gravatar_email']}"
            )

        if not docker_json["type"]:
            print(f"{' ' * 5}└[{R}•{RS}] {C}User Type {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(f"{' ' * 5}└[{R}•{RS}] {C}User Type {Y}:{RS} {docker_json['type']}")

    # [ EYEEM ]

    try:
        ip_address = socket.gethostbyname("eyeem.com")

        EYEEM_Url = f"https://www.eyeem.com/u/{usernames}"

        EYEEM_Request = requests.get(EYEEM_Url)

        if EYEEM_Request.status_code == 200:

            print(f"\n[{B} EYEEM{RS} ]")

            print(f"{' ' * 5}└[{R}•{RS}] {C}User Url{Y}:{RS} {EYEEM_Url}")

            EYEEM_Soup = BeautifulSoup(EYEEM_Request.text, "html.parser")

            EYEEM_NAME = EYEEM_Soup.find("div", attrs={"class": "css-64wcgg"}).find(
                "h1", attrs={"class": "css-a88me eulhdfc0"}
            )

            EYEEM_BIO = EYEEM_Soup.find("div", attrs={"class": "css-1mpr9jb eqclr3s0"})

            EYEEM_PROFILE_PHOTO = EYEEM_Soup.find("div", attrs={"class": "css-kx2m0z"})

            if not EYEEM_NAME:
                print(
                    f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {R}Not Found ❗️{RS} "
                )
            else:
                print(
                    f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {EYEEM_NAME.string}"
                )

            if not EYEEM_PROFILE_PHOTO:
                print(
                    f"{' ' * 5}└[{B}•{RS}] {C}User Profile Photo {Y}:{RS} {R}Not Found ❗️{RS} "
                )
            else:
                print(
                    f"{' ' * 5}└[{B}•{RS}] {C}User Profile Photo {Y}:{RS} {EYEEM_PROFILE_PHOTO.find_all('img')[0].attrs['src']}"
                )

            if not EYEEM_BIO:
                print(f"{' ' * 5}└[{Y}•{RS}] {C}User Bio {Y}:{RS} {R}Not Found ❗️{RS} ")
            else:
                print(
                    f"{' ' * 5}└[{Y}•{RS}] {C}User Bio {Y}:{RS} {EYEEM_BIO.find('span', attrs={'class': 'css-1yzq2te eulhdfc0'}).string}"
                )

                UserMention_Bio = EYEEM_BIO.find(
                    "span", attrs={"class": "css-1yzq2te eulhdfc0"}
                ).string

                Mention_Bio = re.findall(r"@[A-Za-z0-9.-]+", UserMention_Bio)

                print(
                    f"{' ' * 5}└[{R}•{RS}] {C}List Of People Mention On USER Bio{Y}:{RS}"
                )

                if not Mention_Bio:
                    print(
                        f"{' ' * 10}└[{R}•{RS}] {Y}Mention Pople {C}On Bio {Y}:{RS} {R}Not Found ❗️{RS} \n"
                    )
                else:
                    count = 0
                    for Mention_Bios in Mention_Bio:
                        count += 1
                        print(f"{' ' * 20}└[{R}{count}{RS}] {G}►{RS} {Mention_Bios}")

                UserEmail = EYEEM_BIO.find(
                    "span", attrs={"class": "css-1yzq2te eulhdfc0"}
                ).string

                emails = re.findall(r"[\w\.-]+@[\w\.-]+", UserEmail)

                print(
                    f"{' ' * 5}└[{B}•{RS}] {C}List Of Email Write On USER Bio{Y}:{RS}"
                )

                if not emails:
                    print(
                        f"{' ' * 10}└[{R}•{RS}] {C}Find {Y}Email {C}On Bio {Y}:{RS} {R}Not Found ❗️{RS} \n"
                    )
                else:
                    count = 0
                for email in emails:
                    count += 1
                    print(f"{' ' * 20}└[{R}{count}{RS}] {G}►{RS} {email}")

                print(
                    f"{' ' * 5}└[{Y}•{RS}] {C}List Of PhoneNumber Or Any Digit On USER Bio{Y}:{RS}"
                )

                PhoneNumberbio = EYEEM_BIO.find(
                    "span", attrs={"class": "css-1yzq2te eulhdfc0"}
                ).string

                PhoneNumbers = re.findall(r"\d+", PhoneNumberbio)

                if not PhoneNumbers:
                    print(
                        f"{' ' * 10}└[{R}•{RS}] {C}Find {Y}PhoneNumber {C}On Bio {Y}:{RS} {R}Not Found ❗️{RS} "
                    )
                else:
                    count = 0
                for PhoneNumber in PhoneNumbers:
                    count += 1
                    print(f"{' ' * 20}└[{R}{count}{RS}] {G}►{RS} {PhoneNumber}")

        elif EYEEM_Request.status_code == 404:
            print(f"\n[{B} EYEEM{RS} ]")
            print(
                f"{' ' * 5}└[{R}•{RS}] {C}User Info{Y}:{RS} {R}Sorry, we couldn't find that one ❗️{RS}"
            )

    except socket.gaierror:
        print(f"\n[{B} EYEEM{RS} ]")
        print(
            f"{' ' * 5}└[{R}•{RS}] {C}DNS LookUp{Y}:{RS} {R}Oops! The {G}Dns Lookup{R} Failed And The Requested Domain Could Not Be Found.{RS}"
        )

    # [ FANDOM ]

    FANDOM_Url = f"https://www.fandom.com/u/{usernames}"

    FANDOM_Request = requests.get(FANDOM_Url)

    if FANDOM_Request.status_code == 200:

        print(f"\n[{B} FANDOM{RS} ]")

        print(f"{' ' * 5}└[{R}•{RS}] {C}User Url{Y}:{RS} {FANDOM_Url}")

        FANDOM_Soup = BeautifulSoup(FANDOM_Request.text, "html.parser")

        FANDOM_NAME = FANDOM_Soup.find(
            "div", attrs={"class": "profile-info-card__info"}
        ).find("h1", attrs={"class": "profile-info-card__name"})

        FANDOM_ABOUT = FANDOM_Soup.find(
            "div", attrs={"class": "profile-info-card__about"}
        )

        FANDOM_PROFILE_PHOTO = FANDOM_Soup.find(
            "div", attrs={"class": "profile-avatar__avatar"}
        )

        if not FANDOM_NAME:
            print(
                f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {R}Not Found ❗️{RS} "
            )
        else:
            print(
                f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {FANDOM_NAME.string}"
            )

        if not FANDOM_ABOUT:
            print(f"{' ' * 5}└[{Y}•{RS}] {C}User About {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(f"{' ' * 5}└[{Y}•{RS}] {C}User About {Y}:{RS} {FANDOM_ABOUT.string}")

            UserMention_Bio = FANDOM_ABOUT.string

            Mention_Bio = re.findall(r"@[A-Za-z0-9.-]+", UserMention_Bio)

            print(f"{' ' * 5}└[{R}•{RS}] {C}List Of People Mention On USER Bio{Y}:{RS}")

            if not Mention_Bio:
                print(
                    f"{' ' * 10}└[{R}•{RS}] {Y}Mention Pople {C}On Bio {Y}:{RS} {R}Not Found ❗️{RS} \n"
                )
            else:
                count = 0
                for Mention_Bios in Mention_Bio:
                    count += 1
                    print(f"{' ' * 20}└[{R}{count}{RS}] {G}►{RS} {Mention_Bios}")

            UserEmail = FANDOM_ABOUT.string

            emails = re.findall(r"[\w\.-]+@[\w\.-]+", UserEmail)

            print(f"{' ' * 5}└[{B}•{RS}] {C}List Of Email Write On USER Bio{Y}:{RS}")

            if not emails:
                print(
                    f"{' ' * 10}└[{R}•{RS}] {C}Find {Y}Email {C}On Bio {Y}:{RS} {R}Not Found ❗️{RS} \n"
                )
            else:
                count = 0
            for email in emails:
                count += 1
                print(f"{' ' * 20}└[{R}{count}{RS}] {G}►{RS} {email}")

            print(
                f"{' ' * 5}└[{Y}•{RS}] {C}List Of PhoneNumber Or Any Digit On USER Bio{Y}:{RS}"
            )

            PhoneNumberbio = FANDOM_ABOUT.string

            PhoneNumbers = re.findall(r"\d+", PhoneNumberbio)

            if not PhoneNumbers:
                print(
                    f"{' ' * 10}└[{R}•{RS}] {C}Find {Y}PhoneNumber {C}On Bio {Y}:{RS} {R}Not Found ❗️{RS} \n"
                )
            else:
                count = 0
            for PhoneNumber in PhoneNumbers:
                count += 1
                print(f"{' ' * 20}└[{R}{count}{RS}] {G}►{RS} {PhoneNumber}\n")

        if not FANDOM_PROFILE_PHOTO:
            print(
                f"{' ' * 5}└[{G}•{RS}] {C}User Profile Photo {Y}:{RS} {R}Not Found ❗️{RS} "
            )
        else:
            print(
                f"{' ' * 5}└[{G}•{RS}] {C}User Profile Photo {Y}:{RS} {FANDOM_PROFILE_PHOTO.find_all('img')[0].attrs['src']}"
            )

    elif FANDOM_Request.status_code == 404:

        print(f"\n[{B} FANDOM{RS} ]")

        print(
            f"{' ' * 5}└[{R}•{RS}] {C}User Info{Y}:{RS} {R}Sorry, we couldn't find that one ❗️{RS}"
        )

    # [ FLIGHTRADAR24 ]

    FLIGHTRADAR24_URL = f"https://my.flightradar24.com/{usernames}"

    FLIGHTRADAR24_Request = requests.get(FLIGHTRADAR24_URL)

    if FLIGHTRADAR24_Request.status_code == 200:

        print(f"\n[{B} FLIGHTRADAR24{RS} ]")

        FLIGHTRADAR24_Soup = BeautifulSoup(FLIGHTRADAR24_Request.text, "html.parser")

        FLIGHTRADAR24_FULL_NAME = FLIGHTRADAR24_Soup.find(
            "div", attrs={"class": "container profile-container"}
        )

        FLIGHTRADAR24_ACCOUNT_PRIVATE = FLIGHTRADAR24_Soup.find(
            "div", attrs={"class": "container"}
        ).find("h1")

        print(f"{' ' * 5}└[{R}•{RS}] {C}User Url {Y}:{RS} {FLIGHTRADAR24_URL}")

        if not FLIGHTRADAR24_ACCOUNT_PRIVATE:

            if not FLIGHTRADAR24_FULL_NAME:
                print(
                    f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {R}Not Found ❗️{RS} "
                )
            else:
                print(
                    f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {FLIGHTRADAR24_FULL_NAME.find('h3').getText()}"
                )
            print(
                f"{' ' * 5}└[{Y}•{RS}] {C}User Profile Private {Y}:{RS} [ {G}LIVE{RS} ] {RS}️{RS} "
            )
        else:
            print(
                f"{' ' * 5}└[{B}•{RS}] {C}User Profile Private {Y}:{RS} {FLIGHTRADAR24_ACCOUNT_PRIVATE.getText()}"
            )

    elif FLIGHTRADAR24_Request.status_code == 404:
        print(f"\n[{B} FLIGHTRADAR24{RS} ]")
        print(
            f"{' ' * 5}└[{R}•{RS}] {C}User Info{Y}:{RS} {R}Sorry, we couldn't find that one ❗️{RS}"
        )

    # [ GITEE ]

    GITEE_URL = f"https://gitee.com/{usernames}"

    GITEE_Request = requests.get(GITEE_URL)

    if GITEE_Request.status_code == 200:

        print(f"\n[{B} GITEE{RS} ]")

        GITEE_Soup = BeautifulSoup(GITEE_Request.text, "html.parser")

        GITEE_FULL_NAME = GITEE_Soup.find(
            "div", attrs={"class": "users__personal-name"}
        ).find("span")

        GITEE_BIO = GITEE_Soup.find(
            "div", attrs={"class": "users__personal-name"}
        ).find("p", attrs={"class": "bio"})

        print(f"{' ' * 5}└[{R}•{RS}] {C}User Url {Y}:{RS} {GITEE_URL}")

        if not GITEE_FULL_NAME:
            print(
                f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {R}Not Found ❗️{RS} "
            )
        else:
            space_remove = GITEE_FULL_NAME.getText()
            After_remove_space = space_remove.strip()
            print(
                f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {After_remove_space}"
            )

        if not GITEE_BIO:
            print(f"{' ' * 5}└[{Y}•{RS}] {C}User Bio {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(f"{' ' * 5}└[{Y}•{RS}] {C}User Bio {Y}:{RS} {GITEE_BIO.string}")

    elif GITEE_Request.status_code == 404:

        print(f"\n[{B} GITEE{RS} ]")

        print(
            f"{' ' * 5}└[{R}•{RS}] {C}User Info{Y}:{RS} {R}Sorry, we couldn't find that one ❗️{RS}"
        )

    # [ PLUGINS.GRADLE ]

    PLUGINS_GRADLE_URL = f"https://plugins.gradle.org/u/{usernames}"

    PLUGINS_GRADLE_Request = requests.get(PLUGINS_GRADLE_URL)

    if PLUGINS_GRADLE_Request.status_code == 200:

        print(f"\n[{B} PLUGINS_GRADLE{RS} ]")

        PLUGINS_GRADLE_Soup = BeautifulSoup(PLUGINS_GRADLE_Request.text, "html.parser")

        PLUGINS_GRADLE_FULL_NAME = PLUGINS_GRADLE_Soup.find(
            "div", attrs={"class": "col-md-4"}
        ).find("div", attrs={"id": "name"})

        PLUGINS_GRADLE_JOINED = PLUGINS_GRADLE_Soup.find(
            "div", attrs={"class": "col-md-4"}
        ).find("div", attrs={"id": "joined"})

        print(f"{' ' * 5}└[{R}•{RS}] {C}User Url {Y}:{RS} {PLUGINS_GRADLE_URL}")

        if not PLUGINS_GRADLE_FULL_NAME:
            print(
                f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {R}Not Found ❗️{RS} "
            )
        else:
            print(
                f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {PLUGINS_GRADLE_FULL_NAME.string}"
            )

        if not PLUGINS_GRADLE_JOINED:
            print(f"{' ' * 5}└[{Y}•{RS}] {C}User Joined {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(
                f"{' ' * 5}└[{Y}•{RS}] {C}User Joined {Y}:{RS} {PLUGINS_GRADLE_JOINED.string}"
            )

    elif PLUGINS_GRADLE_Request.status_code == 404:

        print(f"\n[{B} PLUGINS_GRADLE{RS} ]")

        print(
            f"{' ' * 5}└[{R}•{RS}] {C}User Info{Y}:{RS} {R}Sorry, we couldn't find that one ❗️{RS}"
        )

    # [ HACKADAY ]

    HACKADAY_URL = f"https://hackaday.io/{usernames}"

    HACKADAY_Request = requests.get(HACKADAY_URL)

    if HACKADAY_Request.status_code == 200:

        print(f"\n[{B} HACKADAY{RS} ]")

        HACKADAY_Soup = BeautifulSoup(HACKADAY_Request.text, "html.parser")

        HACKADAY_FULL_NAME = HACKADAY_Soup.find(
            "div", attrs={"class": "container"}
        ).find("h1")

        HACKADAY_DESCRIPTION = HACKADAY_Soup.find(
            "div", attrs={"class": "container"}
        ).find("p", attrs={"class": "description"})

        print(f"{' ' * 5}└[{R}•{RS}] {C}User Url {Y}:{RS} {HACKADAY_URL}")

        if not HACKADAY_FULL_NAME:
            print(
                f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {R}Not Found ❗️{RS} "
            )
        else:
            print(
                f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {HACKADAY_FULL_NAME.string}"
            )

        if not HACKADAY_DESCRIPTION:
            print(
                f"{' ' * 5}└[{Y}•{RS}] {C}User Description {Y}:{RS} {R}Not Found ❗️{RS} "
            )
        else:
            print(
                f"{' ' * 5}└[{Y}•{RS}] {C}User Description {Y}:{RS} {HACKADAY_DESCRIPTION.string}"
            )

    elif HACKADAY_Request.status_code == 404:

        print(f"\n[{B} HACKADAY{RS} ]")

        print(
            f"{' ' * 5}└[{R}•{RS}] {C}User Info{Y}:{RS} {R}Sorry, we couldn't find that one ❗️{RS}"
        )

    # [ HACKEREARTH ]

    url = f"https://www.hackerearth.com/profiles/api/{usernames}/personal-details/"

    HACKEREARTH_RESPONSE = requests.request("GET", url)

    if HACKEREARTH_RESPONSE.status_code == 200:

        HACKEREARTH_JSON = json.loads(HACKEREARTH_RESPONSE.content)

        print(f"\n[{B} HACKEREARTH{RS} ]")
        print(
            f"{' ' * 5}└[{R}•{RS}] {C}User Url {Y}:{RS} {f'https://www.hackerearth.com/@{usernames}'}"
        )
        print(
            f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {HACKEREARTH_JSON.get('full_name')}"
        )
        print(
            f"{' ' * 5}└[{Y}•{RS}] {C}User Location {Y}:{RS} {HACKEREARTH_JSON.get('location')}"
        )
        print(
            f"{' ' * 5}└[{G}•{RS}] {C}User Facebook {Y}:{RS} {HACKEREARTH_JSON.get('facebook')}"
        )
        print(
            f"{' ' * 5}└[{R}•{RS}] {C}User Linkedin {Y}:{RS} {HACKEREARTH_JSON.get('linkedin')}"
        )
        print(
            f"{' ' * 5}└[{B}•{RS}] {C}User GitHub {Y}:{RS} {HACKEREARTH_JSON.get('github')}"
        )
        print(
            f"{' ' * 5}└[{Y}•{RS}] {C}User Twitter {Y}:{RS} {HACKEREARTH_JSON.get('twitter')}"
        )
        print(
            f"{' ' * 5}└[{G}•{RS}] {C}User Blog {Y}:{RS} {HACKEREARTH_JSON.get('blog')}"
        )
        print(
            f"{' ' * 5}└[{R}•{RS}] {C}User Website {Y}:{RS} {HACKEREARTH_JSON.get('website')}"
        )

    elif HACKEREARTH_RESPONSE.status_code == 400:
        print(f"\n[{B} HACKEREARTH{RS} ]")
        print(
            f"{' ' * 5}└[{R}•{RS}] {C}User Info{Y}:{RS} {R}Sorry, we couldn't find that one ❗️{RS}"
        )

    # [ NEWS_YCOMBINATOR ]

    NEWS_YCOMBINATOR_url = f"https://news.ycombinator.com/user?id={usernames}"

    NEWS_YCOMBINATOR_RESPONSE = requests.request("GET", NEWS_YCOMBINATOR_url)

    if NEWS_YCOMBINATOR_RESPONSE.status_code == 200:

        NEWS_YCOMBINATOR_Soup = BeautifulSoup(
            NEWS_YCOMBINATOR_RESPONSE.text, "html.parser"
        )

        if NEWS_YCOMBINATOR_Soup.string == "No such user.":

            print(f"\n[{B} NEWS YCOMBINATOR{RS} ]")

            print(
                f"{' ' * 5}└[{R}•{RS}] {C}User Info{Y}:{RS} {R}Sorry, we couldn't find that one ❗️{RS}"
            )
        else:

            NEWS_YCOMBINATOR_NAME = NEWS_YCOMBINATOR_Soup.find(
                "tr", attrs={"class": "athing"}
            )

            print(f"\n[{B} NEWS YCOMBINATOR{RS} ]")

            print(f"{' ' * 5}└[{R}•{RS}] {C}User Url {Y}:{RS} {NEWS_YCOMBINATOR_url}")

            if not NEWS_YCOMBINATOR_NAME:
                print(
                    f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {R}Not Found ❗️{RS} "
                )
            else:
                print(
                    f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {NEWS_YCOMBINATOR_NAME.find('a', attrs={'class': 'hnuser'}).string}"
                )
    # [ HACKERONE ]

    HACKERONE_url = f"https://hackerone.com/{usernames}?type=user"

    HACKERONE_RESPONSE = requests.request("GET", HACKERONE_url)

    if HACKERONE_RESPONSE.status_code == 200:

        HACKERONE_Soup = BeautifulSoup(HACKERONE_RESPONSE.text, "html.parser")

        HACKERONE_DESCRIPTION = HACKERONE_Soup.find("meta", property="og:description")

        HACKERONE_PROFILE_PIC = HACKERONE_Soup.find("meta", property="og:image")

        HACKERONE_NAME = HACKERONE_Soup.find("meta", property="og:title")

        print(f"\n[{B} HACKERONE{RS} ]")

        print(f"{' ' * 5}└[{R}•{RS}] {C}User Url{Y}:{RS} {HACKERONE_url}")

        if not HACKERONE_DESCRIPTION:
            print(
                f"{' ' * 5}└[{G}•{RS}] {C}User Profile Name {Y}:{RS} {R}Not Found ❗️{RS} "
            )
        else:

            Name_HACKERONE = HACKERONE_NAME["content"]

            FINAL_NAME = Name_HACKERONE.replace("HackerOne profile - ", "")

            print(f"{' ' * 5}└[{G}•{RS}] {C}User Profile Name {Y}:{RS} {FINAL_NAME}")

        if not HACKERONE_DESCRIPTION:
            print(f"{' ' * 5}└[{B}•{RS}] {C}User Bio {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(
                f"{' ' * 5}└[{B}•{RS}] {C}User Bio {Y}:{RS} {HACKERONE_DESCRIPTION['content']}"
            )

            UserMention_Bio = HACKERONE_DESCRIPTION["content"]

            Mention_Bio = re.findall(r"@[A-Za-z0-9.-]+", UserMention_Bio)

            print(f"{' ' * 5}└[{R}•{RS}] {C}List Of People Mention On USER Bio{Y}:{RS}")

            if not Mention_Bio:
                print(
                    f"{' ' * 10}└[{R}•{RS}] {Y}Mention Pople {C}On Bio {Y}:{RS} {R}Not Found ❗️{RS} \n"
                )
            else:
                count = 0
                for Mention_Bios in Mention_Bio:
                    count += 1
                    print(f"{' ' * 20}└[{R}{count}{RS}] {G}►{RS} {Mention_Bios}")

            UserEmail = HACKERONE_DESCRIPTION["content"]

            emails = re.findall(r"[\w\.-]+@[\w\.-]+", UserEmail)

            print(f"{' ' * 5}└[{B}•{RS}] {C}List Of Email Write On USER Bio{Y}:{RS}")

            if not emails:
                print(
                    f"{' ' * 10}└[{R}•{RS}] {C}Find {Y}Email {C}On Bio {Y}:{RS} {R}Not Found ❗️{RS} \n"
                )
            else:
                count = 0
            for email in emails:
                count += 1
                print(f"{' ' * 20}└[{R}{count}{RS}] {G}►{RS} {email}")

            print(
                f"{' ' * 5}└[{Y}•{RS}] {C}List Of PhoneNumber Or Any Digit On USER Bio{Y}:{RS}"
            )

            PhoneNumberbio = HACKERONE_DESCRIPTION["content"]

            PhoneNumbers = re.findall(r"\d+", PhoneNumberbio)

            if not PhoneNumbers:
                print(
                    f"{' ' * 10}└[{R}•{RS}] {C}Find {Y}PhoneNumber {C}On Bio {Y}:{RS} {R}Not Found ❗️{RS} \n"
                )
            else:
                count = 0
            for PhoneNumber in PhoneNumbers:
                count += 1
                print(f"{' ' * 20}└[{R}{count}{RS}] {G}►{RS} {PhoneNumber}")

        if not HACKERONE_PROFILE_PIC:
            print(
                f"{' ' * 5}└[{Y}•{RS}] {C}User Profile Photo {Y}:{RS} {R}Not Found ❗️{RS} "
            )
        else:
            print(
                f"{' ' * 5}└[{Y}•{RS}] {C}User Profile Photo {Y}:{RS} {HACKERONE_PROFILE_PIC['content']}"
            )

    elif HACKERONE_RESPONSE.status_code == 404:

        print(f"\n[{B} HACKERONE{RS} ]")

        print(
            f"{' ' * 5}└[{R}•{RS}] {C}User Info{Y}:{RS} {R}Sorry, we couldn't find that one ❗️{RS}"
        )

    # [ HACKERRANK ]

    HACKERRANK_url = f"https://www.hackerrank.com/rest/query_slug?slug={usernames}"

    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.33",
    }

    HACKERRANK_RESPONSE = requests.request("GET", HACKERRANK_url, headers=headers)

    HACKERRANK_JSON = json.loads(HACKERRANK_RESPONSE.content)

    if HACKERRANK_JSON["type"] == None:

        print(f"\n[{B} HACKERRANK{RS} ]")

        print(
            f"{' ' * 5}└[{R}•{RS}] {C}User Info{Y}:{RS} {R}Sorry, we couldn't find that one ❗️{RS}"
        )

    elif HACKERRANK_JSON["type"] == "hacker":

        print(f"\n[{B} HACKERRANK{RS} ]")

        print(f"{' ' * 5}└[{R}•{RS}] {C}User Url{Y}:{RS} {HACKERRANK_url}")

        HACKERRANK_USER_URL = f"https://www.hackerrank.com/rest/contests/master/hackers/{usernames}/profile"

        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.33",
        }

        HACKERRANK_USER_RESPONSE = requests.request(
            "GET", HACKERRANK_USER_URL, headers=headers
        )

        HACKERRANK_USER_JSON = json.loads(HACKERRANK_USER_RESPONSE.content)

        print(
            f"{' ' * 5}└[{B}•{RS}] {C}User Profile ID {Y}:{RS} {HACKERRANK_USER_JSON['model'].get('id')}"
        )
        print(
            f"{' ' * 5}└[{B}•{RS}] {C}User Country {Y}:{RS} {HACKERRANK_USER_JSON['model'].get('country')}"
        )
        print(
            f"{' ' * 5}└[{B}•{RS}] {C}User School {Y}:{RS} {HACKERRANK_USER_JSON['model'].get('school')}"
        )
        print(
            f"{' ' * 5}└[{B}•{RS}] {C}User Languages {Y}:{RS} {HACKERRANK_USER_JSON['model'].get('languages')}"
        )
        print(
            f"{' ' * 5}└[{B}•{RS}] {C}User Created AT {Y}:{RS} {HACKERRANK_USER_JSON['model'].get('created_at')}"
        )
        print(
            f"{' ' * 5}└[{B}•{RS}] {C}User Level {Y}:{RS} {HACKERRANK_USER_JSON['model'].get('level')}"
        )
        print(
            f"{' ' * 5}└[{B}•{RS}] {C}User Is Admin {Y}:{RS} {HACKERRANK_USER_JSON['model'].get('is_admin')}"
        )
        print(
            f"{' ' * 5}└[{B}•{RS}] {C}User Support Admin {Y}:{RS} {HACKERRANK_USER_JSON['model'].get('support_admin')}"
        )
        print(
            f"{' ' * 5}└[{B}•{RS}] {C}User Avatar {Y}:{RS} {HACKERRANK_USER_JSON['model'].get('avatar')}"
        )
        print(
            f"{' ' * 5}└[{B}•{RS}] {C}User Website {Y}:{RS} {HACKERRANK_USER_JSON['model'].get('website')}"
        )
        print(
            f"{' ' * 5}└[{B}•{RS}] {C}User Short Bio {Y}:{RS} {HACKERRANK_USER_JSON['model'].get('short_bio')}"
        )
        print(
            f"{' ' * 5}└[{B}•{RS}] {C}User UserName Change Count {Y}:{RS} {HACKERRANK_USER_JSON['model'].get('username_change_count')}"
        )
        print(
            f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {HACKERRANK_USER_JSON['model'].get('name')}"
        )
        print(
            f"{' ' * 5}└[{B}•{RS}] {C}User Personal First Name {Y}:{RS} {HACKERRANK_USER_JSON['model'].get('personal_first_name')}"
        )
        print(
            f"{' ' * 5}└[{B}•{RS}] {C}User Personal Last Name {Y}:{RS} {HACKERRANK_USER_JSON['model'].get('personal_last_name')}"
        )
        print(
            f"{' ' * 5}└[{B}•{RS}] {C}User Company {Y}:{RS} {HACKERRANK_USER_JSON['model'].get('company')}"
        )
        print(
            f"{' ' * 5}└[{B}•{RS}] {C}User Local Language {Y}:{RS} {HACKERRANK_USER_JSON['model'].get('local_language')}"
        )
        print(
            f"{' ' * 5}└[{B}•{RS}] {C}User Has Avatar Url {Y}:{RS} {HACKERRANK_USER_JSON['model'].get('has_avatar_url')}"
        )
        print(
            f"{' ' * 5}└[{B}•{RS}] {C}User Hide Account Checklist {Y}:{RS} {HACKERRANK_USER_JSON['model'].get('hide_account_checklist')}"
        )
        print(
            f"{' ' * 5}└[{B}•{RS}] {C}User Spam {Y}:{RS} {HACKERRANK_USER_JSON['model'].get('spam_user')}"
        )
        print(
            f"{' ' * 5}└[{B}•{RS}] {C}User Job Title {Y}:{RS} {HACKERRANK_USER_JSON['model'].get('job_title')}"
        )
        print(
            f"{' ' * 5}└[{B}•{RS}] {C}User Jobs Headline {Y}:{RS} {HACKERRANK_USER_JSON['model'].get('jobs_headline')}"
        )
        print(
            f"{' ' * 5}└[{B}•{RS}] {C}User Linkedin Url {Y}:{RS} {HACKERRANK_USER_JSON['model'].get('linkedin_url')}"
        )
        print(
            f"{' ' * 5}└[{B}•{RS}] {C}User GitHub Url {Y}:{RS} {HACKERRANK_USER_JSON['model'].get('github_url')}"
        )
        print(
            f"{' ' * 5}└[{B}•{RS}] {C}User Self {Y}:{RS} {HACKERRANK_USER_JSON['model'].get('self')}"
        )
        print(
            f"{' ' * 5}└[{B}•{RS}] {C}User Title {Y}:{RS} {HACKERRANK_USER_JSON['model'].get('title')}"
        )
        print(
            f"{' ' * 5}└[{B}•{RS}] {C}User Event Count {Y}:{RS} {HACKERRANK_USER_JSON['model'].get('event_count')}"
        )
        print(
            f"{' ' * 5}└[{B}•{RS}] {C}User Online {Y}:{RS} {HACKERRANK_USER_JSON['model'].get('online')}"
        )
        print(
            f"{' ' * 5}└[{B}•{RS}] {C}User Is Following {Y}:{RS} {HACKERRANK_USER_JSON['model'].get('is_following')}"
        )
        print(
            f"{' ' * 5}└[{B}•{RS}] {C}User Is Followed {Y}:{RS} {HACKERRANK_USER_JSON['model'].get('is_followed')}"
        )
        print(
            f"{' ' * 5}└[{B}•{RS}] {C}User Followers Count {Y}:{RS} {HACKERRANK_USER_JSON['model'].get('followers_count')}"
        )

    elif HACKERRANK_JSON["type"] == "contest":

        print(f"\n[{B} HACKERRANK{RS} ]")

        print(f"{' ' * 5}└[{R}•{RS}] {C}User Url{Y}:{RS} {HACKERRANK_url}")

        print(
            f"\n{' ' * 5}[{G} NOTE {RS}] [ {C}A Competition To Do Better Than Other People, Usually In Which Prizes Are Given{RS} ] \n"
        )

    # [ HASHNODE ]

    HASHNODE_URL = f"https://hashnode.com/@{usernames}"

    HASHNODE_RESPONSE = requests.request("GET", HASHNODE_URL)

    if HASHNODE_RESPONSE.status_code == 200:

        print(f"\n[{B} HASHNODE{RS} ]")

        print(f"{' ' * 5}└[{R}•{RS}] {C}User Url{Y}:{RS} {HASHNODE_URL}")

        HASHNODE_Soup = BeautifulSoup(HASHNODE_RESPONSE.text, "html.parser")

        HASHNODE_NAME = HASHNODE_Soup.find("div", attrs={"class": "css-ch6q0t"})

        HASHNODE_BIO = HASHNODE_NAME.find("p", attrs={"class": "css-pbihhq"})

        if not HASHNODE_NAME:
            print(
                f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {R}Not Found ❗️{RS} "
            )
        else:
            print(
                f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {HASHNODE_NAME.find('h1').find('span', attrs={'itemprop': 'name'}).string}"
            )

        if not HASHNODE_BIO:
            print(f"{' ' * 5}└[{Y}•{RS}] {C}User Bio {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(f"{' ' * 5}└[{Y}•{RS}] {C}User Bio {Y}:{RS} {HASHNODE_BIO.string}")

    elif HASHNODE_RESPONSE.status_code == 404:

        print(f"\n[{B} HASHNODE{RS} ]")

        print(
            f"{' ' * 5}└[{R}•{RS}] {C}User Info{Y}:{RS} {R}Sorry, we couldn't find that one ❗️{RS}"
        )

    # [ HUBPAGES ]

    HUBPAGES_URL = f"https://hubpages.com/@{usernames}"

    HUBPAGES_RESPONSE = requests.request("GET", HUBPAGES_URL)

    if HUBPAGES_RESPONSE.status_code == 200:

        print(f"\n[{B} HUBPAGES{RS} ]")

        print(f"{' ' * 5}└[{R}•{RS}] {C}User Url{Y}:{RS} {HUBPAGES_URL}")

        HASHNODE_Soup = BeautifulSoup(HUBPAGES_RESPONSE.text, "html.parser")

        HASHNODE_NAME = HASHNODE_Soup.find("div", attrs={"class": "bio_stats"}).find(
            "span", attrs={"class": "author_primary_name"}
        )

        HASHNODE_JOINED = HASHNODE_Soup.find("div", attrs={"class": "bio_stats"}).find(
            "p", attrs={"class": "meta"}
        )

        HASHNODE_BIO = HASHNODE_Soup.find(
            "div", attrs={"class": "content_section"}
        ).find_all("p")

        HASHNODE_ARTICLES = HASHNODE_Soup.find(
            "div", attrs={"id": "user_stats"}
        ).find_all("div", attrs={"class": "value"})[0]

        HASHNODE_FOLLOWERS = HASHNODE_Soup.find(
            "div", attrs={"id": "user_stats"}
        ).find_all("div", attrs={"class": "value"})[1]

        HASHNODE_FOLLOWING = HASHNODE_Soup.find(
            "div", attrs={"id": "user_stats"}
        ).find_all("div", attrs={"class": "value"})[2]

        HASHNODE_PROFILE_PHOTO = HASHNODE_Soup.find(
            "div", attrs={"class": "user-pic-round"}
        ).find("img")

        if not HASHNODE_NAME:
            print(
                f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {R}Not Found ❗️{RS} "
            )
        else:
            print(
                f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {HASHNODE_NAME.string}"
            )

        if not HASHNODE_ARTICLES:
            print(
                f"{' ' * 5}└[{P}•{RS}] {C}User Articles Count {Y}:{RS} {R}Not Found ❗️{RS} "
            )
        else:
            print(
                f"{' ' * 5}└[{P}•{RS}] {C}User Articles Count {Y}:{RS} {HASHNODE_ARTICLES.string}"
            )

        if not HASHNODE_FOLLOWERS:
            print(
                f"{' ' * 5}└[{Y}•{RS}] {C}User Followers {Y}:{RS} {R}Not Found ❗️{RS} "
            )
        else:
            print(
                f"{' ' * 5}└[{Y}•{RS}] {C}User Followers {Y}:{RS} {HASHNODE_FOLLOWERS.string}"
            )

        if not HASHNODE_FOLLOWING:
            print(
                f"{' ' * 5}└[{G}•{RS}] {C}User Following {Y}:{RS} {R}Not Found ❗️{RS} "
            )
        else:
            print(
                f"{' ' * 5}└[{G}•{RS}] {C}User Following {Y}:{RS} {HASHNODE_FOLLOWING.string}"
            )

        if not HASHNODE_JOINED:
            print(
                f"{' ' * 5}└[{R}•{RS}] {C}User Joined & Last Activity {Y}:{RS} {R}Not Found ❗️{RS} "
            )
        else:
            print(
                f"{' ' * 5}└[{R}•{RS}] {C}User Joined & Last Activity {Y}:{RS} {HASHNODE_JOINED.text}"
            )

        if not HASHNODE_BIO:
            print(f"{' ' * 5}└[{B}•{RS}] {C}User Bio {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:

            HUBPAGES_REMOVE_WORD = f"{HASHNODE_BIO}"
            HUBPAGES_REMOVE_WORD_SEC = re.sub(r"</p>", "", HUBPAGES_REMOVE_WORD)
            HUBPAGES_REMOVE_WORD_THR = re.sub(r"<p>", "", HUBPAGES_REMOVE_WORD_SEC)

            print(
                f"{' ' * 5}└[{B}•{RS}] {C}User Bio {Y}:{RS} {HUBPAGES_REMOVE_WORD_THR}"
            )

        if not HASHNODE_PROFILE_PHOTO:
            print(
                f"{' ' * 5}└[{Y}•{RS}] {C}User Profile Photo {Y}:{RS} {R}Not Found ❗️{RS} "
            )
        else:

            HUBPAGES_IMG = HASHNODE_PROFILE_PHOTO
            HUBPAGES_IMG_URL = HUBPAGES_IMG["data-original"]
            print(
                f"{' ' * 5}└[{Y}•{RS}] {C}User Profile Photo {Y}:{RS} {HUBPAGES_IMG_URL}"
            )

    elif HUBPAGES_RESPONSE.status_code == 404:

        print(f"\n[{B} HUBPAGES{RS} ]")

        print(
            f"{' ' * 5}└[{R}•{RS}] {C}User Info{Y}:{RS} {R}Sorry, we couldn't find that one ❗️{RS}"
        )

    # [ IFTTT ]

    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.33",
    }

    IFTTT_URL = f"https://ifttt.com/p/{usernames}"

    IFTTT_RESPONSE = requests.request("GET", IFTTT_URL, headers=headers)

    if IFTTT_RESPONSE.status_code == 200:

        print(f"\n[{B} IFTTT{RS} ]")

        print(f"{' ' * 5}└[{R}•{RS}] {C}User Url{Y}:{RS} {IFTTT_URL}")

        IFTTT_Soup = BeautifulSoup(IFTTT_RESPONSE.text, "html.parser")

        IFTTT_NAME = IFTTT_Soup.find("div", attrs={"class": "user-login"}).find(
            "h1", attrs={"class": "author"}
        )

        IFTTT_JOINED_DATE = IFTTT_Soup.find(
            "section", attrs={"class": "service-header"}
        )

        if not IFTTT_NAME:
            print(
                f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {R}Not Found ❌ {RS}"
            )
        else:
            Remove_Text_To_Space = IFTTT_NAME.getText()
            Remove_Space_Text_Successful = Remove_Text_To_Space.strip()
            print(
                f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name  {Y}:{RS} {Remove_Space_Text_Successful}"
            )

        if not IFTTT_JOINED_DATE:
            print(
                f"{' ' * 5}└[{Y}•{RS}] {C}User Profile Name {Y}:{RS} {R}Not Found ❌ {RS}"
            )
        else:
            print(
                f"{' ' * 5}└[{Y}•{RS}] {C}User Profile Name  {Y}:{RS} {IFTTT_JOINED_DATE.find('p').string}"
            )

    elif IFTTT_RESPONSE.status_code == 404:

        print(f"\n[{B} IFTTT{RS} ]")

        print(
            f"{' ' * 5}└[{R}•{RS}] {C}User Info{Y}:{RS} {R}Sorry, we couldn't find that one ❗️{RS}"
        )

    # [ INSTRUCTABLES ]

    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.33",
    }

    INSTRUCTABLES_URL = (
        f"https://www.instructables.com/json-api/showAuthorStats?screenName={usernames}"
    )

    INSTRUCTABLES_RESPONSE = requests.request("GET", INSTRUCTABLES_URL, headers=headers)

    if INSTRUCTABLES_RESPONSE.status_code == 200:

        INSTRUCTABLES_JSON = json.loads(INSTRUCTABLES_RESPONSE.content)

        print(f"\n[{B} INSTRUCTABLES{RS} ]")

        print(
            f"{' ' * 5}└[{R}•{RS}] {C}User Url{Y}:{RS} https://www.instructables.com/member/{usernames}"
        )

        print(f"{' ' * 5}└[{B}•{RS}] {C}User Profile UserName {Y}:{RS} {usernames}{RS}")

        print(
            f"{' ' * 5}└[{Y}•{RS}] {C}User comment Count {Y}:{RS} {INSTRUCTABLES_JSON.get('commentCount')}{RS}"
        )

        print(
            f"{' ' * 5}└[{G}•{RS}] {C}User Views {Y}:{RS} {INSTRUCTABLES_JSON.get('views')}{RS}"
        )

        print(
            f"{' ' * 5}└[{R}•{RS}] {C}User Featured Count {Y}:{RS} {INSTRUCTABLES_JSON.get('featuredCount')}{RS}"
        )

        print(
            f"{' ' * 5}└[{B}•{RS}] {C}User Favorites Count {Y}:{RS} {INSTRUCTABLES_JSON.get('favoritesCount')}{RS}"
        )

        print(
            f"{' ' * 5}└[{Y}•{RS}] {C}User Instructables Count {Y}:{RS} {INSTRUCTABLES_JSON.get('instructablesCount')}{RS}"
        )

        print(
            f"{' ' * 5}└[{G}•{RS}] {C}User Published Collections Count {Y}:{RS} {INSTRUCTABLES_JSON.get('publishedCollectionsCount')}{RS}"
        )

        print(
            f"{' ' * 5}└[{P}•{RS}] {C}User Published Project Count {Y}:{RS} {INSTRUCTABLES_JSON.get('publishedProjectCount')}{RS}"
        )

        print(
            f"{' ' * 5}└[{R}•{RS}] {C}User Quarantined Project Count {Y}:{RS} {INSTRUCTABLES_JSON.get('quarantinedProjectCount')}{RS}"
        )

        print(
            f"{' ' * 5}└[{B}•{RS}] {C}User Limboed Project Count {Y}:{RS} {INSTRUCTABLES_JSON.get('limboedProjectCount')}{RS}"
        )

        print(
            f"{' ' * 5}└[{Y}•{RS}] {C}User Followers Count {Y}:{RS} {INSTRUCTABLES_JSON.get('followersCount')}{RS}"
        )

        print(
            f"{' ' * 5}└[{G}•{RS}] {C}User Subscriptions Count {Y}:{RS} {INSTRUCTABLES_JSON.get('subscriptionsCount')}{RS}"
        )

        print(
            f"{' ' * 5}└[{P}•{RS}] {C}User Collaborations Count {Y}:{RS} {INSTRUCTABLES_JSON.get('collaborationsCount')}{RS}"
        )

    elif INSTRUCTABLES_RESPONSE.status_code == 404:

        print(f"\n[{B} INSTRUCTABLES{RS} ]")

        print(
            f"{' ' * 5}└[{R}•{RS}] {C}User Info{Y}:{RS} {R}Sorry, we couldn't find that one ❗️{RS}"
        )

    # [ INTIGRITI ]

    try:
        ip_address = socket.gethostbyname("intigriti.com")
        # print('IP address:', ip_address)
        try:
            response = requests.get("https://www.intigriti.com", timeout=7)
            if response.status_code == 200:

                INTIGRITI_url = (
                    f"https://api.intigriti.com/user/public/profile/{usernames}"
                )

                INTIGRITI_headers = {
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.33"
                }

                INTIGRITI_response = requests.request(
                    "GET", INTIGRITI_url, headers=INTIGRITI_headers
                )

                if INTIGRITI_response.status_code == 200:

                    INTIGRITI_json = json.loads(INTIGRITI_response.content)

                    print(INTIGRITI_json)

                    print(f"\n[{B} INTIGRITI{RS} ]")

                    print(
                        f"{' ' * 5}└[{R}•{RS}] {C}User Url{Y}:{RS} https://app.intigriti.com/profile/{usernames}"
                    )

                    print(f"{' ' * 5}└[{B}•{RS}] {C}UserName{Y}:{RS} {usernames}")

                    if (
                        "avatarId" in INTIGRITI_json
                        and INTIGRITI_json["avatarId"] is not None
                    ):
                        photo_url = f"https://api.intigriti.com/file/api/file/{INTIGRITI_json['avatarId']}"
                        response = requests.get(photo_url)
                        if response.status_code == 200:
                            with open(
                                f"./../../Result/media/{usernames}.jpg", "wb"
                            ) as f:
                                f.write(response.content)
                            print(
                                f"{' ' * 5}└[{Y}•{RS}] {C}User Avatar{Y}:{RS} https://api.intigriti.com/file/api/file/{INTIGRITI_json.get('avatarId')} {R}[ {G}Downloaded Successfully!{RS} uosint/Result/media {R}]"
                            )
                        else:
                            print(
                                f"{' ' * 5}└[{Y}•{RS}] {C}User Avatar{Y}:{RS} No Photo Found For This User."
                            )
                    else:
                        print(
                            f"{' ' * 5}└[{Y}•{RS}] {C}User Avatar{Y}:{RS} No Photo Found For This User."
                        )

                    print(
                        f"{' ' * 5}└[{G}•{RS}] {C}User Reputation{Y}:{RS} {INTIGRITI_json.get('reputation')}"
                    )

                    print(
                        f"{' ' * 5}└[{P}•{RS}] {C}User Rank{Y}:{RS} {INTIGRITI_json.get('rank')}"
                    )

                    print(
                        f"{' ' * 5}└[{R}•{RS}] {C}User Streak{Y}:{RS} {INTIGRITI_json.get('streak')}"
                    )

                    print(
                        f"{' ' * 5}└[{B}•{RS}] {C}User StreakReputation{Y}:{RS} {INTIGRITI_json.get('streakReputation')}"
                    )

                    print(
                        f"{' ' * 5}└[{Y}•{RS}] {C}User Identity Checked{Y}:{RS} {INTIGRITI_json.get('identityChecked')}"
                    )

                    print(
                        f"{' ' * 5}└[{G}•{RS}] {C}User Id{Y}:{RS} {INTIGRITI_json.get('userId')}"
                    )

                    print(
                        f"{' ' * 5}└[{P}•{RS}] {C}User Country{Y}:{RS} {INTIGRITI_json.get('country')}"
                    )

                    print(
                        f"{' ' * 5}└[{R}•{RS}] {C}User Website{Y}:{RS} {INTIGRITI_json.get('website')}"
                    )

                    print(
                        f"{' ' * 5}└[{B}•{RS}] {C}User LinkedIn{Y}:{RS} {INTIGRITI_json.get('linkedIn')}"
                    )

                    print(
                        f"{' ' * 5}└[{Y}•{RS}] {C}User Twitter{Y}:{RS} {INTIGRITI_json.get('twitter')}"
                    )

                    print(
                        f"{' ' * 5}└[{G}•{RS}] {C}User Total Submissions{Y}:{RS} {INTIGRITI_json.get('totalSubmissions')}"
                    )

                    print(
                        f"{' ' * 5}└[{P}•{RS}] {C}User Accepted Submissions{Y}:{RS} {INTIGRITI_json.get('acceptedSubmissions')}"
                    )

                    print(
                        f"{' ' * 5}└[{R}•{RS}] {C}User Rejected Submissions{Y}:{RS} {INTIGRITI_json.get('rejectedSubmissions')}"
                    )

                    print(
                        f"{' ' * 5}└[{B}•{RS}] {C}User Valid Submission Ratio{Y}:{RS} {INTIGRITI_json.get('validSubmissionRatio')}"
                    )

                elif INTIGRITI_response.status_code == 404:

                    print(f"\n[{B} INTIGRITI{RS} ]")

                    print(
                        f"{' ' * 5}└[{R}•{RS}] {C}User Info{Y}:{RS} {R}Sorry, we couldn't find that one ❗️{RS}"
                    )

            else:
                print(f"\n[{B} INTIGRITI{RS} ]")

                print(
                    f"{' ' * 5}└[{R}•{RS}] {C}Connection Lost{Y}:{RS} {R}Oops! Unable To Establish A Connection{RS}"
                )
        except requests.exceptions.Timeout:
            print(f"\n[{B} INTIGRITI{RS} ]")

            print(
                f"{' ' * 5}└[{R}•{RS}] {C}Timeout Error{Y}:{RS} {R}Oops! Timed Out{RS}"
            )
    except socket.gaierror:
        print(f"\n[{B} INTIGRITI{RS} ]")

        print(
            f"{' ' * 5}└[{R}•{RS}] {C}DNS LookUp{Y}:{RS} {R}Oops! The {G}Dns Lookup{R} Failed And The Requested Domain Could Not Be Found.{RS}"
        )

    input(
        f"\n[{G} NOTE {RS}]{RS} USER {C}VPN{RS} TO SEARCH {R}USERNAME{RS} PORN SITE {B} PRESS ENTER {RS}"
    )

    # [ X VIDEOS ]

    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.33",
    }

    xvideos_Url = f"https://www.xvideos.com/profiles/{usernames}#_tabAboutMe"

    xvideos_Request = requests.request("GET", xvideos_Url, headers=headers)

    if xvideos_Request.status_code == 200:
        print(f"\n[{B} X VIDEOS{RS} ]")
        print(f"{' ' * 5}└[{R}•{RS}] {C}User Url{Y}:{RS} {xvideos_Url}")
        xvideos_Soup = BeautifulSoup(xvideos_Request.text, "html.parser")

        XVIDEO_USER_NAME = (
            xvideos_Soup.find("div", attrs={"id": "profile-title"})
            .find("h2")
            .find("strong")
        )
        XVIDEO_USER_Gender = xvideos_Soup.find(
            "div", attrs={"id": "pfinfo-col-col1"}
        ).find("p", attrs={"id": "pinfo-sex"})
        XVIDEO_USER_Age = xvideos_Soup.find(
            "div", attrs={"id": "pfinfo-col-col1"}
        ).find("p", attrs={"id": "pinfo-age"})
        XVIDEO_USER_Country = xvideos_Soup.find(
            "div", attrs={"id": "pfinfo-col-col1"}
        ).find("p", attrs={"id": "pinfo-country"})
        XVIDEO_USER_profile_hits = xvideos_Soup.find(
            "div", attrs={"id": "pfinfo-col-col1"}
        ).find("p", attrs={"id": "pinfo-profile-hits"})
        XVIDEO_USER_subscribers = xvideos_Soup.find(
            "div", attrs={"id": "pfinfo-col-col1"}
        ).find("p", attrs={"id": "pinfo-subscribers"})
        XVIDEO_USER_signedup = xvideos_Soup.find(
            "div", attrs={"id": "pfinfo-col-col1"}
        ).find("p", attrs={"id": "pinfo-signedup"})
        XVIDEO_USER_lastactivity = xvideos_Soup.find(
            "div", attrs={"id": "pfinfo-col-col1"}
        ).find("p", attrs={"id": "pinfo-lastactivity"})
        XVIDEO_USER_City = xvideos_Soup.find(
            "div", attrs={"id": "pfinfo-col-col1"}
        ).find("p", attrs={"id": "pinfo-city"})

        # Personal information

        XVIDEO_USER_languages = xvideos_Soup.find(
            "div", attrs={"id": "pfinfo-col-col1"}
        ).find("p", attrs={"id": "pinfo-languages"})
        XVIDEO_USER_seeking = xvideos_Soup.find(
            "div", attrs={"id": "pfinfo-col-col1"}
        ).find("p", attrs={"id": "pinfo-seeking"})
        XVIDEO_USER_relationship = xvideos_Soup.find(
            "div", attrs={"id": "pfinfo-col-col1"}
        ).find("p", attrs={"id": "pinfo-relationship"})
        XVIDEO_USER_kids = xvideos_Soup.find(
            "div", attrs={"id": "pfinfo-col-col1"}
        ).find("p", attrs={"id": "pinfo-kids"})
        XVIDEO_USER_education = xvideos_Soup.find(
            "div", attrs={"id": "pfinfo-col-col1"}
        ).find("p", attrs={"id": "pinfo-education"})
        XVIDEO_USER_religion = xvideos_Soup.find(
            "div", attrs={"id": "pfinfo-col-col1"}
        ).find("p", attrs={"id": "pinfo-religion"})
        XVIDEO_USER_smoking = xvideos_Soup.find(
            "div", attrs={"id": "pfinfo-col-col1"}
        ).find("p", attrs={"id": "pinfo-smoking"})
        XVIDEO_USER_drinking = xvideos_Soup.find(
            "div", attrs={"id": "pfinfo-col-col1"}
        ).find("p", attrs={"id": "pinfo-drinking"})

        # Physical Information

        XVIDEO_USER_ethnicity = xvideos_Soup.find(
            "div", attrs={"id": "pfinfo-col-col2"}
        ).find("p", attrs={"id": "pinfo-ethnicity"})
        XVIDEO_USER_body = xvideos_Soup.find(
            "div", attrs={"id": "pfinfo-col-col2"}
        ).find("p", attrs={"id": "pinfo-body"})
        XVIDEO_USER_height = xvideos_Soup.find(
            "div", attrs={"id": "pfinfo-col-col2"}
        ).find("p", attrs={"id": "pinfo-height"})
        XVIDEO_USER_weight = xvideos_Soup.find(
            "div", attrs={"id": "pfinfo-col-col2"}
        ).find("p", attrs={"id": "pinfo-weight"})
        XVIDEO_USER_hair_length = xvideos_Soup.find(
            "div", attrs={"id": "pfinfo-col-col2"}
        ).find("p", attrs={"id": "pinfo-hair_length"})
        XVIDEO_USER_hair_color = xvideos_Soup.find(
            "div", attrs={"id": "pfinfo-col-col2"}
        ).find("p", attrs={"id": "pinfo-hair_color"})
        XVIDEO_USER_eyes_color = xvideos_Soup.find(
            "div", attrs={"id": "pfinfo-col-col2"}
        ).find("p", attrs={"id": "pinfo-eyes_color"})

        XVIDEO_USER_tags = xvideos_Soup.find(
            "div", attrs={"id": "pfinfo-col-col2"}
        ).find("p", attrs={"id": "pinfo-tags"})
        XVIDEO_USER_aboutme = xvideos_Soup.find(
            "div", attrs={"id": "pfinfo-col-col2"}
        ).find("p", attrs={"id": "pinfo-aboutme"})

        if not XVIDEO_USER_NAME:
            print(
                f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {R}Not Found ❗️{RS} "
            )
        else:
            print(
                f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {XVIDEO_USER_NAME.string}"
            )

        if not XVIDEO_USER_Gender:
            print(f"{' ' * 5}└[{Y}•{RS}] {C}User Gender {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(
                f"{' ' * 5}└[{Y}•{RS}] {C}User Gender {Y}:{RS} {XVIDEO_USER_Gender.find('span').string}"
            )

        if not XVIDEO_USER_Age:
            print(f"{' ' * 5}└[{G}•{RS}] {C}User Age {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(
                f"{' ' * 5}└[{G}•{RS}] {C}User Age {Y}:{RS} {XVIDEO_USER_Age.find('span').string} "
            )

        if not XVIDEO_USER_Country:
            print(f"{' ' * 5}└[{G}•{RS}] {C}User Country {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(
                f"{' ' * 5}└[{G}•{RS}] {C}User Country {Y}:{RS} {XVIDEO_USER_Country.find('span').string}"
            )

        if not XVIDEO_USER_City:
            print(f"{' ' * 5}└[{R}•{RS}] {C}User City {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(
                f"{' ' * 5}└[{R}•{RS}] {C}User City {Y}:{RS} {XVIDEO_USER_City.find('span').string}"
            )

        if not XVIDEO_USER_profile_hits:
            print(
                f"{' ' * 5}└[{B}•{RS}] {C}User Profile Hits {Y}:{RS} {R}Not Found ❗️{RS} "
            )
        else:
            print(
                f"{' ' * 5}└[{B}•{RS}] {C}User Profile Hits {Y}:{RS} {XVIDEO_USER_profile_hits.find('span').string}"
            )

        if not XVIDEO_USER_subscribers:
            print(
                f"{' ' * 5}└[{Y}•{RS}] {C}User Subscribers {Y}:{RS} {R}Not Found ❗️{RS} "
            )
        else:
            print(
                f"{' ' * 5}└[{Y}•{RS}] {C}User Subscribers {Y}:{RS} {XVIDEO_USER_subscribers.find('span').string}"
            )

        if not XVIDEO_USER_signedup:
            print(
                f"{' ' * 5}└[{G}•{RS}] {C}User Signedup Date {Y}:{RS} {R}Not Found ❗️{RS} "
            )
        else:
            print(
                f"{' ' * 5}└[{G}•{RS}] {C}User Signedup Date {Y}:{RS} {XVIDEO_USER_signedup.find('span').string}"
            )

        if not XVIDEO_USER_lastactivity:
            print(
                f"{' ' * 5}└[{R}•{RS}] {C}User Last activity {Y}:{RS} {R}Not Found ❗️{RS} "
            )
        else:
            print(
                f"{' ' * 5}└[{R}•{RS}] {C}User Last activity {Y}:{RS} {XVIDEO_USER_lastactivity.find('span').string}"
            )

        if not XVIDEO_USER_languages:
            print(
                f"{' ' * 5}└[{B}•{RS}] {C}User Languages {Y}:{RS} {R}Not Found ❗️{RS} "
            )
        else:
            print(
                f"{' ' * 5}└[{B}•{RS}] {C}User Languages {Y}:{RS} {XVIDEO_USER_languages.find('span').string}"
            )

        print(
            f" \n {' ' * 5}[{G} NOTE {RS}] [ {Y}{C}Personal{Y}-{C}Information{RS} ] \n"
        )

        if not XVIDEO_USER_seeking:
            print(f"{' ' * 5}└[{Y}•{RS}] {C}User Seeking {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(
                f"{' ' * 5}└[{Y}•{RS}] {C}User Seeking {Y}:{RS} {XVIDEO_USER_seeking.find('span').string}"
            )

        if not XVIDEO_USER_relationship:
            print(
                f"{' ' * 5}└[{G}•{RS}] {C}User Relationship {Y}:{RS} {R}Not Found ❗️{RS} "
            )
        else:
            print(
                f"{' ' * 5}└[{G}•{RS}] {C}User Relationship {Y}:{RS} {XVIDEO_USER_relationship.find('span').string}"
            )

        if not XVIDEO_USER_kids:
            print(f"{' ' * 5}└[{R}•{RS}] {C}User Kids {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(
                f"{' ' * 5}└[{R}•{RS}] {C}User Kids {Y}:{RS} {XVIDEO_USER_kids.find('span').string}"
            )

        if not XVIDEO_USER_education:
            print(
                f"{' ' * 5}└[{B}•{RS}] {C}User Education {Y}:{RS} {R}Not Found ❗️{RS} "
            )
        else:
            print(
                f"{' ' * 5}└[{B}•{RS}] {C}User Education {Y}:{RS} {XVIDEO_USER_education.find('span').string}"
            )

        if not XVIDEO_USER_religion:
            print(
                f"{' ' * 5}└[{Y}•{RS}] {C}User Religion {Y}:{RS} {R}Not Found ❗️{RS} "
            )
        else:
            print(
                f"{' ' * 5}└[{Y}•{RS}] {C}User Religion {Y}:{RS} {XVIDEO_USER_religion.find('span').string}"
            )

        if not XVIDEO_USER_smoking:
            print(f"{' ' * 5}└[{G}•{RS}] {C}User Smoking {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(
                f"{' ' * 5}└[{G}•{RS}] {C}User Smoking {Y}:{RS} {XVIDEO_USER_smoking.find('span').string}"
            )

        if not XVIDEO_USER_drinking:
            print(
                f"{' ' * 5}└[{R}•{RS}] {C}User Drinking {Y}:{RS} {R}Not Found ❗️{RS} "
            )
        else:
            print(
                f"{' ' * 5}└[{R}•{RS}] {C}User Drinking {Y}:{RS} {XVIDEO_USER_drinking.find('span').string}"
            )

        print(
            f" \n {' ' * 5}[{G} NOTE {RS}] [ {Y}{C}Physical{Y}-{C}Information{RS} ] \n"
        )

        if not XVIDEO_USER_ethnicity:
            print(
                f"{' ' * 5}└[{R}•{RS}] {C}User Ethnicity {Y}:{RS} {R}Not Found ❗️{RS} "
            )
        else:
            print(
                f"{' ' * 5}└[{R}•{RS}] {C}User Ethnicity {Y}:{RS} {XVIDEO_USER_ethnicity.find('span').string}"
            )

        if not XVIDEO_USER_body:
            print(f"{' ' * 5}└[{B}•{RS}] {C}User Body {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(
                f"{' ' * 5}└[{B}•{RS}] {C}User Body {Y}:{RS} {XVIDEO_USER_body.find('span').string}"
            )

        if not XVIDEO_USER_height:
            print(f"{' ' * 5}└[{Y}•{RS}] {C}User Height {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(
                f"{' ' * 5}└[{Y}•{RS}] {C}User Height {Y}:{RS} {XVIDEO_USER_height.find('span').string}"
            )

        if not XVIDEO_USER_weight:
            print(f"{' ' * 5}└[{G}•{RS}] {C}User Weight {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(
                f"{' ' * 5}└[{G}•{RS}] {C}User Weight {Y}:{RS} {XVIDEO_USER_weight.find('span').string}"
            )

        if not XVIDEO_USER_hair_length:
            print(
                f"{' ' * 5}└[{R}•{RS}] {C}User Hair length {Y}:{RS} {R}Not Found ❗️{RS} "
            )
        else:
            print(
                f"{' ' * 5}└[{R}•{RS}] {C}User Hair length {Y}:{RS} {XVIDEO_USER_hair_length.find('span').string}"
            )

        if not XVIDEO_USER_hair_color:
            print(
                f"{' ' * 5}└[{B}•{RS}] {C}User Hair color {Y}:{RS} {R}Not Found ❗️{RS} "
            )
        else:
            print(
                f"{' ' * 5}└[{B}•{RS}] {C}User Hair color {Y}:{RS} {XVIDEO_USER_hair_color.find('span').string}"
            )

        if not XVIDEO_USER_eyes_color:
            print(
                f"{' ' * 5}└[{Y}•{RS}] {C}User Eyes color {Y}:{RS} {R}Not Found ❗️{RS} "
            )
        else:
            print(
                f"{' ' * 5}└[{Y}•{RS}] {C}User Eyes color {Y}:{RS} {XVIDEO_USER_eyes_color.find('span').string}"
            )

        if not XVIDEO_USER_tags:
            print(
                f"{' ' * 5}└[{R}•{RS}] {C}User Interests {Y}:{RS} {R}Not Found ❗️{RS} "
            )
        else:
            print(
                f"{' ' * 5}└[{R}•{RS}] {C}User Interests {Y}:{RS} {XVIDEO_USER_tags.find('span').string}"
            )

        if not XVIDEO_USER_aboutme:
            print(
                f"{' ' * 5}└[{B}•{RS}] {C}User About Me {Y}:{RS} {R}Not Found ❗️{RS} "
            )
        else:
            print(
                f"{' ' * 5}└[{B}•{RS}] {C}User About Me {Y}:{RS} {XVIDEO_USER_aboutme.getText()}"
            )

    elif xvideos_Request.status_code == 404:
        print(f"\n[{B} X VIDEOS{RS} ]")
        print(
            f"{' ' * 5}└[{R}•{RS}] {C}User Info{Y}:{RS} {R}Sorry, we couldn't find that one ❗️{RS}"
        )

    # [ X HAMSTER ]

    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.33",
    }

    XHAMSTER_Url = f"https://xhamster.com/users/{usernames}"

    XHAMSTER_Request = requests.request("GET", XHAMSTER_Url, headers=headers)

    if XHAMSTER_Request.status_code == 200:
        print(f"\n[{B} X HAMSTER{RS} ]")
        print(f"{' ' * 5}└[{R}•{RS}] {C}User Url{Y}:{RS} {XHAMSTER_Url}")
        XHAMSTER_Soup = BeautifulSoup(XHAMSTER_Request.text, "html.parser")

        # Personal information

        XHAMSTER_USER_NAME = XHAMSTER_Soup.find("div", attrs={"class": "user-name"})
        XHAMSTER_USER_IAM = (
            XHAMSTER_Soup.find("div", attrs={"class": "personal-info-block info-block"})
            .find("div", attrs={"class": "content-container"})
            .find("div", attrs={"class": "info-row i-am"})
        )
        XHAMSTER_USER_FROM = (
            XHAMSTER_Soup.find("div", attrs={"class": "personal-info-block info-block"})
            .find("div", attrs={"class": "content-container"})
            .find("div", attrs={"class": "info-row from"})
        )
        XHAMSTER_USER_seeking = (
            XHAMSTER_Soup.find("div", attrs={"class": "personal-info-block info-block"})
            .find("div", attrs={"class": "content-container"})
            .find("div", attrs={"class": "info-row seeking"})
        )
        XHAMSTER_USER_FETISHES = (
            XHAMSTER_Soup.find("div", attrs={"class": "personal-info-block info-block"})
            .find("div", attrs={"class": "content-container"})
            .find("div", attrs={"class": "info-row fetishes"})
        )
        XHAMSTER_USER_EDUCATION = (
            XHAMSTER_Soup.find("div", attrs={"class": "personal-info-block info-block"})
            .find("div", attrs={"class": "content-container"})
            .find("div", attrs={"class": "info-row education"})
        )
        XHAMSTER_USER_OCCUPATION = (
            XHAMSTER_Soup.find("div", attrs={"class": "personal-info-block info-block"})
            .find("div", attrs={"class": "content-container"})
            .find("div", attrs={"class": "info-row occupation"})
        )
        XHAMSTER_USER_INCOME = (
            XHAMSTER_Soup.find("div", attrs={"class": "personal-info-block info-block"})
            .find("div", attrs={"class": "content-container"})
            .find("div", attrs={"class": "info-row income"})
        )
        XHAMSTER_USER_RELATIONS = (
            XHAMSTER_Soup.find("div", attrs={"class": "personal-info-block info-block"})
            .find("div", attrs={"class": "content-container"})
            .find("div", attrs={"class": "info-row relations"})
        )
        XHAMSTER_USER_kids = (
            XHAMSTER_Soup.find("div", attrs={"class": "personal-info-block info-block"})
            .find("div", attrs={"class": "content-container"})
            .find("div", attrs={"class": "info-row kids"})
        )
        XHAMSTER_USER_religion = (
            XHAMSTER_Soup.find("div", attrs={"class": "personal-info-block info-block"})
            .find("div", attrs={"class": "content-container"})
            .find("div", attrs={"class": "info-row religion"})
        )
        XHAMSTER_USER_smoking = (
            XHAMSTER_Soup.find("div", attrs={"class": "personal-info-block info-block"})
            .find("div", attrs={"class": "content-container"})
            .find("div", attrs={"class": "info-row smoking"})
        )
        XHAMSTER_USER_alcohol = (
            XHAMSTER_Soup.find("div", attrs={"class": "personal-info-block info-block"})
            .find("div", attrs={"class": "content-container"})
            .find("div", attrs={"class": "info-row alcohol"})
        )
        XHAMSTER_USER_drugs = (
            XHAMSTER_Soup.find("div", attrs={"class": "personal-info-block info-block"})
            .find("div", attrs={"class": "content-container"})
            .find("div", attrs={"class": "info-row drugs"})
        )
        XHAMSTER_USER_star_sign = (
            XHAMSTER_Soup.find("div", attrs={"class": "personal-info-block info-block"})
            .find("div", attrs={"class": "content-container"})
            .find("div", attrs={"class": "info-row star_sign"})
        )
        XHAMSTER_USER_star_ethnicity = (
            XHAMSTER_Soup.find("div", attrs={"class": "personal-info-block info-block"})
            .find("div", attrs={"class": "content-container"})
            .find("div", attrs={"class": "info-row ethnicity"})
        )
        XHAMSTER_USER_star_body = (
            XHAMSTER_Soup.find("div", attrs={"class": "personal-info-block info-block"})
            .find("div", attrs={"class": "content-container"})
            .find("div", attrs={"class": "info-row body"})
        )
        XHAMSTER_USER_star_hairLength = (
            XHAMSTER_Soup.find("div", attrs={"class": "personal-info-block info-block"})
            .find("div", attrs={"class": "content-container"})
            .find("div", attrs={"class": "info-row hairLength"})
        )
        XHAMSTER_USER_star_eyeColor = (
            XHAMSTER_Soup.find("div", attrs={"class": "personal-info-block info-block"})
            .find("div", attrs={"class": "content-container"})
            .find("div", attrs={"class": "info-row eyeColor"})
        )
        XHAMSTER_USER_star_height = (
            XHAMSTER_Soup.find("div", attrs={"class": "personal-info-block info-block"})
            .find("div", attrs={"class": "content-container"})
            .find("div", attrs={"class": "info-row height"})
        )
        XHAMSTER_USER_Profile_subscribers_comments_etc = XHAMSTER_Soup.find_all(
            "div", attrs={"class": "details-row"}
        )

        if not XHAMSTER_USER_NAME:
            print(
                f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {R}Not Found ❗️{RS} "
            )
        else:
            print(
                f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {XHAMSTER_USER_NAME.find('div', attrs={'class': 'value'}).string}"
            )

        if not XHAMSTER_USER_Profile_subscribers_comments_etc:
            print(f"{' ' * 5}└[{Y}•{RS}] {C}User Rank {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            space_remove = XHAMSTER_USER_Profile_subscribers_comments_etc[1].getText()
            After_remove_space = space_remove.strip()
            print(f"{' ' * 5}└[{Y}•{RS}] {C}User Rank {Y}:{RS} {After_remove_space}")

        if not XHAMSTER_USER_Profile_subscribers_comments_etc:
            print(
                f"{' ' * 5}└[{G}•{RS}] {C}User Registration Date {Y}:{RS} {R}Not Found ❗️{RS} "
            )
        else:
            space_remove = XHAMSTER_USER_Profile_subscribers_comments_etc[2].getText()
            After_remove_space = space_remove.strip()
            print(
                f"{' ' * 5}└[{G}•{RS}] {C}User Registration Date {Y}:{RS} {After_remove_space}"
            )

        if not XHAMSTER_USER_Profile_subscribers_comments_etc:
            print(f"{' ' * 5}└[{R}•{RS}] {C}User View {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            space_remove = XHAMSTER_USER_Profile_subscribers_comments_etc[3].getText()
            After_remove_space = space_remove.strip()
            print(f"{' ' * 5}└[{R}•{RS}] {C}User View {Y}:{RS} {After_remove_space}")

        if not XHAMSTER_USER_Profile_subscribers_comments_etc:
            print(
                f"{' ' * 5}└[{B}•{RS}] {C}User Subscribers {Y}:{RS} {R}Not Found ❗️{RS} "
            )
        else:
            space_remove = XHAMSTER_USER_Profile_subscribers_comments_etc[4].getText()
            After_remove_space = space_remove.strip()
            print(
                f"{' ' * 5}└[{B}•{RS}] {C}User Subscribers {Y}:{RS} {After_remove_space}"
            )

        if not XHAMSTER_USER_Profile_subscribers_comments_etc:
            print(
                f"{' ' * 5}└[{Y}•{RS}] {C}User Comments {Y}:{RS} {R}Not Found ❗️{RS} "
            )
        else:
            space_remove = XHAMSTER_USER_Profile_subscribers_comments_etc[5].getText()
            After_remove_space = space_remove.strip()
            print(
                f"{' ' * 5}└[{Y}•{RS}] {C}User Comments {Y}:{RS} {After_remove_space}"
            )

        print(
            f" \n {' ' * 5}[{G} NOTE {RS}] [ {Y}{C}Personal{Y}-{C}Information{RS} ] \n"
        )

        if not XHAMSTER_USER_IAM:
            print(f"{' ' * 5}└[{Y}•{RS}] {C}User I am {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(
                f"{' ' * 5}└[{Y}•{RS}] {C}User I am {Y}:{RS} {XHAMSTER_USER_IAM.find('div', attrs={'class': 'value'}).getText()}"
            )

        if not XHAMSTER_USER_FROM:
            print(f"{' ' * 5}└[{G}•{RS}] {C}User From {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(
                f"{' ' * 5}└[{G}•{RS}] {C}User From {Y}:{RS} {XHAMSTER_USER_FROM.find('div', attrs={'class': 'value'}).getText()}"
            )

        if not XHAMSTER_USER_seeking:
            print(f"{' ' * 5}└[{R}•{RS}] {C}User Seeking {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            seeking_space_remove = XHAMSTER_USER_seeking.find(
                "div", attrs={"class": "value"}
            ).getText()
            After_remove_seeking_space = seeking_space_remove.strip()
            print(
                f"{' ' * 5}└[{R}•{RS}] {C}User Seeking {Y}:{RS} {After_remove_seeking_space}"
            )

        if not XHAMSTER_USER_FETISHES:
            print(
                f"{' ' * 5}└[{B}•{RS}] {C}User Fetishes {Y}:{RS} {R}Not Found ❗️{RS} "
            )
        else:
            print(
                f"{' ' * 5}└[{B}•{RS}] {C}User Fetishes {Y}:{RS} {XHAMSTER_USER_FETISHES.find('div', attrs={'class': 'value'}).getText()}"
            )

        if not XHAMSTER_USER_EDUCATION:
            print(
                f"{' ' * 5}└[{Y}•{RS}] {C}User Education {Y}:{RS} {R}Not Found ❗️{RS} "
            )
        else:
            EDUCATION_space_remove = XHAMSTER_USER_EDUCATION.find(
                "div", attrs={"class": "value"}
            ).getText()
            After_remove_EDUCATION_space = EDUCATION_space_remove.strip()
            print(
                f"{' ' * 5}└[{Y}•{RS}] {C}User Education {Y}:{RS} {After_remove_EDUCATION_space}"
            )

        if not XHAMSTER_USER_OCCUPATION:
            print(
                f"{' ' * 5}└[{G}•{RS}] {C}User Occupation {Y}:{RS} {R}Not Found ❗️{RS} "
            )
        else:
            OCCUPATION_space_remove = XHAMSTER_USER_OCCUPATION.find(
                "div", attrs={"class": "value"}
            ).getText()
            After_remove_OCCUPATION_space = OCCUPATION_space_remove.strip()
            print(
                f"{' ' * 5}└[{G}•{RS}] {C}User Occupation {Y}:{RS} {After_remove_OCCUPATION_space}"
            )

        if not XHAMSTER_USER_INCOME:
            print(f"{' ' * 5}└[{R}•{RS}] {C}User Income {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            space_remove = XHAMSTER_USER_INCOME.find(
                "div", attrs={"class": "value"}
            ).getText()
            After_remove_space = space_remove.strip()
            print(f"{' ' * 5}└[{R}•{RS}] {C}User Income {Y}:{RS} {After_remove_space}")

        if not XHAMSTER_USER_RELATIONS:
            print(
                f"{' ' * 5}└[{B}•{RS}] {C}User Relationship {Y}:{RS} {R}Not Found ❗️{RS} "
            )
        else:
            space_remove = XHAMSTER_USER_RELATIONS.find(
                "div", attrs={"class": "value"}
            ).getText()
            After_remove_space = space_remove.strip()
            print(
                f"{' ' * 5}└[{B}•{RS}] {C}User Relationship {Y}:{RS} {After_remove_space}"
            )

        if not XHAMSTER_USER_kids:
            print(f"{' ' * 5}└[{Y}•{RS}] {C}User Kids {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            space_remove = XHAMSTER_USER_kids.find(
                "div", attrs={"class": "value"}
            ).getText()
            After_remove_space = space_remove.strip()
            print(f"{' ' * 5}└[{Y}•{RS}] {C}User Kids {Y}:{RS} {After_remove_space}")

        if not XHAMSTER_USER_religion:
            print(
                f"{' ' * 5}└[{G}•{RS}] {C}User Religion {Y}:{RS} {R}Not Found ❗️{RS} "
            )
        else:
            space_remove = XHAMSTER_USER_religion.find(
                "div", attrs={"class": "value"}
            ).getText()
            After_remove_space = space_remove.strip()
            print(
                f"{' ' * 5}└[{G}•{RS}] {C}User Religion {Y}:{RS} {After_remove_space}"
            )

        if not XHAMSTER_USER_smoking:
            print(f"{' ' * 5}└[{R}•{RS}] {C}User Smoking {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            space_remove = XHAMSTER_USER_smoking.find(
                "div", attrs={"class": "value"}
            ).getText()
            After_remove_space = space_remove.strip()
            print(f"{' ' * 5}└[{R}•{RS}] {C}User Smoking {Y}:{RS} {After_remove_space}")

        if not XHAMSTER_USER_alcohol:
            print(
                f"{' ' * 5}└[{B}•{RS}] {C}User Drinking {Y}:{RS} {R}Not Found ❗️{RS} "
            )
        else:
            space_remove = XHAMSTER_USER_alcohol.find(
                "div", attrs={"class": "value"}
            ).getText()
            After_remove_space = space_remove.strip()
            print(
                f"{' ' * 5}└[{B}•{RS}] {C}User Drinking {Y}:{RS} {After_remove_space}"
            )

        if not XHAMSTER_USER_drugs:
            print(f"{' ' * 5}└[{Y}•{RS}] {C}User Drugs {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            space_remove = XHAMSTER_USER_drugs.find(
                "div", attrs={"class": "value"}
            ).getText()
            After_remove_space = space_remove.strip()
            print(f"{' ' * 5}└[{Y}•{RS}] {C}User Drugs {Y}:{RS} {After_remove_space}")

        if not XHAMSTER_USER_star_sign:
            print(
                f"{' ' * 5}└[{G}•{RS}] {C}User Star Sign {Y}:{RS} {R}Not Found ❗️{RS} "
            )
        else:
            space_remove = XHAMSTER_USER_star_sign.find(
                "div", attrs={"class": "value"}
            ).getText()
            After_remove_space = space_remove.strip()
            print(
                f"{' ' * 5}└[{G}•{RS}] {C}User Star Sign {Y}:{RS} {After_remove_space}"
            )

        # What I look like

        print(f" \n {' ' * 5}[{G} NOTE {RS}] [ {Y}{C}What I Look Like{RS} ] \n")

        if not XHAMSTER_USER_star_ethnicity:
            print(
                f"{' ' * 5}└[{R}•{RS}] {C}User Ethnicity {Y}:{RS} {R}Not Found ❗️{RS} "
            )
        else:
            space_remove = XHAMSTER_USER_star_ethnicity.find(
                "div", attrs={"class": "value"}
            ).getText()
            After_remove_space = space_remove.strip()
            print(
                f"{' ' * 5}└[{R}•{RS}] {C}User Ethnicity {Y}:{RS} {After_remove_space}"
            )

        if not XHAMSTER_USER_star_body:
            print(f"{' ' * 5}└[{B}•{RS}] {C}User Body {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            space_remove = XHAMSTER_USER_star_body.find(
                "div", attrs={"class": "value"}
            ).getText()
            After_remove_space = space_remove.strip()
            print(f"{' ' * 5}└[{B}•{RS}] {C}User Body {Y}:{RS} {After_remove_space}")

        if not XHAMSTER_USER_star_hairLength:
            print(
                f"{' ' * 5}└[{Y}•{RS}] {C}User Hair length {Y}:{RS} {R}Not Found ❗️{RS} "
            )
        else:
            space_remove = XHAMSTER_USER_star_hairLength.find(
                "div", attrs={"class": "value"}
            ).getText()
            After_remove_space = space_remove.strip()
            print(
                f"{' ' * 5}└[{Y}•{RS}] {C}User Hair length {Y}:{RS} {After_remove_space}"
            )

        if not XHAMSTER_USER_star_eyeColor:
            print(
                f"{' ' * 5}└[{G}•{RS}] {C}User Eye Color {Y}:{RS} {R}Not Found ❗️{RS} "
            )
        else:
            space_remove = XHAMSTER_USER_star_eyeColor.find(
                "div", attrs={"class": "value"}
            ).getText()
            After_remove_space = space_remove.strip()
            print(
                f"{' ' * 5}└[{G}•{RS}] {C}User Eye Color {Y}:{RS} {After_remove_space}"
            )

        if not XHAMSTER_USER_star_height:
            print(f"{' ' * 5}└[{R}•{RS}] {C}User Height {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            space_remove = XHAMSTER_USER_star_height.find(
                "div", attrs={"class": "value"}
            ).getText()
            After_remove_space = space_remove.strip()
            print(f"{' ' * 5}└[{R}•{RS}] {C}User Height {Y}:{RS} {After_remove_space}")

    elif XHAMSTER_Request.status_code == 404:
        print(f"\n[{B} X HAMSTER{RS} ]")
        print(
            f"{' ' * 5}└[{R}•{RS}] {C}User Info{Y}:{RS} {R}Sorry, we couldn't find that one ❗️{RS}"
        )
