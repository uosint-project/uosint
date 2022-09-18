import requests, time, json, os, urllib3
from requests.structures import CaseInsensitiveDict
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from bs4 import BeautifulSoup
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
C = '\033[36m'
BL = '\033[1m'


def Username_input(usernames):

    today = date.today()
    Today_Date = today.strftime("%B %d, %Y")
    print(f"""
     {B}_  _ {R}____ ____ _ _  _ ___ {RS}
     {B}|  | {R}|  | [__  | |\ |  |  {RS}
     {B}|__| {R}|__| ___] | | \|  |  {RS}

     Github {Y}:{RS} https://github.com/naimkowshik 
     {B}NOW {Y}:{RS} {Today_Date}  {B}Version {Y}:{C} 1{Y}.{C}0{RS}
     {B}Status {Y}:{RS} This Tool Is Still In Development Mode 〽️
    """)

    Facebook_Url = f"https://www.facebook.com/{usernames}"

    Facebook_Request = requests.get(Facebook_Url)

    if Facebook_Request.status_code == 200:

        print(f"\n[{B} FACEBOOK{RS} ]")

        print(f"{' ' * 5}└[{R}•{RS}] {C}User Url {Y}:{RS} {Facebook_Url}")

        Facebook_Soup = BeautifulSoup(Facebook_Request.text, "html.parser")

        full_name_tag = Facebook_Soup.find_all('title')

        for FULL_NAME in full_name_tag:
            print(f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {FULL_NAME.string}")


    elif Facebook_Request.status_code == 404:
        print(f"[{B} FACEBOOK{RS} ]")
        print(f"{' ' * 5}└[{R}•{RS}] {C}User Info {Y}:{RS} {R}Not Found ❗️{RS} ")

    # [ Twitter ]

    Twitter_Url = f"https://nitter.net/{usernames}"

    Twitter_Request = requests.request("GET", Twitter_Url)

    if Twitter_Request.status_code == 200:
        print(f"\n[{B} TWITTER{RS} ]")

        Twitter_Soup = BeautifulSoup(Twitter_Request.text, "html.parser")

        full_name_tag = Twitter_Soup.find_all(class_="profile-card-fullname")
        username_tag = Twitter_Soup.find_all(class_="profile-card-username")
        User_Bio_tag = Twitter_Soup.find_all(class_="profile-bio")
        User_Joined_tag = Twitter_Soup.find_all(class_="profile-joindate")
        Tweets_Following_Followers_Likes_tag = Twitter_Soup.find_all(class_="profile-stat-num")
        User_Location = Twitter_Soup.find_all(class_="profile-location")
        User_Website_tag = Twitter_Soup.find_all(class_="profile-website")
        title = Twitter_Soup.find_all(span_="title")
        verified_twitter = Twitter_Soup.find_all(class_='icon-ok verified-icon')
        suspended_twitters = Twitter_Soup.find_all(class_='error-panel')

        if (not suspended_twitters):

            print(f"{' ' * 5}└[{R}•{RS}] {C}User Url{Y}:{RS} {f'https://twitter.com/{usernames}'}")

            if (not full_name_tag):
                print(f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {R}Not Found ❌ {RS}")
            else:
                print(f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name  {Y}:{RS} {full_name_tag[0].getText()}")

            if (not username_tag):
                print(f"{' ' * 5}└[{Y}•{RS}] {C}UserName {Y}:{RS} {R}Not Found ❌ {RS}")
            else:
                print(f"{' ' * 5}└[{Y}•{RS}] {C}UserName {Y}:{RS} {username_tag[0].getText()}")

            if (not User_Joined_tag):
                print(f"{' ' * 5}└[{G}•{RS}] {C}User Joined {Y}:{RS} {R}Not Found ❌ {RS}")
            else:
                print(f"{' ' * 5}└[{G}•{RS}] {C}User Joined {Y}:{RS} {User_Joined_tag[0].getText()}")

            if (not Tweets_Following_Followers_Likes_tag):
                print(f"{' ' * 5}└[{R}•{RS}] {C}User Tweets {Y}:{RS} {R}Not Found ❌ {RS}")
            else:
                print(
                    f"{' ' * 5}└[{R}•{RS}] {C}User Tweets {Y}:{RS} {Tweets_Following_Followers_Likes_tag[0].getText()}")

            if (not Tweets_Following_Followers_Likes_tag):
                print(f"{' ' * 5}└[{B}•{RS}] {C}User Following {Y}:{RS} {R}Not Found ❌ {RS}")
            else:
                print(
                    f"{' ' * 5}└[{B}•{RS}] {C}User Following {Y}:{RS} {Tweets_Following_Followers_Likes_tag[1].getText()}")

            if (not Tweets_Following_Followers_Likes_tag):
                print(f"{' ' * 5}└[{Y}•{RS}] {C}User Followers {Y}:{RS} {R}Not Found ❌ {RS}")
            else:
                print(
                    f"{' ' * 5}└[{Y}•{RS}] {C}User Followers {Y}:{RS} {Tweets_Following_Followers_Likes_tag[2].getText()}")

            if (not Tweets_Following_Followers_Likes_tag):
                print(f"{' ' * 5}└[{Y}•{RS}] {C}User Likes {Y}:{RS} {R}Not Found ❌ {RS}")
            else:
                print(
                    f"{' ' * 5}└[{Y}•{RS}] {C}User Likes {Y}:{RS} {Tweets_Following_Followers_Likes_tag[3].getText()}")

            if (not User_Bio_tag):
                print(f"{' ' * 5}└[{R}•{RS}] {C}User Bio {Y}:{RS} {R}Not Found ❌ {RS}")
            else:
                print(f"{' ' * 5}└[{R}•{RS}] {C}User Bio {Y}:{RS} {User_Bio_tag[0].getText()}")

            print(f"{' ' * 5}└[{B}•{RS}] {C}User Suspended {Y}:{RS} [ {G}LIVE{RS} ] {RS}")
        else:
            print(f"{' ' * 5}└[{R}•{RS}] {C}User Suspended {Y}:{RS} {suspended_twitters[0].getText()}")


    elif Twitter_Request.status_code == 404:
        print(f"\n[{B} TWITTER{RS} ]")
        print(f"{' ' * 5}└[{R}•{RS}] {C}User Info {Y}:{RS} {R}Not Found ❗️{RS}")

    # [ pinterest ]

    pinterest_Url = f"https://www.pinterest.com/{usernames}"

    pinterest_Request = requests.request("GET", pinterest_Url)

    if pinterest_Request.status_code == 200:
        print(f"\n[{B} PINTEREST{RS} ]")
        print(f"{' ' * 5}└[{R}•{RS}] {C}User Url{Y}:{RS} {pinterest_Url}")
        Pinterest_Soup = BeautifulSoup(pinterest_Request.text, "html.parser")
        full_name_Pinterest_tag = Pinterest_Soup.find_all(class_="FNs zI7 iyn Hsu")
        Follower_Pinterest_tag = Pinterest_Soup.find_all(class_="tBJ dyH iFc sAJ O2T zDA IZT mWe")

        if (not full_name_Pinterest_tag):
            print(f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {R}Not Found ❌ {RS}")
        else:
            print(f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {full_name_Pinterest_tag[0].getText()}")

    elif pinterest_Request.status_code == 404:
        print(f"\n[{B} PINTEREST{RS} ]")
        print(f"{' ' * 5}└[{R}•{RS}] {C}User Info{Y}:{RS} {R}Not Found ❗️{RS}")

    # [ YouTube ]

    YouTube_Url = f"https://www.youtube.com/user/{usernames}"

    YouTube_Request = requests.request("GET", YouTube_Url)

    if YouTube_Request.status_code == 200:
        print(f"\n[{B} YouTube{RS} ]")
        print(f"{' ' * 5}└[{R}•{RS}] {C}User Url{Y}:{RS} {YouTube_Url}")

        YouTube_Soup = BeautifulSoup(YouTube_Request.text, "html.parser")

        full_name_YouTube_tag = YouTube_Soup.find_all("title")

        if (not full_name_YouTube_tag):
            print(f"{' ' * 5}└[{B}•{RS}] {C}User Name {Y}:{RS} {R}Not Found ❌ {RS}")
        else:
            print(f"{' ' * 5}└[{B}•{RS}] {C}User Name {Y}:{RS} {full_name_YouTube_tag[0].getText()}")

    elif YouTube_Request.status_code == 404:
        print(f"\n[{B} YouTube{RS} ]")
        print(f"{' ' * 5}└[{R}•{RS}] {C}User Info{Y}:{RS} {R}Not Found ❗️{RS}")

    # [ VIMEO ]

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.33',
    }

    VIMEO_Url = f"https://vimeo.com/{usernames}"

    VIMEO_Request = requests.get(VIMEO_Url, headers=headers)

    if VIMEO_Request.status_code == 200:
        print(f"\n[{B} VIMEO{RS} ]")

        print(f"{' ' * 5}└[{R}•{RS}] {C}User Url {Y}:{RS} {VIMEO_Url}")

        VIMEO_Url = f"https://vimeo.com/{usernames}/collections"

        VIMEO_Requestss = requests.get(VIMEO_Url, headers=headers)

        VIMEO_Soupssss = BeautifulSoup(VIMEO_Requestss.text, "html.parser")

        all = VIMEO_Soupssss.find_all('p', class_="super_link_list_title")

        VIMEO_SOups = BeautifulSoup(VIMEO_Request.text, "html.parser")

        VIMEO_Url = f"https://vimeo.com/{usernames}/following/followers/sort:date"

        VIMEO_Requests = requests.get(VIMEO_Url, headers=headers)

        VIMEO_Soups = BeautifulSoup(VIMEO_Requests.text, "html.parser")

        Following_Followers = VIMEO_Soups.find_all('div', class_="js-tabs tab_bar")

        Following_Followers = Following_Followers[0].getText()
        Following_Followers_result = Following_Followers.strip()

        VIMEO_Soup = BeautifulSoup(VIMEO_Request.text, "html.parser")

        name_PERISCOPE = VIMEO_Soup.find('meta', property="og:title")

        Description_PERISCOPE = VIMEO_Soup.find('meta', property="og:description")

        print(f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {name_PERISCOPE['content']}")
        print(f"{' ' * 5}└[{Y}•{RS}] {C}User Description {Y}:{RS} {Description_PERISCOPE['content']}")

    if VIMEO_Request.status_code == 404:
        print(f"\n[{B} VIMEO{RS} ]")
        print(f"{' ' * 5}└[{R}•{RS}] {C}User Info {Y}:{RS} {R}Not Found ❗️{RS} ")

    # [ DAILYMOTION ]

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.33',
    }

    dailymotion_Url = f"https://www.dailymotion.com/{usernames}"

    dailymotion_Request = requests.request("GET", dailymotion_Url, headers=headers)

    if dailymotion_Request.status_code == 200:
        print(f"\n[{B} DAILYMOTION{RS} ]")
        print(f"{' ' * 5}└[{R}•{RS}] {C}User Url{Y}:{RS} {dailymotion_Url}")
        dailymotion_Soup = BeautifulSoup(dailymotion_Request.text, "html.parser")
        full_name_DAILYMOTION_tag = dailymotion_Soup.find_all("title")
        print(f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {full_name_DAILYMOTION_tag[0].getText()}")

    elif dailymotion_Request.status_code == 404:
        print(f"\n[{B} DAILYMOTION{RS} ]")
        print(f"{' ' * 5}└[{R}•{RS}] {C}User Info{Y}:{RS} {R}Not Found ❗️{RS}")

    # [ Caffeine_TV ]

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.33',
    }

    url = f"https://api.caffeine.tv/v1/users/{usernames}"

    Caffeine_TV_Request = requests.request("GET", url, headers=headers)

    if Caffeine_TV_Request.status_code == 200:
        Caffeine_TV_Data = json.loads(Caffeine_TV_Request.content)
        print(f"\n[{B} CAFFEINE_TV{RS} ]")
        print(f"{' ' * 5}└[{R}•{RS}] {C}User Url {Y}:{RS} {f'https://www.caffeine.tv/{usernames}/profile'}")
        print(f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {Caffeine_TV_Data['user']['name']}")
        print(f"{' ' * 5}└[{Y}•{RS}] {C}UserName {Y}:{RS} {Caffeine_TV_Data['user']['username']}")
        print(f"{' ' * 5}└[{G}•{RS}] {C}User Following {Y}:{RS} {Caffeine_TV_Data['user']['following_count']}")
        print(f"{' ' * 5}└[{R}•{RS}] {C}User Followers {Y}:{RS} {Caffeine_TV_Data['user']['followers_count']}")
        print(f"{' ' * 5}└[{B}•{RS}] {C}User Badge {Y}:{RS} {Caffeine_TV_Data['user']['badge']}")

    elif Caffeine_TV_Request.status_code == 404:
        print(f"\n[{B} CAFFEINE_TV{RS} ]")
        print(f"{' ' * 5}└[{R}•{RS}] {C}User Info{Y}:{RS} {R}Not Found ❗️{RS}")

    # [ GITHUB ]

    Github_Url = f"https://github.com/{usernames}"

    Github_Request = requests.get(Github_Url)

    if Github_Request.status_code == 200:

        print(f"\n[{B} GITHUB{RS} ]")

        print(f"{' ' * 5}└[{R}•{RS}] {C}User Url {Y}:{RS} {Github_Url}")

        Github_Soup = BeautifulSoup(Github_Request.text, "html.parser")

        full_name_Github_tag = Github_Soup.find_all(class_="p-name vcard-fullname d-block overflow-hidden")
        user_name_Github_tag = Github_Soup.find_all(class_="p-nickname vcard-username d-block")
        user_bio_Github_tag = Github_Soup.find_all(class_="p-note user-profile-bio mb-3 js-user-profile-bio f4")
        user_followers_Github_tag = Github_Soup.find_all(class_="text-bold color-fg-default")
        user_following_Github_tag = Github_Soup.find_all(class_="text-bold color-fg-default")
        user_workfrom_organization_Github_tag = Github_Soup.find_all(class_="p-org")
        user_location_Github_tag = Github_Soup.find_all(class_="p-label")

        # USer Full Name
        if (not full_name_Github_tag):
            print(f"{' ' * 5}└[{B}•{RS}] {C}User FullName {Y}:{RS} {R}Not Found ❌ {RS}")
        else:
            def remove(string):
                return string.replace("""
              """, "")

            string = full_name_Github_tag[0].getText()
            print(f"{' ' * 5}└[{B}•{RS}] {C}User FullName {Y}:{RS} {remove(string)}")

        # User Followers
        if (not user_followers_Github_tag):
            print(f"{' ' * 5}└[{Y}•{RS}] {C}User Followers {Y}:{RS} {R}Not Found ❌ {RS}")
        else:
            def remove(string):
                return string.replace("""
              """, " ")

            string = user_followers_Github_tag[0].getText()
            print(f"{' ' * 5}└[{Y}•{RS}] {C}User Followers {Y}:{RS} {remove(string)}")

        # User Following
        if (not user_following_Github_tag):
            print(f"{' ' * 5}└[{G}•{RS}] {C}User Following {Y}:{RS} {R}Not Found ❌ {RS}")
        else:
            def remove(string):
                return string.replace("""
              """, "        ")

            string = user_following_Github_tag[1].getText()
            print(f"{' ' * 5}└[{G}•{RS}] {C}User Following {Y}:{RS} {remove(string)}")

        # User location
        if (not user_location_Github_tag):
            print(f"{' ' * 5}└[{R}•{RS}] {C}User Location {Y}:{RS} {R}Not Found ❌ {RS}")
        else:
            def remove(string):
                return string.replace("""
              """, "        ")

            string = user_location_Github_tag[0].getText()
            print(f"{' ' * 5}└[{R}•{RS}] {C}User Location {Y}:{RS} {remove(string)}")

        # User Working From
        if (not user_workfrom_organization_Github_tag):
            print(f"{' ' * 5}└[{B}•{RS}] {C}User Work Organization {Y}:{RS} {R}Not Found ❌ {RS}")
        else:
            def remove(string):
                return string.replace("""
              """, "        ")

            string = user_workfrom_organization_Github_tag[0].getText()
            print(f"{' ' * 5}└[{B}•{RS}] {C}User Work Organization {Y}:{RS} {remove(string)}")

        # User BIO
        if (not user_bio_Github_tag):
            print(f"{' ' * 5}└[{Y}•{RS}] {C}User Bio {Y}:{RS} {R}Not Found ❌ {RS}")
        else:
            def remove(string):
                return string.replace("""
              """, "        ")

            string = user_bio_Github_tag[0].getText()
            print(f"{' ' * 5}└[{Y}•{RS}] {C}User Bio {Y}:{RS} {remove(string)}")


    elif Github_Request.status_code == 404:
        print(f"\n[{B} GITHUB{RS} ]")
        print(f"{' ' * 5}└[{R}•{RS}] {C}User Info{Y}:{RS} {R}Not Found ❗️{RS}")

    # [ replit ]

    replit_Url = f"https://replit.com/@{usernames}"

    Replit_Request = requests.request("GET", replit_Url)

    if Replit_Request.status_code == 200:
        print(f"\n[{B} REPLIT{RS} ]")
        print(f"{' ' * 5}└[{R}•{RS}] {C}User Url{Y}:{RS} {replit_Url}")
        Replit_Soup = BeautifulSoup(Replit_Request.text, "html.parser")
        full_name_Replit_tag = Replit_Soup.find_all("title")
        print(f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {full_name_Replit_tag[0].getText()}")

    elif Replit_Request.status_code == 404:
        print(f"\n[{B} REPLIT{RS} ]")
        print(f"{' ' * 5}└[{R}•{RS}] {C}User Info{Y}:{RS} {R}Not Found ❗️{RS}")

    # [ Talegram ]

    Telegram_Bot_Url = f"https://t.me/{usernames}_bot"

    Telegram_Request = requests.get(Telegram_Bot_Url)

    if Telegram_Request.status_code == 200:

        print(f"\n[{B} TELEGRAM{RS} ]")

        print(f"{' ' * 5}└[{G} BOT {RS}]")

        print(f"{' ' * 8}└[{R}•{RS}]{C}User Url {Y}:{RS} {Telegram_Bot_Url}")

        Telegram_Soup = BeautifulSoup(Telegram_Request.text, "html.parser")

        BOT_full_name_tag = Telegram_Soup.find_all('span', attrs={'dir': 'auto'})

        for FULL_NAME in BOT_full_name_tag:
            print(f"{' ' * 8}└[{B}•{RS}] {C}BOT Name {Y}:{RS} {FULL_NAME.string}")
        full_name_tag = Telegram_Soup.find_all(class_="tgme_page_description")
        if (full_name_tag):
            def remove(string):
                return string.replace("""
      """, "")

            string = full_name_tag[0].getText()
            print(f"{' ' * 8}└[{Y}•{RS}] {C}User Description {Y}:{RS} {remove(string)}")
            print(
                f"{' ' * 5}[{G} NOTE {RS}] [ {C}USER DESCRIPTION{RS} {Y}MEANS {G}NOT SURE THIS USER {R}EXISTS{RS} OR {R}NOT{RS} ] \n")

    elif Telegram_Request.status_code == 404:
        print(f"\n└── {B}Telegram {R}✖{RS}")
        print(f"{' ' * 5}├──{C}User Url {Y}:{RS} {R}Not Found ❗️{RS}")

    Telegram_USER_Url = f"https://t.me/{usernames}"

    Telegram_Request = requests.get(Telegram_USER_Url)

    print(f"{' ' * 5}└[{G} USER {RS}/{G} GROUP {RS}/{G} PAGE {RS}]")

    if Telegram_Request.status_code == 200:

        print(f"{' ' * 10}└[{R}•{RS}] {C}User Url {Y}:{RS} {Telegram_USER_Url}")

        Telegram_Soup = BeautifulSoup(Telegram_Request.text, "html.parser")

        user_full_name_tag_talegram = Telegram_Soup.find_all('span', attrs={'dir': 'auto'})
        full_name_tag_talegram = Telegram_Soup.find_all(class_="tgme_page_description")
        Group_member_and_online_talegram = Telegram_Soup.find_all(class_="tgme_page_extra")

        if (full_name_tag_talegram):
            def remove(string):
                return string.replace("""
      """, "")

            string = full_name_tag_talegram[0].getText()
            print(f"{' ' * 10}└[{B}•{RS}] {C}User Description {Y}:{RS} {remove(string)}")

        for FULL_NAME in user_full_name_tag_talegram:
            print(f"{' ' * 10}└[{Y}•{RS}] {C}User Profile{RS}/{C}Group{RS}/{C}Page Name {Y}:{RS} {FULL_NAME.string}")

        if (not Group_member_and_online_talegram):
            print(f"{' ' * 10}└[{G}•{RS}] {C}Group Members & Online {Y}:{RS} {R}Not Found ❌ {RS}")
        else:
            def remove(string):
                return string.replace("""
      """, " ")

            string = Group_member_and_online_talegram[0].getText()
            print(
                f"{' ' * 10}└[{R}•{RS}] {C}Group Members & Online{RS}/{C}Username{RS}/{C}Subscribers{Y}:{RS} {remove(string)}")

    elif Telegram_Request.status_code == 404:
        print(f"\n└── {B}Telegram {R}✖{RS}")
        print(f"{' ' * 5}└[{R}•{RS}] {C}User Url {Y}:{RS} {R}Not Found ❗️{RS}")

    # [ TINDER ]

    Tinder_Url = f"https://tinder.com/@{usernames}"

    Tinder_Request = requests.get(Tinder_Url)

    if Tinder_Request.status_code == 200:

        print(f"\n[{B} TINDER{RS} ]")

        Tinder_Soup = BeautifulSoup(Tinder_Request.text, "html.parser")

        Tinder_title = Tinder_Soup.find("meta", property='profile:first_name')
        Tinder_Image = Tinder_Soup.find("meta", property="og:image")

        if Tinder_title:
            print(f"{' ' * 5}└[{R}•{RS}] {C}User Url {Y}:{RS} {Tinder_Url}")
            print(f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {Tinder_title['content']}")
            print(f"{' ' * 5}└[{B}•{RS}] {C}User Profile Image {Y}:{RS} {Tinder_Image['content']}")
        else:
            print(f"{' ' * 5}└[{R}•{RS}] {C}User Info {Y}:{RS} {R}Not Found ❗️{RS} ")

    # [ SOUNDCLOUD ]

    SOUNDCLOUD_Url = f"https://soundcloud.com/{usernames}"

    SOUNDCLOUD_Request = requests.get(SOUNDCLOUD_Url)

    if SOUNDCLOUD_Request.status_code == 200:
        print(f"\n[{B} SOUNDCLOUD{RS} ]")

        SOUNDCLOUD_Soup = BeautifulSoup(SOUNDCLOUD_Request.text, "html.parser")

        SOUNDCLOUD_title = SOUNDCLOUD_Soup.find("meta", property='og:title')
        SOUNDCLOUD_FOLLOWER = SOUNDCLOUD_Soup.find("meta", property='soundcloud:follower_count')

        print(f"{' ' * 5}└[{R}•{RS}] {C}User Url {Y}:{RS} {SOUNDCLOUD_Url}")
        print(f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {SOUNDCLOUD_title['content']}")
        print(f"{' ' * 5}└[{B}•{RS}] {C}User Follower {Y}:{RS} {SOUNDCLOUD_FOLLOWER['content']}")

    if SOUNDCLOUD_Request.status_code == 404:
        print(f"\n[{B} SOUNDCLOUD{RS} ]")
        print(f"{' ' * 5}└[{R}•{RS}] {C}User Info {Y}:{RS} {R}Not Found ❗️{RS}")

    # [ STEAM ]

    STEAM_Url = f"https://steamcommunity.com/id/{usernames}"

    STEAM_Request = requests.get(STEAM_Url)

    if STEAM_Request.status_code == 200:

        print(f"\n[{B} STEAM{RS} ]")

        STEAM_Soup = BeautifulSoup(STEAM_Request.text, "html.parser")

        STEAM_name = STEAM_Soup.find_all('span', attrs={'class': 'actual_persona_name'})

        STEAM_specified_profile_could_not_be_found = STEAM_Soup.find_all('div', id="message")

        profile_private_info = STEAM_Soup.find_all('div', class_="profile_private_info")

        STEAM_friend_PlayerLevel = STEAM_Soup.find_all('span', attrs={'class': 'friendPlayerLevelNum'})

        NOT_FOUND = STEAM_Soup.find_all('p', class_='sectionText')

        if (not profile_private_info):
            if (not NOT_FOUND):
                print(f"{' ' * 5}└[{R}•{RS}] {C}User Url {Y}:{RS} {STEAM_Url}")
                print(f"{' ' * 5}└[{B}•{RS}] {C}User Player Name {Y}:{RS} {STEAM_name[0].getText()}")
                print(f"{' ' * 5}└[{Y}•{RS}] {C}User Player LevelNum {Y}:{RS} {STEAM_friend_PlayerLevel[0].getText()}")
            else:
                print(f"{' ' * 5}└[{R}•{RS}] {C}User Info{Y}:{RS} {R}Not Found ❗️{RS}")
        else:
            def remove(string):
                return string.replace("""
    															""", "        ")

            string = profile_private_info[0].getText()
            str = remove(string)
            new_str = str.strip()
            print(f"{' ' * 5}└[{R}•{RS}] {C}User Private {Y}:{RS} {new_str}")

    # [ LINKTR ]

    LINKTR_Url = f"https://linktr.ee/{usernames}"

    LINKTR_Request = requests.get(LINKTR_Url)

    if LINKTR_Request.status_code == 200:

        print(f"\n[{B} LINKTR{RS} ]")

        print(f"{' ' * 5}└[{R}•{RS}] {C}User Url {Y}:{RS} {LINKTR_Url}")

        LINKTR_Soup = BeautifulSoup(LINKTR_Request.text, "html.parser")

        LINKTR_title2 = LINKTR_Soup.find('span', attrs={
            'class': 'UserDetailsCard_title__trfvf UserDetailsCard_oneLineTruncation__uhOF5'})

        NOT_verified = LINKTR_Soup.find('div', class_="sc-bdfBwQ dnZXm")

        profile_name = LINKTR_Soup.find('div', class_="sc-bdfBwQ Header__Grid-sc-i98650-0 llgrqs jvyDlw")

        profile_description = LINKTR_Soup.find('div', class_="sc-bdfBwQ hTuoxC")

        profile_image = LINKTR_Soup.find('meta', property='og:image')

        if (not NOT_verified):
            if (not profile_name):
                print(f"{' ' * 5}└[{Y}•{RS}] {C}User Profile Name {Y}:{RS} {R}Not Found ❗️{RS} ")
            else:
                print(f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {profile_name.string}")

            if (not profile_description):
                print(f"{' ' * 5}└[{Y}•{RS}] {C}User Description {Y}:{RS} {R}Not Found ❗️{RS} ")
            else:
                print(f"{' ' * 5}└[{Y}•{RS}] {C}User Description {Y}:{RS} {profile_description.string}")

            if (not profile_image):
                print(f"{' ' * 5}└[{Y}•{RS}] {C}User Profile Image {Y}:{RS} {R}Not Found ❗️{RS} ")
            else:
                print(f"{' ' * 5}└[{G}•{RS}] {C}User Profile Image {Y}:{RS} {profile_image['content']}")
        else:
            print(f"{' ' * 5}└[{B}•{RS}] {C}User Profile Image {Y}:{RS} {NOT_verified.string}")

    if LINKTR_Request.status_code == 404:
        print(f"\n[{B} LINKTR{RS} ]")
        print(f"{' ' * 5}└[{R}•{RS}] {C}User Info {Y}:{RS} {R}Not Found ❗️{RS} ")

    # [ XBOX GAMER ]

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.33',
    }

    XBOXGAMERTAG_Url = f"https://www.xboxgamertag.com/search/{usernames}"

    XBOXGAMERTAG_Request = requests.get(XBOXGAMERTAG_Url, headers=headers)

    if XBOXGAMERTAG_Request.status_code == 200:
        print(f"\n[{B} XBOX GAMER{RS} ]")

        print(f"{' ' * 5}└[{R}•{RS}] {C}User Url {Y}:{RS} {XBOXGAMERTAG_Url}")

        LINKTR_Soup = BeautifulSoup(XBOXGAMERTAG_Request.text, "html.parser")

        Gamerscore = LINKTR_Soup.find('div', class_="col-auto profile-detail-item")

        name_XBOX = LINKTR_Soup.find('title')

        def remove(string):
            return string.replace("""
                                    """, " ")

        string = Gamerscore.getText()
        str = remove(string)
        new_str = str.strip()
        print(f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {name_XBOX.getText()}")
        print(f"{' ' * 5}└[{B}•{RS}] {C}User Gamer Score {Y}:{RS} {new_str}")

    if XBOXGAMERTAG_Request.status_code == 404:
        print(f"\n[{B} XBOX GAMER{RS} ]")
        print(f"{' ' * 5}└[{R}•{RS}] {C}User Info {Y}:{RS} {R}Not Found ❗️{RS} ")

    # [ TWITCH ]

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.33',
    }

    TWITCH_Url = f"https://twitchtracker.com/{usernames}"

    TWITCH_Request = requests.get(TWITCH_Url, headers=headers)

    if TWITCH_Request.status_code == 200:

        print(f"\n[{B} TWITCH{RS} ]")

        print(f"{' ' * 5}└[{R}•{RS}] {C}User Url {Y}:{RS} {'https://www.twitch.tv/' + usernames}")

        TWITCH_Soup = BeautifulSoup(TWITCH_Request.text, "html.parser")

        name_TWITCH = TWITCH_Soup.find('div', id='app-title')

        BIO_TWITCH = TWITCH_Soup.find('div', style="word-wrap:break-word;font-size:12px;")

        PLAYER_RANK_TWITCH = TWITCH_Soup.find('span', class_="to-number")

        PLAYER_Followers_TWITCHs = TWITCH_Soup.find('div', style="display: inline-block;")

        PLAYER_Avgviewer_TWITCHs = TWITCH_Soup.find('div', style="display: inline-block;margin-left: 20px;")

        name_TWITCH_SPACE_REMOVE = name_TWITCH.getText()
        name_TWITCH_SPACE_REMOVE_RESULT = name_TWITCH_SPACE_REMOVE.strip()

        if (not BIO_TWITCH):
            print(f"{' ' * 5}└[{R}•{RS}] {C}User Player Name {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(f"{' ' * 5}└[{B}•{RS}] {C}User Player Name {Y}:{RS} {name_TWITCH_SPACE_REMOVE_RESULT}")

        if (not BIO_TWITCH):
            print(f"{' ' * 5}└[{B}•{RS}] {C}User Description {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(f"{' ' * 5}└[{Y}•{RS}] {C}User Description {Y}:{RS} {BIO_TWITCH.get_text()}")

        if (not PLAYER_Followers_TWITCHs):
            print(f"{' ' * 5}└[{Y}•{RS}] {C}User Player Followers {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            PLAYER_FOLLOWERSS_TWITCHs = TWITCH_Soup.find('div', style="display: inline-block;").find('span',
                                                                                                     class_="to-number")
            print(f"{' ' * 5}└[{G}•{RS}] {C}User Player Followers {Y}:{RS} {PLAYER_FOLLOWERSS_TWITCHs.string}")

        if (not PLAYER_RANK_TWITCH):
            print(f"{' ' * 5}└[{Y}•{RS}] {C}User Player RANK {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(f"{' ' * 5}└[{B}•{RS}] {C}User Player RANK {Y}:{RS} {PLAYER_RANK_TWITCH.getText()}")

    if TWITCH_Request.status_code == 404:
        print(f"\n[{B} TWITCH{RS} ]")
        print(f"{' ' * 5}└[{R}•{RS}] {C}User Info {Y}:{RS} {R}Not Found ❗️{RS} ")

    # [ PROFILES WORDPRESS ]

    PROFILESWORDPRESS_Url = f"https://profiles.wordpress.org/{usernames}/"

    PROFILESWORDPRESS_Request = requests.get(PROFILESWORDPRESS_Url)

    if PROFILESWORDPRESS_Request.status_code == 200:

        print(f"\n[{B} PROFILES WORDPRESS{RS} ]")

        print(f"{' ' * 5}└[{R}•{RS}] {C}User Url {Y}:{RS} {PROFILESWORDPRESS_Url}")

        PROFILESWORDPRESS_Soup = BeautifulSoup(PROFILESWORDPRESS_Request.text, "html.parser")

        NAME_title = PROFILESWORDPRESS_Soup.find('h2', attrs={'class': 'fn'})

        username_slack_title = PROFILESWORDPRESS_Soup.find('p', attrs={'id': 'slack-username'})

        Member_Since_title = PROFILESWORDPRESS_Soup.find('li', attrs={'id': 'user-member-since'})

        location_name = PROFILESWORDPRESS_Soup.find('li', attrs={'id': 'user-location'})

        USER_GITHUB_USERNAME = PROFILESWORDPRESS_Soup.find('li', attrs={'id': 'user-github'})

        user_job = PROFILESWORDPRESS_Soup.find('li', attrs={'id': 'user-job'})

        user_company = PROFILESWORDPRESS_Soup.find('li', attrs={'id': 'user-company'})

        Interests = PROFILESWORDPRESS_Soup.find('div', attrs={'class': 'item-meta-interests'})

        BIO = PROFILESWORDPRESS_Soup.find('div', attrs={'class': 'item-meta-about'})

        if (not NAME_title):
            print(f"{' ' * 5}└[{Y}•{RS}] {C}User Profile Name {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {NAME_title.string}")

        if (not username_slack_title):
            print(f"{' ' * 5}└[{Y}•{RS}] {C}User Slack Username {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            name_PROFILESWORDPRESS_SPACE_REMOVE = username_slack_title.get_text()
            name_PROFILESWORDPRESS_SPACE_REMOVE_RESULT = name_PROFILESWORDPRESS_SPACE_REMOVE.strip()
            print(f"{' ' * 5}└[{Y}•{RS}] {C}User Slack Username {Y}:{RS} {name_PROFILESWORDPRESS_SPACE_REMOVE_RESULT}")

        if (not BIO):
            print(f"{' ' * 5}└[{G}•{RS}] {C}User Bio {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            BIOS = PROFILESWORDPRESS_Soup.find('div', attrs={'class': 'item-meta-about'}).find('p')
            print(f"{' ' * 5}└[{G}•{RS}] {C}User Bio {Y}:{RS} {BIOS.getText()}")

        if (not Member_Since_title):
            print(f"{' ' * 5}└[{R}•{RS}] {C}User Member Since {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            Member_Since_titleS = PROFILESWORDPRESS_Soup.find('li', attrs={'id': 'user-member-since'}).find('strong')
            print(f"{' ' * 5}└[{R}•{RS}] {C}User Member Since {Y}:{RS} {Member_Since_titleS.get_text()}")

        if (not location_name):
            print(f"{' ' * 5}└[{B}•{RS}] {C}User Location {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            location_names = PROFILESWORDPRESS_Soup.find('li', attrs={'id': 'user-location'}).find('strong')
            print(f"{' ' * 5}└[{B}•{RS}] {C}User Location {Y}:{RS} {location_names.get_text()}")

        if (not USER_GITHUB_USERNAME):
            print(f"{' ' * 5}└[{Y}•{RS}] {C}User GitHub {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            USER_GITHUB_USERNAMES = PROFILESWORDPRESS_Soup.find('li', attrs={'id': 'user-github'}).find('strong')
            print(f"{' ' * 5}└[{Y}•{RS}] {C}User GitHub {Y}:{RS} {USER_GITHUB_USERNAMES.get_text()}")

        if (not user_job):
            print(f"{' ' * 5}└[{G}•{RS}] {C}User Job Title {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            USER_JOB = PROFILESWORDPRESS_Soup.find('li', attrs={'id': 'user-job'}).find('strong')
            print(f"{' ' * 5}└[{G}•{RS}] {C}User Job Title {Y}:{RS} {USER_JOB.get_text()}")

        if (not user_company):
            print(f"{' ' * 5}└[{R}•{RS}] {C}User Employer {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            USER_COMPANY = PROFILESWORDPRESS_Soup.find('li', attrs={'id': 'user-company'}).find('strong')
            print(f"{' ' * 5}└[{R}•{RS}] {C}User Employer {Y}:{RS} {USER_COMPANY.get_text()}")

        if (not Interests):
            print(f"{' ' * 5}└[{B}•{RS}] {C}User Interests {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            InterestsS = PROFILESWORDPRESS_Soup.find('div', attrs={'class': 'item-meta-interests'}).find('p')
            name_Interests_SPACE_REMOVE = InterestsS.getText()
            name_Interests_SPACE_REMOVE_RESULT = name_Interests_SPACE_REMOVE.strip()
            print(f"{' ' * 5}└[{B}•{RS}] {C}User Interests {Y}:{RS} {name_Interests_SPACE_REMOVE_RESULT}")

    if PROFILESWORDPRESS_Request.status_code == 404:
        print(f"\n[{B} PROFILES WORDPRESS{RS} ]")
        print(f"{' ' * 5}└[{R}•{RS}] {C}User Info {Y}:{RS} {R}Not Found ❗️{RS} ")

    # [ THERMI ]

    THERMI_Url = f"https://thermi.com/providers_profiles/{usernames}/"

    THERMI_Request = requests.get(THERMI_Url)

    if THERMI_Request.status_code == 200:

        print(f"\n[{B} THERMI{RS} ]")

        print(f"{' ' * 5}└[{R}•{RS}] {C}User Url {Y}:{RS} {THERMI_Url}")

        THERMI_Soup = BeautifulSoup(THERMI_Request.text, "html.parser")

        THERMI_NAME = THERMI_Soup.find('div', attrs={'class': 'provider_name'})

        specialty_NAME = THERMI_Soup.find('div', attrs={'class': 'provider_specialty'})

        Address_NAME = THERMI_Soup.find('div', attrs={'class': 'content_container'})

        PHONE_NUMBER = THERMI_Soup.find('a', attrs={'class': 'provider_phone'})

        if (not THERMI_NAME):
            print(f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            name_THERMI_NAME_SPACE_REMOVE = THERMI_NAME.get_text()
            name_THERMI_SPACE_REMOVE_RESULT = name_THERMI_NAME_SPACE_REMOVE.strip()
            print(f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {name_THERMI_SPACE_REMOVE_RESULT}")

        if (not specialty_NAME):
            print(f"{' ' * 5}└[{Y}•{RS}] {C}User Specialty {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            name_THERMI_NAME_SPACE_REMOVE = specialty_NAME.get_text()
            name_THERMI_SPACE_REMOVE_RESULT = name_THERMI_NAME_SPACE_REMOVE.strip()
            print(f"{' ' * 5}└[{Y}•{RS}] {C}User Specialty {Y}:{RS} {name_THERMI_SPACE_REMOVE_RESULT}")

        if (not Address_NAME):
            print(f"{' ' * 5}└[{G}•{RS}] {C}User Address {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            Address_NAMES = THERMI_Soup.find('div', attrs={'class': 'content_container'}).find('address')
            name_THERMI_NAME_SPACE_REMOVE = Address_NAMES.get_text()
            name_THERMI_SPACE_REMOVE_RESULT = name_THERMI_NAME_SPACE_REMOVE.strip()
            print(f"{' ' * 5}└[{G}•{RS}] {C}User Address {Y}:{RS} {name_THERMI_SPACE_REMOVE_RESULT}")

        if (not PHONE_NUMBER):
            print(f"{' ' * 5}└[{R}•{RS}] {C}User Address {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            name_THERMI_NAME_SPACE_REMOVE = PHONE_NUMBER.get_text()
            name_THERMI_SPACE_REMOVE_RESULT = name_THERMI_NAME_SPACE_REMOVE.strip()
            print(
                f"{' ' * 5}└[{R}•{RS}] {C}User PhoneNumber{RS}/{C}Telephone {Y}:{RS} {name_THERMI_SPACE_REMOVE_RESULT}")

        print(f"{' ' * 5}[{G} NOTE {RS}] [ {C}YOU SEE THE {R}INFO{C} ON{RS},{C} THIS A {Y}DOCTORE{C} INFO{G}{RS} ] \n")

    if THERMI_Request.status_code == 404:
        print(f"\n[{B} THERMI{RS} ]")
        print(f"{' ' * 5}└[{R}•{RS}] {C}User Info {Y}:{RS} {R}Not Found ❗️{RS} ")

    # [ FREELANCER ]

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.33',
    }

    FREELANCER_Url = f"https://www.freelancer.com/u/{usernames}"

    FREELANCER_Request = requests.get(FREELANCER_Url, headers=headers)

    if FREELANCER_Request.status_code == 200:

        print(f"\n[{B} FREELANCER{RS} ]")

        print(f"{' ' * 5}└[{R}•{RS}] {C}User Url {Y}:{RS} {FREELANCER_Url}")

        FREELANCER_Soup = BeautifulSoup(FREELANCER_Request.text, "html.parser")

        FREELANCER_NAME = FREELANCER_Soup.find('fl-col', class_="SummaryHeader")

        FREELANCER_TAGLINE = FREELANCER_Soup.find('fl-heading', class_="Tagline ng-star-inserted")

        FREELANCER_STAR = FREELANCER_Soup.find('fl-bit', class_="ValueBlock ng-star-inserted")

        FREELANCER_REVIEW = FREELANCER_Soup.find('fl-bit', class_="ReviewCount ng-star-inserted")

        FREELANCER_PER_HOURS = FREELANCER_Soup.find('fl-bit', class_="Row ng-star-inserted")

        FREELANCER_ADDRESS = FREELANCER_Soup.find('fl-col', class_="SupplementaryInfo")

        FREELANCER_JOBS_COMPLETED = FREELANCER_Soup.find('fl-text', class_="ReputationItemAmount")

        if (not FREELANCER_NAME):
            print(f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {FREELANCER_NAME.find('h3').get_text()}")

        if (not FREELANCER_TAGLINE):
            print(f"{' ' * 5}└[{Y}•{RS}] {C}User TagLine {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(f"{' ' * 5}└[{Y}•{RS}] {C}User TagLine {Y}:{RS} {FREELANCER_TAGLINE.find('h2').get_text()}")

        if (not FREELANCER_STAR):
            print(f"{' ' * 5}└[{G}•{RS}] {C}User Average Rating {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(f"{' ' * 5}└[{G}•{RS}] {C}User Average Rating {Y}:{RS} {FREELANCER_STAR.string}")

        if (not FREELANCER_REVIEW):
            print(f"{' ' * 5}└[{R}•{RS}] {C}User Review {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(f"{' ' * 5}└[{R}•{RS}] {C}User Review {Y}:{RS} {FREELANCER_REVIEW.get_text()}")

        if (not FREELANCER_PER_HOURS):
            print(f"{' ' * 5}└[{B}•{RS}] {C}User Charge {G}$USD{C} Hour{Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            FREELANCER_PER_HOURS_REMOVE = FREELANCER_PER_HOURS.getText()
            FREELANCER_PER_HOURS_REMOVE_RESULT = FREELANCER_PER_HOURS_REMOVE.strip()
            print(f"{' ' * 5}└[{B}•{RS}] {C}User Charge {G}$USD{C} Hour{Y}:{RS} {FREELANCER_PER_HOURS_REMOVE_RESULT}")

        if (not FREELANCER_ADDRESS):
            print(f"{' ' * 5}└[{Y}•{RS}] {C}User Address {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(f"{' ' * 5}└[{Y}•{RS}] {C}User Address {Y}:{RS} {FREELANCER_ADDRESS.get_text()}")

        if (not FREELANCER_ADDRESS):
            print(f"{' ' * 5}└[{G}•{RS}] {C}User Jobs Completed {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(f"{' ' * 5}└[{G}•{RS}] {C}User Jobs Completed {Y}:{RS} {FREELANCER_JOBS_COMPLETED.get_text()}")

        url = f"https://www.freelancer.com/api/users/0.1/users?limit=1&usernames[]={usernames}&avatar=true&online_offline_details=true&status=true&support_status_details=true&limited_account=true&webapp=1&compact=true&new_errors=true&new_pools=true"

        freelancer_Verifications_Request = requests.request("GET", url)

        freelancer_Verifications_Data_Json = json.loads(freelancer_Verifications_Request.content)

        freelancer_Verifications_ID = list(freelancer_Verifications_Data_Json['result']['users'].keys())[0]

        print(
            f"\n{' ' * 5}[{G} NOTE {RS}] [ {B}Freelancer {Y}Verified{C} Checker You Can Find {R}USER{Y} Facebook{RS}, {Y}Linkedin{C} IF YOUR {R}USER{Y} LINK {C}THIS {Y}ACCOUNT {C}WITH HIS {B}Freelancer Account{RS} ]\n")

        if freelancer_Verifications_Data_Json['result']['users'][freelancer_Verifications_ID]['status'][
            'payment_verified'] == True:
            print(f"{' ' * 5}└[{R}•{RS}] {C}User Payment Verified {Y}:{RS} {G} True ✔️️{RS} ")
        else:
            print(f"{' ' * 5}└[{R}•{RS}] {C}User Payment Verified {Y}:{RS} {R} False {R}❌️️{RS} ")

        if freelancer_Verifications_Data_Json['result']['users'][freelancer_Verifications_ID]['status'][
            'email_verified'] == True:
            print(f"{' ' * 5}└[{B}•{RS}] {C}User Email Verified {Y}:{RS} {G} True ✔️️{RS} ")
        else:
            print(f"{' ' * 5}└[{B}•{RS}] {C}User Email Verified {Y}:{RS} {R} False {R}❌️️{RS} ")

        if freelancer_Verifications_Data_Json['result']['users'][freelancer_Verifications_ID]['status'][
            'deposit_made'] == True:
            print(f"{' ' * 5}└[{Y}•{RS}] {C}User Deposit Made {Y}:{RS} {G} True ✔️️{RS} ")
        else:
            print(f"{' ' * 5}└[{Y}•{RS}] {C}User Deposit Made {Y}:{RS} {R} False {R}❌️️{RS} ")

        if freelancer_Verifications_Data_Json['result']['users'][freelancer_Verifications_ID]['status'][
            'profile_complete'] == True:
            print(f"{' ' * 5}└[{G}•{RS}] {C}User Profile Complete {Y}:{RS} {G} True ✔️️{RS} ")
        else:
            print(f"{' ' * 5}└[{G}•{RS}] {C}User Profile Complete {Y}:{RS} {R} False {R}❌️️{RS} ")

        if freelancer_Verifications_Data_Json['result']['users'][freelancer_Verifications_ID]['status'][
            'phone_verified'] == True:
            print(f"{' ' * 5}└[{R}•{RS}] {C}User Phone Verified {Y}:{RS} {G} True ✔️️{RS} ")
        else:
            print(f"{' ' * 5}└[{R}•{RS}] {C}User Phone Verified {Y}:{RS} {R} False {R}❌️️{RS} ")

        if freelancer_Verifications_Data_Json['result']['users'][freelancer_Verifications_ID]['status'][
            'identity_verified'] == True:
            print(f"{' ' * 5}└[{B}•{RS}] {C}User Identity Verified {Y}:{RS} {G} True ✔️️{RS} ")
        else:
            print(f"{' ' * 5}└[{B}•{RS}] {C}User Identity Verified {Y}:{RS} {R} False {R}❌️️{RS} ")

        if freelancer_Verifications_Data_Json['result']['users'][freelancer_Verifications_ID]['status'][
            'facebook_connected'] == True:
            print(f"{' ' * 5}└[{Y}•{RS}] {C}User Facebook Connected {Y}:{RS} {G} True ✔️️{RS} ")
        else:
            print(f"{' ' * 5}└[{Y}•{RS}] {C}User Facebook Connected {Y}:{RS} {R} False {R}❌️️{RS} ")

        if freelancer_Verifications_Data_Json['result']['users'][freelancer_Verifications_ID]['status'][
            'freelancer_verified_user'] == True:
            print(f"{' ' * 5}└[{G}•{RS}] {C}User Freelancer Verified_user {Y}:{RS} {G} True ✔️️{RS} ")
        else:
            print(f"{' ' * 5}└[{G}•{RS}] {C}User Freelancer Verified_user {Y}:{RS} {R} False {R}❌️️{RS} ")

        if freelancer_Verifications_Data_Json['result']['users'][freelancer_Verifications_ID]['status'][
            'linkedin_connected'] == True:
            print(f"{' ' * 5}└[{R}•{RS}] {C}User Linkedin Connected {Y}:{RS} {G} True ✔️️{RS} ")
        else:
            print(f"{' ' * 5}└[{R}•{RS}] {C}User Linkedin Connected {Y}:{RS} {R} False {R}❌️️{RS} ")

        if freelancer_Verifications_Data_Json['result']['users'][freelancer_Verifications_ID]['status'][
            'custom_charge_verified'] == True:
            print(f"{' ' * 5}└[{Y}•{RS}] {C}User Custom Charge Verified {Y}:{RS} {G} True ✔️️{RS} ")
        else:
            print(f"{' ' * 5}└[{Y}•{RS}] {C}User Custom Charge Verified {Y}:{RS} {R} False {R}❌️️{RS} ")

    if FREELANCER_Request.status_code == 404:
        print(f"\n[{B} FREELANCER{RS} ]")
        print(f"{' ' * 5}└[{R}•{RS}] {C}User Info {Y}:{RS} {R}Not Found ❗️{RS} ")

    # [ TradingView ]

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.33',
    }

    TradingView_Url = f"https://www.tradingview.com/u/{usernames}"

    TradingView_Request = requests.get(TradingView_Url, headers=headers)

    if TradingView_Request.status_code == 200:

        print(f"\n[{B} TradingView{RS} ]")

        print(f"{' ' * 5}└[{R}•{RS}] {C}User Url {Y}:{RS} {TradingView_Url}")

        TradingView_Soup = BeautifulSoup(TradingView_Request.text, "html.parser")

        TradingView_IMAGE = TradingView_Soup.find('meta', property="og:image:secure_url")

        TradingView_NAME = TradingView_Soup.find('div', class_="tv-profile__main-block--container")

        if (not TradingView_NAME):
            print(f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            TradingView_NAMES = TradingView_NAME.find('h1', class_="tv-profile__name-text").get_text()
            print(f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {TradingView_NAMES}")

        if (not TradingView_IMAGE):
            print(f"{' ' * 5}└[{G}•{RS}] {C}User Profile Image {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(f"{' ' * 5}└[{G}•{RS}] {C}User Image {Y}:{RS} {TradingView_IMAGE['content']}")

    if TradingView_Request.status_code == 404:
        print(f"\n[{B} TradingView{RS} ]")
        print(f"{' ' * 5}└[{R}•{RS}] {C}User Info {Y}:{RS} {R}Not Found ❗️{RS} ")

    # [ GAANA ]

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.33',
    }

    GAANA_Url = f"https://gaana.com/artist/{usernames}"

    GAANA_Request = requests.request("GET", GAANA_Url, headers=headers)

    if GAANA_Request.status_code == 200:
        print(f"\n[{B} GAANA{RS} ]")
        print(f"{' ' * 5}└[{R}•{RS}] {C}User Url{Y}:{RS} {GAANA_Url}")
        GAANA_Soup = BeautifulSoup(GAANA_Request.text, "html.parser")

        GAANA_USER_NAME = GAANA_Soup.find('div', attrs={'class': 'info'})

        if (not GAANA_USER_NAME):
            print(f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(
                f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {GAANA_USER_NAME.find('div', attrs={'class': '_a'}).find('h1', attrs={'class': 'title t_over'}).string}")

    elif GAANA_Request.status_code == 404:
        print(f"\n[{B} GAANA{RS} ]")
        print(f"{' ' * 5}└[{R}•{RS}] {C}User Info{Y}:{RS} {R}Not Found ❗️{RS}")

    # [ FLICKR ]

    FLICKR_Url = f"https://www.flickr.com/people/{usernames}/"

    FLICKR_Request = requests.get(FLICKR_Url)

    if FLICKR_Request.status_code == 200:

        print(f"\n[{B} FLICKR{RS} ]")

        print(f"{' ' * 5}└[{R}•{RS}] {C}User Url {Y}:{RS} {FLICKR_Url}")

        FLICKR_Soup = BeautifulSoup(FLICKR_Request.text, "html.parser")

        FLICKR_PROFILE_NAME = FLICKR_Soup.find('div', attrs={'class': 'title-container'})
        FLICKR_JOIN_DATE = FLICKR_Soup.find('div', attrs={'class': 'infos-view-container'})
        FLICKR_FOLLOWERS_FOLLOWING = FLICKR_Soup.find('div', attrs={'class': 'metadata-container'})

        if (not FLICKR_PROFILE_NAME):
            print(f"{' ' * 5}└[{B}•{RS}] {C}User Seeking {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            seeking_space_remove = FLICKR_PROFILE_NAME.find('h1').getText()
            After_remove_seeking_space = seeking_space_remove.strip()
            print(f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {After_remove_seeking_space}")

        if (not FLICKR_JOIN_DATE):
            print(f"{' ' * 5}└[{Y}•{RS}] {C}User Seeking {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            seeking_space_remove = FLICKR_JOIN_DATE.find('ul').find('li').find('a', attrs={
                'class': 'archives-link'}).getText()
            After_remove_seeking_space = seeking_space_remove.strip()
            print(f"{' ' * 5}└[{Y}•{RS}] {C}User Join FLICKR {Y}:{RS} {After_remove_seeking_space}")

        if (not FLICKR_FOLLOWERS_FOLLOWING):
            print(f"{' ' * 5}└[{G}•{RS}] {C}User Seeking {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            seeking_space_remove = FLICKR_FOLLOWERS_FOLLOWING.find('div', attrs={'class': 'coverphoto-stats'}).find(
                'p').getText()
            After_remove_seeking_space = seeking_space_remove.strip()
            print(f"{' ' * 5}└[{G}•{RS}] {C}User Followers & Following {Y}:{RS} {After_remove_seeking_space}")

    elif FLICKR_Request.status_code == 404:
        print(f"\n[{B} FLICKR{RS} ]")
        print(f"{' ' * 5}└[{R}•{RS}] {C}User Info {Y}:{RS} {R}Not Found ❗️{RS} ")

    # [ INDEPENDENT ACADEMIA ]

    INDEPENDENT_ACADEMIA_URL = f"https://independent.academia.edu/{usernames}"

    INDEPENDENT_ACADEMIA_Request = requests.get(INDEPENDENT_ACADEMIA_URL)

    if INDEPENDENT_ACADEMIA_Request.status_code == 200:

        print(f"\n[{B} INDEPENDENT ACADEMIA{RS} ]")

        INDEPENDENT_ACADEMIA_Soup = BeautifulSoup(INDEPENDENT_ACADEMIA_Request.text, "html.parser")

        INDEPENDENT_ACADEMIA_FULL_NAME = INDEPENDENT_ACADEMIA_Soup.find('div',
                                                                        attrs={'class': 'profile-info-container'})

        print(f"{' ' * 5}└[{R}•{RS}] {C}User Url {Y}:{RS} {INDEPENDENT_ACADEMIA_URL}")

        if (not INDEPENDENT_ACADEMIA_FULL_NAME):
            print(f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(
                f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {INDEPENDENT_ACADEMIA_FULL_NAME.find('li', attrs={'class': 'InlineList-item u-fontSerif u-fs24 u-lineHeight1_2'}).getText()}")


    elif INDEPENDENT_ACADEMIA_Request.status_code == 404:
        print(f"\n[{B} INDEPENDENT ACADEMIA{RS} ]")
        print(f"{' ' * 5}└[{R}•{RS}] {C}User Info{Y}:{RS} {R}Not Found ❗️{RS}")

    # [ DEVELOPER APPLE ]

    DEVELOPER_APPLE_URL = f"https://developer.apple.com/forums/profile/{usernames}"

    DEVELOPER_APPLE_Request = requests.get(DEVELOPER_APPLE_URL)

    if DEVELOPER_APPLE_Request.status_code == 200:

        print(f"\n[{B} DEVELOPER APPLE{RS} ]")

        ANILIST_Soup = BeautifulSoup(DEVELOPER_APPLE_Request.text, "html.parser")

        DEVELOPER_APPLE_NAME = ANILIST_Soup.find('section', attrs={'class': 'user-info-box'})

        print(f"{' ' * 5}└[{R}•{RS}] {C}User Url {Y}:{RS} {DEVELOPER_APPLE_URL}")

        if (not DEVELOPER_APPLE_NAME):
            print(f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(
                f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {DEVELOPER_APPLE_NAME.find('div', attrs={'class': 'user-name-reputation'}).find('h2').getText()}")

    elif DEVELOPER_APPLE_Request.status_code == 404:
        print(f"\n[{B} DEVELOPER APPLE{RS} ]")
        print(f"{' ' * 5}└[{R}•{RS}] {C}User Info{Y}:{RS} {R}Not Found ❗️{RS}")

    # [ VIDEOHIVE NET ]

    VIDEOHIVE_URL = f"https://videohive.net/user/{usernames}"

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.33',
    }

    VIDEOHIVE_URL_Request = requests.request("GET", VIDEOHIVE_URL, headers=headers)

    if VIDEOHIVE_URL_Request.status_code == 200:

        print(f"\n[{B} VIDEOHIVE NET{RS} ]")

        VIDEOHIVE_Soup = BeautifulSoup(VIDEOHIVE_URL_Request.text, "html.parser")

        VIDEOHIVE_NAME = VIDEOHIVE_Soup.find('div', attrs={'class': 'user-info-header h-mb0'}).find('h1')
        VIDEOHIVE_LOCATION = VIDEOHIVE_Soup.find('div', attrs={'class': 'user-info-header h-mb0'}).find('p')
        VIDEOHIVE_SALES = VIDEOHIVE_Soup.find('div', attrs={'class': 'user-info-header h-mb0'}).find('strong', attrs={
            'class': 't-heading -size-m'})

        print(f"{' ' * 5}└[{R}•{RS}] {C}User Url {Y}:{RS} {VIDEOHIVE_URL}")

        if (not VIDEOHIVE_NAME):
            print(f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {VIDEOHIVE_NAME.getText()}")

        if (not VIDEOHIVE_LOCATION):
            print(f"{' ' * 5}└[{Y}•{RS}] {C}User Location {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            name_THERMI_NAME_SPACE_REMOVE = VIDEOHIVE_LOCATION.getText()

            name_THERMI_SPACE_REMOVE_RESULT = name_THERMI_NAME_SPACE_REMOVE.strip()

            print(f"{' ' * 5}└[{Y}•{RS}] {C}User Location {Y}:{RS} {name_THERMI_SPACE_REMOVE_RESULT}")

        if (not VIDEOHIVE_SALES):
            print(f"{' ' * 5}└[{G}•{RS}] {C}User Sales {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            name_THERMI_NAME_SPACE_REMOVE = VIDEOHIVE_SALES.getText()

            name_THERMI_SPACE_REMOVE_RESULT = name_THERMI_NAME_SPACE_REMOVE.strip()

            print(f"{' ' * 5}└[{G}•{RS}] {C}User Sales {Y}:{RS} {name_THERMI_SPACE_REMOVE_RESULT}")


    elif VIDEOHIVE_URL_Request.status_code == 404:
        print(f"\n[{B} VIDEOHIVE NET{RS} ]")
        print(f"{' ' * 5}└[{R}•{RS}] {C}User Info{Y}:{RS} {R}Not Found ❗️{RS}")

    # [ BANDCAMP ]

    BANDCAMP_URL = f"https://bandcamp.com/{usernames}"

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.33',
    }

    BANDCAMP_URL_Request = requests.request("GET", BANDCAMP_URL, headers=headers)

    if BANDCAMP_URL_Request.status_code == 200:

        print(f"\n[{B} BANDCAMP{RS} ]")

        BANDCAMP_Soup = BeautifulSoup(BANDCAMP_URL_Request.text, "html.parser")

        BANDCAMP_NAME = BANDCAMP_Soup.find('div', attrs={'class': 'name'}).find('h1')
        BANDCAMP_LOCATION = BANDCAMP_Soup.find('div', attrs={'class': 'info'}).find('li')

        print(f"{' ' * 5}└[{R}•{RS}] {C}User Url {Y}:{RS} {BANDCAMP_URL}")

        if (not BANDCAMP_NAME):
            print(f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {BANDCAMP_NAME.getText()}")

        if (not BANDCAMP_LOCATION):
            print(f"{' ' * 5}└[{Y}•{RS}] {C}User Location {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(f"{' ' * 5}└[{Y}•{RS}] {C}User Location {Y}:{RS} {BANDCAMP_LOCATION.getText()}")


    elif BANDCAMP_URL_Request.status_code == 404:
        print(f"\n[{B} BANDCAMP{RS} ]")
        print(f"{' ' * 5}└[{R}•{RS}] {C}User Info{Y}:{RS} {R}Not Found ❗️{RS}")

    # [ BEZUZYTECZNA ]

    BEHANCE_URL = f"https://bezuzyteczna.pl/uzytkownicy/{usernames}"

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.33',
    }

    BEHANCE_URL_Request = requests.request("GET", BEHANCE_URL, headers=headers)

    if BEHANCE_URL_Request.status_code == 200:

        print(f"\n[{B} BEZUZYTECZNA{RS} ]")

        BEHANCE_Soup = BeautifulSoup(BEHANCE_URL_Request.text, "html.parser")

        BANDCAMP_NAME = BEHANCE_Soup.find('div', attrs={'class': 'p-panel__name'})
        BANDCAMP_JOINED = BEHANCE_Soup.find('div', attrs={'class': 'p-panel__info-line'}).find('span', attrs={
            'p-panel__info-right'})

        print(f"{' ' * 5}└[{R}•{RS}] {C}User Url {Y}:{RS} {BEHANCE_URL}")

        if (not BANDCAMP_NAME):
            print(f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            name_THERMI_NAME_SPACE_REMOVE = BANDCAMP_NAME.getText()

            name_THERMI_SPACE_REMOVE_RESULT = name_THERMI_NAME_SPACE_REMOVE.strip()
            print(f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {name_THERMI_SPACE_REMOVE_RESULT}")

        if (not BANDCAMP_JOINED):
            print(f"{' ' * 5}└[{Y}•{RS}] {C}User Joined {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(f"{' ' * 5}└[{Y}•{RS}] {C}User Joined {Y}:{RS} {BANDCAMP_JOINED.getText()}")


    elif BEHANCE_URL_Request.status_code == 404:
        print(f"\n[{B} BEZUZYTECZNA{RS} ]")
        print(f"{' ' * 5}└[{R}•{RS}] {C}User Info{Y}:{RS} {R}Not Found ❗️{RS}")

    # [ BIKEMAP ]

    BIKEMAP_URL = f"https://www.bikemap.net/en/u/{usernames}/routes/created/"

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.33',
    }

    BIKEMAP_URL_Request = requests.request("GET", BIKEMAP_URL, headers=headers)

    if BIKEMAP_URL_Request.status_code == 200:

        print(f"\n[{B} BIKEMAP{RS} ]")

        BIKEMAP_Soup = BeautifulSoup(BIKEMAP_URL_Request.text, "html.parser")

        BIKEMAP_NAME = BIKEMAP_Soup.find('div', attrs={'class': 'col-sm-10'}).find('h1', attrs={'class': 'title mr'})
        BIKEMAP_JOIN = BIKEMAP_Soup.find('div', attrs={'class': 'title-info'}).find('span',
                                                                                    attrs={'class': 'member-since'})
        BIKEMAP_LOCATION = BIKEMAP_Soup.find('div', attrs={'class': 'title-info'}).find('span',
                                                                                        attrs={'class': 'location'})
        BIKEMAP_PROFILE_PIC = BIKEMAP_Soup.find('div', attrs={'class': 'col-sm-2'}).findAll('img')

        BIKEMAP_PROFILE_PICS = BIKEMAP_PROFILE_PIC[0]

        print(f"{' ' * 5}└[{R}•{RS}] {C}User Url {Y}:{RS} {BIKEMAP_URL}")

        if (not BIKEMAP_NAME):
            print(f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {BIKEMAP_NAME.getText()}")

        if (not BIKEMAP_JOIN):
            print(f"{' ' * 5}└[{Y}•{RS}] {C}User Joined {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(f"{' ' * 5}└[{Y}•{RS}] {C}User Joined {Y}:{RS} {BIKEMAP_JOIN.getText()}")

        if (not BIKEMAP_LOCATION):
            print(f"{' ' * 5}└[{G}•{RS}] {C}User Location {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(f"{' ' * 5}└[{G}•{RS}] {C}User Location {Y}:{RS} {BIKEMAP_LOCATION.getText()}")

        if (not BIKEMAP_PROFILE_PICS):
            print(f"{' ' * 5}└[{R}•{RS}] {C}User Profile Photo {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(f"{' ' * 5}└[{R}•{RS}] {C}User Profile Photo {Y}:{RS} {BIKEMAP_PROFILE_PICS.attrs['src']}")


    elif BIKEMAP_URL_Request.status_code == 404:
        print(f"\n[{B} BIKEMAP{RS} ]")
        print(f"{' ' * 5}└[{R}•{RS}] {C}User Info{Y}:{RS} {R}Not Found ❗️{RS}")

    # [ FORUM DANGEROUSTHINGS ]

    FORUM_DANGEROUSTHINGS_URL = f"https://forum.dangerousthings.com/u/{usernames}"

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.33',
    }

    FORUM_DANGEROUSTHINGS_URL_Request = requests.request("GET", FORUM_DANGEROUSTHINGS_URL, headers=headers)

    if FORUM_DANGEROUSTHINGS_URL_Request.status_code == 200:
        print(f"\n[{B} FORUM DANGEROUSTHINGS{RS} ]")
        print(f"{' ' * 5}└[{R}•{RS}] {C}User Url{Y}:{RS} {FORUM_DANGEROUSTHINGS_URL}")

        FORUM_DANGEROUSTHINGS_Soup = BeautifulSoup(FORUM_DANGEROUSTHINGS_URL_Request.text, "html.parser")

        FORUM_DANGEROUSTHINGS_NAME = FORUM_DANGEROUSTHINGS_Soup.find('div', attrs={'class': 'user-crawler'}).find('h2',
                                                                                                                  attrs={
                                                                                                                      'class': 'username'})

        FORUM_DANGEROUSTHINGS_BIO = FORUM_DANGEROUSTHINGS_Soup.find('p')

        if (not FORUM_DANGEROUSTHINGS_NAME):
            print(f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(
                f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {FORUM_DANGEROUSTHINGS_NAME.getText()}")

        if (not FORUM_DANGEROUSTHINGS_BIO):
            print(f"{' ' * 5}└[{Y}•{RS}] {C}User Bio {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(
                f"{' ' * 5}└[{Y}•{RS}] {C}User Bio {Y}:{RS} {FORUM_DANGEROUSTHINGS_BIO.getText()}")

    elif FORUM_DANGEROUSTHINGS_URL_Request.status_code == 404:
        print(f"\n[{B} FORUM DANGEROUSTHINGS{RS} ]")
        print(f"{' ' * 5}└[{R}•{RS}] {C}User Info{Y}:{RS} {R}Not Found ❗️{RS}")

    # [ COMMUNITY BITWARDEN ]

    COMMUNITY_BITWARDEN_URL = f"https://community.bitwarden.com/u/{usernames}/summary"

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.33',
    }

    COMMUNITY_BITWARDEN_URL_Request = requests.request("GET", COMMUNITY_BITWARDEN_URL, headers=headers)

    if COMMUNITY_BITWARDEN_URL_Request.status_code == 200:
        print(f"\n[{B} COMMUNITY BITWARDEN{RS} ]")
        print(f"{' ' * 5}└[{R}•{RS}] {C}User Url{Y}:{RS} {COMMUNITY_BITWARDEN_URL}")

        COMMUNITY_BITWARDEN_Soup = BeautifulSoup(COMMUNITY_BITWARDEN_URL_Request.text, "html.parser")

        COMMUNITY_BITWARDEN_PROFILE_PICS = COMMUNITY_BITWARDEN_Soup.find('div', attrs={'id': 'main-outlet'}).findAll(
            'img')

        COMMUNITY_BITWARDEN_PROFILE_NAME = COMMUNITY_BITWARDEN_Soup.find('div', attrs={'id': 'main-outlet'}).find('h2',
                                                                                                                  attrs={
                                                                                                                      'class': 'username'})

        COMMUNITY_BITWARDEN_PROFILE_PICS = COMMUNITY_BITWARDEN_PROFILE_PICS[0]

        if (not COMMUNITY_BITWARDEN_PROFILE_NAME):
            print(f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {COMMUNITY_BITWARDEN_PROFILE_NAME.getText()}")

        if (not COMMUNITY_BITWARDEN_PROFILE_PICS):
            print(f"{' ' * 5}└[{Y}•{RS}] {C}User Profile Photo {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(
                f"{' ' * 5}└[{Y}•{RS}] {C}User Profile Photo {Y}:{RS} {COMMUNITY_BITWARDEN_PROFILE_PICS.attrs['src']}")


    elif COMMUNITY_BITWARDEN_URL_Request.status_code == 404:
        print(f"\n[{B} COMMUNITY BITWARDEN{RS} ]")
        print(f"{' ' * 5}└[{R}•{RS}] {C}User Info{Y}:{RS} {R}Not Found ❗️{RS}")

    # [ BOOKCROSSING ]

    BOOKCROSSING_URL = f"https://www.bookcrossing.com/mybookshelf/{usernames}/"

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.33',
    }

    BOOKCROSSING_URL_Request = requests.request("GET", BOOKCROSSING_URL, headers=headers)

    if BOOKCROSSING_URL_Request.status_code == 200:
        print(f"\n[{B} BOOKCROSSING{RS} ]")
        print(f"{' ' * 5}└[{R}•{RS}] {C}User Url{Y}:{RS} {BOOKCROSSING_URL}")

        BOOKCROSSING_Soup = BeautifulSoup(BOOKCROSSING_URL_Request.text, "html.parser")

        BOOKCROSSING_NAME = BOOKCROSSING_Soup.find('div', attrs={'class': 'col small'}).find('h2')

        if (not BOOKCROSSING_NAME):
            print(f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(
                f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {BOOKCROSSING_NAME.getText()}")

    elif BOOKCROSSING_URL_Request.status_code == 404:
        print(f"\n[{B} BOOKCROSSING{RS} ]")
        print(f"{' ' * 5}└[{R}•{RS}] {C}User Info{Y}:{RS} {R}Not Found ❗️{RS}")

    # [ BUY ME A COFFEE ]

    BUY_ME_A_COFFEE_URL = f"https://www.buymeacoffee.com/{usernames}"

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.33',
    }

    BUY_ME_A_COFFEE_URL_Request = requests.request("GET", BUY_ME_A_COFFEE_URL, headers=headers)

    if BUY_ME_A_COFFEE_URL_Request.status_code == 200:
        print(f"\n[{B} BUY ME A COFFEE{RS} ]")
        print(f"{' ' * 5}└[{R}•{RS}] {C}User Url{Y}:{RS} {BUY_ME_A_COFFEE_URL}")

        BUY_ME_A_COFFEE_Soup = BeautifulSoup(BUY_ME_A_COFFEE_URL_Request.text, "html.parser")

        BUY_ME_A_COFFEE_NAME = BUY_ME_A_COFFEE_Soup.find('div', attrs={
            'class': 'p-relative dis-inline-block w-100 xs-pd-l-16 xs-pd-r-16'}).find('h1').find_all('span')
        BUY_ME_A_COFFEE_DESCRIPTION = BUY_ME_A_COFFEE_Soup.find('div', attrs={
            'class': 'p-relative dis-inline-block w-100 xs-pd-l-16 xs-pd-r-16'}).find('h1').find_all('span')
        BUY_ME_A_COFFEE_PROFILE_PHOTO = BUY_ME_A_COFFEE_Soup.find('div', attrs={'class': 'ctr-img-w-h mg-0-a'}).findAll(
            'img')

        BUY_ME_A_COFFEE_PROFILE_PROFILE_PICS = BUY_ME_A_COFFEE_PROFILE_PHOTO[0]

        if (not BUY_ME_A_COFFEE_NAME):
            print(f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(
                f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {BUY_ME_A_COFFEE_NAME[0].getText()}")

        if (not BUY_ME_A_COFFEE_DESCRIPTION):
            print(f"{' ' * 5}└[{Y}•{RS}] {C}User Description {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(
                f"{' ' * 5}└[{Y}•{RS}] {C}User Description {Y}:{RS} {BUY_ME_A_COFFEE_DESCRIPTION[1].getText()}")

        if (not BUY_ME_A_COFFEE_PROFILE_PROFILE_PICS):
            print(f"{' ' * 5}└[{G}•{RS}] {C}User Profile Photo {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(
                f"{' ' * 5}└[{G}•{RS}] {C}User Profile Photo {Y}:{RS} {BUY_ME_A_COFFEE_PROFILE_PROFILE_PICS.attrs['data-src']}")


    elif BUY_ME_A_COFFEE_URL_Request.status_code == 404:
        print(f"\n[{B} BUY ME A COFFEE{RS} ]")
        print(f"{' ' * 5}└[{R}•{RS}] {C}User Info{Y}:{RS} {R}Not Found ❗️{RS}")

    # [ BUZZFEED ]

    BUZZFEED_URL = f"https://www.buzzfeed.com/{usernames}"

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.33',
    }

    BUZZFEED_URL_Request = requests.request("GET", BUZZFEED_URL, headers=headers)

    if BUZZFEED_URL_Request.status_code == 200:
        print(f"\n[{B} BUZZFEED{RS} ]")
        print(f"{' ' * 5}└[{R}•{RS}] {C}User Url{Y}:{RS} {BUZZFEED_URL}")

        BUZZFEED_Soup = BeautifulSoup(BUZZFEED_URL_Request.text, "html.parser")

        BUZZFEED_NAME = BUZZFEED_Soup.find('div', attrs={'class': 'userNameContainer__3Ba3D0bepv'}).find('h1')
        BUZZFEED_JOIN = BUZZFEED_Soup.find('dl', attrs={'class': 'userMetaList__3R_19D6l1X'}).find('dd')

        if (not BUZZFEED_NAME):
            print(f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(
                f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {BUZZFEED_NAME.getText()}")

        if (not BUZZFEED_JOIN):
            print(f"{' ' * 5}└[{Y}•{RS}] {C}User Joined {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(
                f"{' ' * 5}└[{Y}•{RS}] {C}User Joined {Y}:{RS} {BUZZFEED_JOIN.getText()}")


    elif BUZZFEED_URL_Request.status_code == 404:
        print(f"\n[{B} BUZZFEED{RS} ]")
        print(f"{' ' * 5}└[{R}•{RS}] {C}User Info{Y}:{RS} {R}Not Found ❗️{RS}")

    # [ CNET ]

    CNET_URL = f"https://www.cnet.com/profiles/{usernames}/"

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.33',
    }

    CNET_URL_Request = requests.request("GET", CNET_URL, headers=headers)

    if CNET_URL_Request.status_code == 200:
        print(f"\n[{B} CNET{RS} ]")
        print(f"{' ' * 5}└[{R}•{RS}] {C}User Url{Y}:{RS} {CNET_URL}")

        CNET_Soup = BeautifulSoup(CNET_URL_Request.text, "html.parser")

        CNET_NAME = CNET_Soup.find('div', attrs={'id': 'profile-info'}).find('h1').find('span',
                                                                                        attrs={'itemprop': 'name'})
        CNET_LOCATION = CNET_Soup.find('div', attrs={'id': 'profile-info'}).find('div', attrs={'class': 'col-5'}).find(
            'span', attrs={'itemprop': 'locality'})
        CNET_PROFILE_PHOTO = CNET_Soup.find('div', attrs={'class': 'headshot big'})

        if (not CNET_NAME):
            print(f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(
                f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {CNET_NAME.getText()}")

        if (not CNET_LOCATION):
            print(f"{' ' * 5}└[{Y}•{RS}] {C}User Location {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(
                f"{' ' * 5}└[{Y}•{RS}] {C}User Location {Y}:{RS} {CNET_LOCATION.getText()}")

        if (not CNET_PROFILE_PHOTO):
            print(f"{' ' * 5}└[{G}•{RS}] {C}User Profile Photo {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            CNET_PHOTO = CNET_PROFILE_PHOTO.find('figure', attrs={'class': 'img'}).findAll('img')

            CNETS_PHOTO = CNET_PHOTO[0]

            print(f"{' ' * 5}└[{G}•{RS}] {C}User Profile Photo {Y}:{RS} {CNETS_PHOTO.attrs['src']}")

    elif CNET_URL_Request.status_code == 404:
        print(f"\n[{B} CNET{RS} ]")
        print(f"{' ' * 5}└[{R}•{RS}] {C}User Info{Y}:{RS} {R}Not Found ❗️{RS}")

    # [ COROFLOT ]

    COROFLOT_URL = f"https://www.coroflot.com/{usernames}/profile"

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.33',
    }

    COROFLOT_URL_Request = requests.request("GET", COROFLOT_URL, headers=headers)

    if COROFLOT_URL_Request.status_code == 200:

        print(f"\n[{B} COROFLOT{RS} ]")

        print(f"{' ' * 5}└[{R}•{RS}] {C}User Url {Y}:{RS} {COROFLOT_URL}")

        COROFLOT_Soup = BeautifulSoup(COROFLOT_URL_Request.text, "html.parser")

        COROFLOT_NAME = COROFLOT_Soup.find('div', attrs={'class': 'right_side'}).find('h1',
                                                                                      attrs={'class': 'name_full'})
        COROFLOT_LOCATION = COROFLOT_Soup.find('div', attrs={'class': 'right_side'}).find('div',
                                                                                          attrs={'class': 'location'})
        COROFLOT_JOIN = COROFLOT_Soup.find('div', attrs={'class': 'member_since_block'})

        if (not COROFLOT_NAME):
            print(f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            SPACE_REMOVE = COROFLOT_NAME.get_text()
            SPACE_REMOVE_RESULT = SPACE_REMOVE.strip()
            print(f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {SPACE_REMOVE_RESULT}")

        if (not COROFLOT_LOCATION):
            print(f"{' ' * 5}└[{Y}•{RS}] {C}User Location {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(f"{' ' * 5}└[{Y}•{RS}] {C}User Location {Y}:{RS} {COROFLOT_LOCATION.getText()}")

        if (not COROFLOT_JOIN):
            print(f"{' ' * 5}└[{G}•{RS}] {C}User Joined {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            SPACE_REMOVE = COROFLOT_JOIN.get_text()
            SPACE_REMOVE_RESULT = SPACE_REMOVE.strip()
            print(f"{' ' * 5}└[{G}•{RS}] {C}User Joined {Y}:{RS} {SPACE_REMOVE_RESULT}")

    elif COROFLOT_URL_Request.status_code == 404:
        print(f"\n[{B} COROFLOT{RS} ]")
        print(f"{' ' * 5}└[{R}•{RS}] {C}User Info{Y}:{RS} {R}Not Found ❗️{RS}")

    # [ COMMUNITY CRYPTOMATOR ]

    COMMUNITY_CRYPTOMATOR_Url = f"https://community.cryptomator.org/u/{usernames}/summary"

    COMMUNITY_CRYPTOMATOR_Request = requests.get(COMMUNITY_CRYPTOMATOR_Url)

    if COMMUNITY_CRYPTOMATOR_Request.status_code == 200:

        print(f"\n[{B} COMMUNITY CRYPTOMATOR{RS} ]")

        print(f"{' ' * 5}└[{R}•{RS}] {C}User Url{Y}:{RS} {COMMUNITY_CRYPTOMATOR_Url}")

        COMMUNITY_CRYPTOMATOR_Soup = BeautifulSoup(COMMUNITY_CRYPTOMATOR_Request.text, "html.parser")

        COMMUNITY_CRYPTOMATOR_NAME = COMMUNITY_CRYPTOMATOR_Soup.find('div', attrs={'class': 'user-crawler'})

        COMMUNITY_CRYPTOMATOR_DESCRIPTION = COMMUNITY_CRYPTOMATOR_Soup.find('meta', property="og:description")

        COMMUNITY_CRYPTOMATOR_PHOTO = COMMUNITY_CRYPTOMATOR_Soup.find('meta', property="og:image")

        if (not COMMUNITY_CRYPTOMATOR_NAME):
            print(f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(
                f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {COMMUNITY_CRYPTOMATOR_NAME.find('h2', attrs={'class': 'username'}).getText()}")

        if (not COMMUNITY_CRYPTOMATOR_DESCRIPTION):
            print(f"{' ' * 5}└[{Y}•{RS}] {C}User Description {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(f"{' ' * 5}└[{Y}•{RS}] {C}User Description {Y}:{RS} {COMMUNITY_CRYPTOMATOR_DESCRIPTION['content']}")

        if (not COMMUNITY_CRYPTOMATOR_PHOTO):
            print(f"{' ' * 5}└[{G}•{RS}] {C}User Description {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(f"{' ' * 5}└[{G}•{RS}] {C}User Description {Y}:{RS} {COMMUNITY_CRYPTOMATOR_PHOTO['content']}")


    elif COMMUNITY_CRYPTOMATOR_Request.status_code == 404:
        print(f"\n[{B} COMMUNITY CRYPTOMATOR{RS} ]")
        print(f"{' ' * 5}└[{R}•{RS}] {C}User Info{Y}:{RS} {R}Not Found ❗️{RS}")

    # [ DEV.TO ]

    DEV_TO_Url = f"https://dev.to/{usernames}"

    DEV_TO_Request = requests.get(DEV_TO_Url)

    if DEV_TO_Request.status_code == 200:

        print(f"\n[{B} DEV.TO{RS} ]")

        print(f"{' ' * 5}└[{R}•{RS}] {C}User Url{Y}:{RS} {DEV_TO_Url}")

        DEV_TO_Soup = BeautifulSoup(DEV_TO_Request.text, "html.parser")

        DEV_TO_NAME = DEV_TO_Soup.find('div', attrs={'class': 'profile-header__details'})

        DEV_TO_BIO = DEV_TO_Soup.find("meta", property="og:description")

        DEV_TO_WEBSITE = DEV_TO_Soup.find('div', attrs={'class': 'profile-header__meta'}).find('a').find('span')

        if (not DEV_TO_NAME):
            print(f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(
                f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {DEV_TO_NAME.find('h1', attrs={'class': 'crayons-title fw-heavy mb-2'}).getText()}")

        if (not DEV_TO_BIO):
            print(f"{' ' * 5}└[{Y}•{RS}] {C}User Bio {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(f"{' ' * 5}└[{Y}•{RS}] {C}User Bio {Y}:{RS} {DEV_TO_BIO['content']}")

        if (not DEV_TO_WEBSITE):
            print(f"{' ' * 5}└[{G}•{RS}] {C}User Website {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            space_remove = DEV_TO_WEBSITE.getText()
            After_remove_space = space_remove.strip()
            print(f"{' ' * 5}└[{G}•{RS}] {C}User Website {Y}:{RS} {After_remove_space}")

    elif DEV_TO_Request.status_code == 404:
        print(f"\n[{B} DEV.TO{RS} ]")
        print(f"{' ' * 5}└[{R}•{RS}] {C}User Info{Y}:{RS} {R}Not Found ❗️{RS}")

    input(f"\n[{G} NOTE {RS}]{RS} USER {C}VPN{RS} TO SEARCH {R}USERNAME{RS} PORN SITE {B} PRESS ENTER {RS}")

    # [ X VIDEOS ]

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.33',
    }

    xvideos_Url = f"https://www.xvideos.com/profiles/{usernames}#_tabAboutMe"

    xvideos_Request = requests.request("GET", xvideos_Url, headers=headers)

    if xvideos_Request.status_code == 200:
        print(f"\n[{B} X VIDEOS{RS} ]")
        print(f"{' ' * 5}└[{R}•{RS}] {C}User Url{Y}:{RS} {xvideos_Url}")
        xvideos_Soup = BeautifulSoup(xvideos_Request.text, "html.parser")

        XVIDEO_USER_NAME = xvideos_Soup.find('div', attrs={'id': 'profile-title'}).find('h2').find('strong')
        XVIDEO_USER_Gender = xvideos_Soup.find('div', attrs={'id': 'pfinfo-col-col1'}).find('p',
                                                                                            attrs={'id': 'pinfo-sex'})
        XVIDEO_USER_Age = xvideos_Soup.find('div', attrs={'id': 'pfinfo-col-col1'}).find('p', attrs={'id': 'pinfo-age'})
        XVIDEO_USER_Country = xvideos_Soup.find('div', attrs={'id': 'pfinfo-col-col1'}).find('p', attrs={
            'id': 'pinfo-country'})
        XVIDEO_USER_profile_hits = xvideos_Soup.find('div', attrs={'id': 'pfinfo-col-col1'}).find('p', attrs={
            'id': 'pinfo-profile-hits'})
        XVIDEO_USER_subscribers = xvideos_Soup.find('div', attrs={'id': 'pfinfo-col-col1'}).find('p', attrs={
            'id': 'pinfo-subscribers'})
        XVIDEO_USER_signedup = xvideos_Soup.find('div', attrs={'id': 'pfinfo-col-col1'}).find('p', attrs={
            'id': 'pinfo-signedup'})
        XVIDEO_USER_lastactivity = xvideos_Soup.find('div', attrs={'id': 'pfinfo-col-col1'}).find('p', attrs={
            'id': 'pinfo-lastactivity'})
        XVIDEO_USER_City = xvideos_Soup.find('div', attrs={'id': 'pfinfo-col-col1'}).find('p',
                                                                                          attrs={'id': 'pinfo-city'})

        # Personal information

        XVIDEO_USER_languages = xvideos_Soup.find('div', attrs={'id': 'pfinfo-col-col1'}).find('p', attrs={
            'id': 'pinfo-languages'})
        XVIDEO_USER_seeking = xvideos_Soup.find('div', attrs={'id': 'pfinfo-col-col1'}).find('p', attrs={
            'id': 'pinfo-seeking'})
        XVIDEO_USER_relationship = xvideos_Soup.find('div', attrs={'id': 'pfinfo-col-col1'}).find('p', attrs={
            'id': 'pinfo-relationship'})
        XVIDEO_USER_kids = xvideos_Soup.find('div', attrs={'id': 'pfinfo-col-col1'}).find('p',
                                                                                          attrs={'id': 'pinfo-kids'})
        XVIDEO_USER_education = xvideos_Soup.find('div', attrs={'id': 'pfinfo-col-col1'}).find('p', attrs={
            'id': 'pinfo-education'})
        XVIDEO_USER_religion = xvideos_Soup.find('div', attrs={'id': 'pfinfo-col-col1'}).find('p', attrs={
            'id': 'pinfo-religion'})
        XVIDEO_USER_smoking = xvideos_Soup.find('div', attrs={'id': 'pfinfo-col-col1'}).find('p', attrs={
            'id': 'pinfo-smoking'})
        XVIDEO_USER_drinking = xvideos_Soup.find('div', attrs={'id': 'pfinfo-col-col1'}).find('p', attrs={
            'id': 'pinfo-drinking'})

        # Physical Information

        XVIDEO_USER_ethnicity = xvideos_Soup.find('div', attrs={'id': 'pfinfo-col-col2'}).find('p', attrs={
            'id': 'pinfo-ethnicity'})
        XVIDEO_USER_body = xvideos_Soup.find('div', attrs={'id': 'pfinfo-col-col2'}).find('p',
                                                                                          attrs={'id': 'pinfo-body'})
        XVIDEO_USER_height = xvideos_Soup.find('div', attrs={'id': 'pfinfo-col-col2'}).find('p', attrs={
            'id': 'pinfo-height'})
        XVIDEO_USER_weight = xvideos_Soup.find('div', attrs={'id': 'pfinfo-col-col2'}).find('p', attrs={
            'id': 'pinfo-weight'})
        XVIDEO_USER_hair_length = xvideos_Soup.find('div', attrs={'id': 'pfinfo-col-col2'}).find('p', attrs={
            'id': 'pinfo-hair_length'})
        XVIDEO_USER_hair_color = xvideos_Soup.find('div', attrs={'id': 'pfinfo-col-col2'}).find('p', attrs={
            'id': 'pinfo-hair_color'})
        XVIDEO_USER_eyes_color = xvideos_Soup.find('div', attrs={'id': 'pfinfo-col-col2'}).find('p', attrs={
            'id': 'pinfo-eyes_color'})

        XVIDEO_USER_tags = xvideos_Soup.find('div', attrs={'id': 'pfinfo-col-col2'}).find('p',
                                                                                          attrs={'id': 'pinfo-tags'})
        XVIDEO_USER_aboutme = xvideos_Soup.find('div', attrs={'id': 'pfinfo-col-col2'}).find('p', attrs={
            'id': 'pinfo-aboutme'})

        if (not XVIDEO_USER_NAME):
            print(f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {XVIDEO_USER_NAME.string}")

        if (not XVIDEO_USER_Gender):
            print(f"{' ' * 5}└[{Y}•{RS}] {C}User Gender {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(f"{' ' * 5}└[{Y}•{RS}] {C}User Gender {Y}:{RS} {XVIDEO_USER_Gender.find('span').string}")

        if (not XVIDEO_USER_Age):
            print(f"{' ' * 5}└[{G}•{RS}] {C}User Age {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(f"{' ' * 5}└[{G}•{RS}] {C}User Age {Y}:{RS} {XVIDEO_USER_Age.find('span').string} ")

        if (not XVIDEO_USER_Country):
            print(f"{' ' * 5}└[{G}•{RS}] {C}User Country {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(f"{' ' * 5}└[{G}•{RS}] {C}User Country {Y}:{RS} {XVIDEO_USER_Country.find('span').string}")

        if (not XVIDEO_USER_City):
            print(f"{' ' * 5}└[{R}•{RS}] {C}User City {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(f"{' ' * 5}└[{R}•{RS}] {C}User City {Y}:{RS} {XVIDEO_USER_City.find('span').string}")

        if (not XVIDEO_USER_profile_hits):
            print(f"{' ' * 5}└[{B}•{RS}] {C}User Profile Hits {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(
                f"{' ' * 5}└[{B}•{RS}] {C}User Profile Hits {Y}:{RS} {XVIDEO_USER_profile_hits.find('span').string}")

        if (not XVIDEO_USER_subscribers):
            print(f"{' ' * 5}└[{Y}•{RS}] {C}User Subscribers {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(
                f"{' ' * 5}└[{Y}•{RS}] {C}User Subscribers {Y}:{RS} {XVIDEO_USER_subscribers.find('span').string}")

        if (not XVIDEO_USER_signedup):
            print(f"{' ' * 5}└[{G}•{RS}] {C}User Signedup Date {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(
                f"{' ' * 5}└[{G}•{RS}] {C}User Signedup Date {Y}:{RS} {XVIDEO_USER_signedup.find('span').string}")

        if (not XVIDEO_USER_lastactivity):
            print(f"{' ' * 5}└[{R}•{RS}] {C}User Last activity {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(f"{' ' * 5}└[{R}•{RS}] {C}User Last activity {Y}:{RS} {XVIDEO_USER_lastactivity.find('span').string}")

        if (not XVIDEO_USER_languages):
            print(f"{' ' * 5}└[{B}•{RS}] {C}User Languages {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(f"{' ' * 5}└[{B}•{RS}] {C}User Languages {Y}:{RS} {XVIDEO_USER_languages.find('span').string}")

        print(f" \n {' ' * 5}[{G} NOTE {RS}] [ {Y}{C}Personal{Y}-{C}Information{RS} ] \n")

        if (not XVIDEO_USER_seeking):
            print(f"{' ' * 5}└[{Y}•{RS}] {C}User Seeking {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(f"{' ' * 5}└[{Y}•{RS}] {C}User Seeking {Y}:{RS} {XVIDEO_USER_seeking.find('span').string}")

        if (not XVIDEO_USER_relationship):
            print(f"{' ' * 5}└[{G}•{RS}] {C}User Relationship {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(f"{' ' * 5}└[{G}•{RS}] {C}User Relationship {Y}:{RS} {XVIDEO_USER_relationship.find('span').string}")

        if (not XVIDEO_USER_kids):
            print(f"{' ' * 5}└[{R}•{RS}] {C}User Kids {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(f"{' ' * 5}└[{R}•{RS}] {C}User Kids {Y}:{RS} {XVIDEO_USER_kids.find('span').string}")

        if (not XVIDEO_USER_education):
            print(f"{' ' * 5}└[{B}•{RS}] {C}User Education {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(f"{' ' * 5}└[{B}•{RS}] {C}User Education {Y}:{RS} {XVIDEO_USER_education.find('span').string}")

        if (not XVIDEO_USER_religion):
            print(f"{' ' * 5}└[{Y}•{RS}] {C}User Religion {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(f"{' ' * 5}└[{Y}•{RS}] {C}User Religion {Y}:{RS} {XVIDEO_USER_religion.find('span').string}")

        if (not XVIDEO_USER_smoking):
            print(f"{' ' * 5}└[{G}•{RS}] {C}User Smoking {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(f"{' ' * 5}└[{G}•{RS}] {C}User Smoking {Y}:{RS} {XVIDEO_USER_smoking.find('span').string}")

        if (not XVIDEO_USER_drinking):
            print(f"{' ' * 5}└[{R}•{RS}] {C}User Drinking {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(f"{' ' * 5}└[{R}•{RS}] {C}User Drinking {Y}:{RS} {XVIDEO_USER_drinking.find('span').string}")

        print(f" \n {' ' * 5}[{G} NOTE {RS}] [ {Y}{C}Physical{Y}-{C}Information{RS} ] \n")

        if (not XVIDEO_USER_ethnicity):
            print(f"{' ' * 5}└[{R}•{RS}] {C}User Ethnicity {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(f"{' ' * 5}└[{R}•{RS}] {C}User Ethnicity {Y}:{RS} {XVIDEO_USER_ethnicity.find('span').string}")

        if (not XVIDEO_USER_body):
            print(f"{' ' * 5}└[{B}•{RS}] {C}User Body {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(f"{' ' * 5}└[{B}•{RS}] {C}User Body {Y}:{RS} {XVIDEO_USER_body.find('span').string}")

        if (not XVIDEO_USER_height):
            print(f"{' ' * 5}└[{Y}•{RS}] {C}User Height {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(f"{' ' * 5}└[{Y}•{RS}] {C}User Height {Y}:{RS} {XVIDEO_USER_height.find('span').string}")

        if (not XVIDEO_USER_weight):
            print(f"{' ' * 5}└[{G}•{RS}] {C}User Weight {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(f"{' ' * 5}└[{G}•{RS}] {C}User Weight {Y}:{RS} {XVIDEO_USER_weight.find('span').string}")

        if (not XVIDEO_USER_hair_length):
            print(f"{' ' * 5}└[{R}•{RS}] {C}User Hair length {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(f"{' ' * 5}└[{R}•{RS}] {C}User Hair length {Y}:{RS} {XVIDEO_USER_hair_length.find('span').string}")

        if (not XVIDEO_USER_hair_color):
            print(f"{' ' * 5}└[{B}•{RS}] {C}User Hair color {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(f"{' ' * 5}└[{B}•{RS}] {C}User Hair color {Y}:{RS} {XVIDEO_USER_hair_color.find('span').string}")

        if (not XVIDEO_USER_eyes_color):
            print(f"{' ' * 5}└[{Y}•{RS}] {C}User Eyes color {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(f"{' ' * 5}└[{Y}•{RS}] {C}User Eyes color {Y}:{RS} {XVIDEO_USER_eyes_color.find('span').string}")

        if (not XVIDEO_USER_tags):
            print(f"{' ' * 5}└[{R}•{RS}] {C}User Interests {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(f"{' ' * 5}└[{R}•{RS}] {C}User Interests {Y}:{RS} {XVIDEO_USER_tags.find('span').string}")

        if (not XVIDEO_USER_aboutme):
            print(f"{' ' * 5}└[{B}•{RS}] {C}User About Me {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(f"{' ' * 5}└[{B}•{RS}] {C}User About Me {Y}:{RS} {XVIDEO_USER_aboutme.getText()}")


    elif xvideos_Request.status_code == 404:
        print(f"\n[{B} X VIDEOS{RS} ]")
        print(f"{' ' * 5}└[{R}•{RS}] {C}User Info{Y}:{RS} {R}Not Found ❗️{RS}")

    # [ X HAMSTER ]

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.33',
    }

    XHAMSTER_Url = f"https://xhamster.com/users/{usernames}"

    XHAMSTER_Request = requests.request("GET", XHAMSTER_Url, headers=headers)

    if XHAMSTER_Request.status_code == 200:
        print(f"\n[{B} X HAMSTER{RS} ]")
        print(f"{' ' * 5}└[{R}•{RS}] {C}User Url{Y}:{RS} {XHAMSTER_Url}")
        XHAMSTER_Soup = BeautifulSoup(XHAMSTER_Request.text, "html.parser")

        # Personal information

        XHAMSTER_USER_NAME = XHAMSTER_Soup.find('div', attrs={'class': 'user-name'})
        XHAMSTER_USER_IAM = XHAMSTER_Soup.find('div', attrs={'class': 'personal-info-block info-block'}).find('div',
                                                                                                              attrs={
                                                                                                                  'class': 'content-container'}).find(
            'div', attrs={'class': 'info-row i-am'})
        XHAMSTER_USER_FROM = XHAMSTER_Soup.find('div', attrs={'class': 'personal-info-block info-block'}).find('div',
                                                                                                               attrs={
                                                                                                                   'class': 'content-container'}).find(
            'div', attrs={'class': 'info-row from'})
        XHAMSTER_USER_seeking = XHAMSTER_Soup.find('div', attrs={'class': 'personal-info-block info-block'}).find('div',
                                                                                                                  attrs={
                                                                                                                      'class': 'content-container'}).find(
            'div', attrs={'class': 'info-row seeking'})
        XHAMSTER_USER_FETISHES = XHAMSTER_Soup.find('div', attrs={'class': 'personal-info-block info-block'}).find(
            'div', attrs={'class': 'content-container'}).find('div', attrs={'class': 'info-row fetishes'})
        XHAMSTER_USER_EDUCATION = XHAMSTER_Soup.find('div', attrs={'class': 'personal-info-block info-block'}).find(
            'div', attrs={'class': 'content-container'}).find('div', attrs={'class': 'info-row education'})
        XHAMSTER_USER_OCCUPATION = XHAMSTER_Soup.find('div', attrs={'class': 'personal-info-block info-block'}).find(
            'div', attrs={'class': 'content-container'}).find('div', attrs={'class': 'info-row occupation'})
        XHAMSTER_USER_INCOME = XHAMSTER_Soup.find('div', attrs={'class': 'personal-info-block info-block'}).find('div',
                                                                                                                 attrs={
                                                                                                                     'class': 'content-container'}).find(
            'div', attrs={'class': 'info-row income'})
        XHAMSTER_USER_RELATIONS = XHAMSTER_Soup.find('div', attrs={'class': 'personal-info-block info-block'}).find(
            'div', attrs={'class': 'content-container'}).find('div', attrs={'class': 'info-row relations'})
        XHAMSTER_USER_kids = XHAMSTER_Soup.find('div', attrs={'class': 'personal-info-block info-block'}).find('div',
                                                                                                               attrs={
                                                                                                                   'class': 'content-container'}).find(
            'div', attrs={'class': 'info-row kids'})
        XHAMSTER_USER_religion = XHAMSTER_Soup.find('div', attrs={'class': 'personal-info-block info-block'}).find(
            'div', attrs={'class': 'content-container'}).find('div', attrs={'class': 'info-row religion'})
        XHAMSTER_USER_smoking = XHAMSTER_Soup.find('div', attrs={'class': 'personal-info-block info-block'}).find('div',
                                                                                                                  attrs={
                                                                                                                      'class': 'content-container'}).find(
            'div', attrs={'class': 'info-row smoking'})
        XHAMSTER_USER_alcohol = XHAMSTER_Soup.find('div', attrs={'class': 'personal-info-block info-block'}).find('div',
                                                                                                                  attrs={
                                                                                                                      'class': 'content-container'}).find(
            'div', attrs={'class': 'info-row alcohol'})
        XHAMSTER_USER_drugs = XHAMSTER_Soup.find('div', attrs={'class': 'personal-info-block info-block'}).find('div',
                                                                                                                attrs={
                                                                                                                    'class': 'content-container'}).find(
            'div', attrs={'class': 'info-row drugs'})
        XHAMSTER_USER_star_sign = XHAMSTER_Soup.find('div', attrs={'class': 'personal-info-block info-block'}).find(
            'div', attrs={'class': 'content-container'}).find('div', attrs={'class': 'info-row star_sign'})
        XHAMSTER_USER_star_ethnicity = XHAMSTER_Soup.find('div',
                                                          attrs={'class': 'personal-info-block info-block'}).find('div',
                                                                                                                  attrs={
                                                                                                                      'class': 'content-container'}).find(
            'div', attrs={'class': 'info-row ethnicity'})
        XHAMSTER_USER_star_body = XHAMSTER_Soup.find('div', attrs={'class': 'personal-info-block info-block'}).find(
            'div', attrs={'class': 'content-container'}).find('div', attrs={'class': 'info-row body'})
        XHAMSTER_USER_star_hairLength = XHAMSTER_Soup.find('div',
                                                           attrs={'class': 'personal-info-block info-block'}).find(
            'div', attrs={'class': 'content-container'}).find('div', attrs={'class': 'info-row hairLength'})
        XHAMSTER_USER_star_eyeColor = XHAMSTER_Soup.find('div', attrs={'class': 'personal-info-block info-block'}).find(
            'div', attrs={'class': 'content-container'}).find('div', attrs={'class': 'info-row eyeColor'})
        XHAMSTER_USER_star_height = XHAMSTER_Soup.find('div', attrs={'class': 'personal-info-block info-block'}).find(
            'div', attrs={'class': 'content-container'}).find('div', attrs={'class': 'info-row height'})
        XHAMSTER_USER_Profile_subscribers_comments_etc = XHAMSTER_Soup.find_all('div', attrs={'class': 'details-row'})

        if (not XHAMSTER_USER_NAME):
            print(f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(
                f"{' ' * 5}└[{B}•{RS}] {C}User Profile Name {Y}:{RS} {XHAMSTER_USER_NAME.find('div', attrs={'class': 'value'}).string}")

        if (not XHAMSTER_USER_Profile_subscribers_comments_etc):
            print(f"{' ' * 5}└[{Y}•{RS}] {C}User Rank {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            space_remove = XHAMSTER_USER_Profile_subscribers_comments_etc[1].getText()
            After_remove_space = space_remove.strip()
            print(f"{' ' * 5}└[{Y}•{RS}] {C}User Rank {Y}:{RS} {After_remove_space}")

        if (not XHAMSTER_USER_Profile_subscribers_comments_etc):
            print(f"{' ' * 5}└[{G}•{RS}] {C}User Registration Date {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            space_remove = XHAMSTER_USER_Profile_subscribers_comments_etc[2].getText()
            After_remove_space = space_remove.strip()
            print(f"{' ' * 5}└[{G}•{RS}] {C}User Registration Date {Y}:{RS} {After_remove_space}")

        if (not XHAMSTER_USER_Profile_subscribers_comments_etc):
            print(f"{' ' * 5}└[{R}•{RS}] {C}User View {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            space_remove = XHAMSTER_USER_Profile_subscribers_comments_etc[3].getText()
            After_remove_space = space_remove.strip()
            print(f"{' ' * 5}└[{R}•{RS}] {C}User View {Y}:{RS} {After_remove_space}")

        if (not XHAMSTER_USER_Profile_subscribers_comments_etc):
            print(f"{' ' * 5}└[{B}•{RS}] {C}User Subscribers {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            space_remove = XHAMSTER_USER_Profile_subscribers_comments_etc[4].getText()
            After_remove_space = space_remove.strip()
            print(f"{' ' * 5}└[{B}•{RS}] {C}User Subscribers {Y}:{RS} {After_remove_space}")

        if (not XHAMSTER_USER_Profile_subscribers_comments_etc):
            print(f"{' ' * 5}└[{Y}•{RS}] {C}User Comments {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            space_remove = XHAMSTER_USER_Profile_subscribers_comments_etc[5].getText()
            After_remove_space = space_remove.strip()
            print(f"{' ' * 5}└[{Y}•{RS}] {C}User Comments {Y}:{RS} {After_remove_space}")

        print(f" \n {' ' * 5}[{G} NOTE {RS}] [ {Y}{C}Personal{Y}-{C}Information{RS} ] \n")

        if (not XHAMSTER_USER_IAM):
            print(f"{' ' * 5}└[{Y}•{RS}] {C}User I am {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(
                f"{' ' * 5}└[{Y}•{RS}] {C}User I am {Y}:{RS} {XHAMSTER_USER_IAM.find('div', attrs={'class': 'value'}).getText()}")

        if (not XHAMSTER_USER_FROM):
            print(f"{' ' * 5}└[{G}•{RS}] {C}User From {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(
                f"{' ' * 5}└[{G}•{RS}] {C}User From {Y}:{RS} {XHAMSTER_USER_FROM.find('div', attrs={'class': 'value'}).getText()}")

        if (not XHAMSTER_USER_seeking):
            print(f"{' ' * 5}└[{R}•{RS}] {C}User Seeking {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            seeking_space_remove = XHAMSTER_USER_seeking.find('div', attrs={'class': 'value'}).getText()
            After_remove_seeking_space = seeking_space_remove.strip()
            print(f"{' ' * 5}└[{R}•{RS}] {C}User Seeking {Y}:{RS} {After_remove_seeking_space}")

        if (not XHAMSTER_USER_FETISHES):
            print(f"{' ' * 5}└[{B}•{RS}] {C}User Fetishes {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            print(
                f"{' ' * 5}└[{B}•{RS}] {C}User Fetishes {Y}:{RS} {XHAMSTER_USER_FETISHES.find('div', attrs={'class': 'value'}).getText()}")

        if (not XHAMSTER_USER_EDUCATION):
            print(f"{' ' * 5}└[{Y}•{RS}] {C}User Education {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            EDUCATION_space_remove = XHAMSTER_USER_EDUCATION.find('div', attrs={'class': 'value'}).getText()
            After_remove_EDUCATION_space = EDUCATION_space_remove.strip()
            print(f"{' ' * 5}└[{Y}•{RS}] {C}User Education {Y}:{RS} {After_remove_EDUCATION_space}")

        if (not XHAMSTER_USER_OCCUPATION):
            print(f"{' ' * 5}└[{G}•{RS}] {C}User Occupation {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            OCCUPATION_space_remove = XHAMSTER_USER_OCCUPATION.find('div', attrs={'class': 'value'}).getText()
            After_remove_OCCUPATION_space = OCCUPATION_space_remove.strip()
            print(f"{' ' * 5}└[{G}•{RS}] {C}User Occupation {Y}:{RS} {After_remove_OCCUPATION_space}")

        if (not XHAMSTER_USER_INCOME):
            print(f"{' ' * 5}└[{R}•{RS}] {C}User Income {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            space_remove = XHAMSTER_USER_INCOME.find('div', attrs={'class': 'value'}).getText()
            After_remove_space = space_remove.strip()
            print(f"{' ' * 5}└[{R}•{RS}] {C}User Income {Y}:{RS} {After_remove_space}")

        if (not XHAMSTER_USER_RELATIONS):
            print(f"{' ' * 5}└[{B}•{RS}] {C}User Relationship {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            space_remove = XHAMSTER_USER_RELATIONS.find('div', attrs={'class': 'value'}).getText()
            After_remove_space = space_remove.strip()
            print(f"{' ' * 5}└[{B}•{RS}] {C}User Relationship {Y}:{RS} {After_remove_space}")

        if (not XHAMSTER_USER_kids):
            print(f"{' ' * 5}└[{Y}•{RS}] {C}User Kids {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            space_remove = XHAMSTER_USER_kids.find('div', attrs={'class': 'value'}).getText()
            After_remove_space = space_remove.strip()
            print(f"{' ' * 5}└[{Y}•{RS}] {C}User Kids {Y}:{RS} {After_remove_space}")

        if (not XHAMSTER_USER_religion):
            print(f"{' ' * 5}└[{G}•{RS}] {C}User Religion {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            space_remove = XHAMSTER_USER_religion.find('div', attrs={'class': 'value'}).getText()
            After_remove_space = space_remove.strip()
            print(f"{' ' * 5}└[{G}•{RS}] {C}User Religion {Y}:{RS} {After_remove_space}")

        if (not XHAMSTER_USER_smoking):
            print(f"{' ' * 5}└[{R}•{RS}] {C}User Smoking {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            space_remove = XHAMSTER_USER_smoking.find('div', attrs={'class': 'value'}).getText()
            After_remove_space = space_remove.strip()
            print(f"{' ' * 5}└[{R}•{RS}] {C}User Smoking {Y}:{RS} {After_remove_space}")

        if (not XHAMSTER_USER_alcohol):
            print(f"{' ' * 5}└[{B}•{RS}] {C}User Drinking {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            space_remove = XHAMSTER_USER_alcohol.find('div', attrs={'class': 'value'}).getText()
            After_remove_space = space_remove.strip()
            print(f"{' ' * 5}└[{B}•{RS}] {C}User Drinking {Y}:{RS} {After_remove_space}")

        if (not XHAMSTER_USER_drugs):
            print(f"{' ' * 5}└[{Y}•{RS}] {C}User Drugs {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            space_remove = XHAMSTER_USER_drugs.find('div', attrs={'class': 'value'}).getText()
            After_remove_space = space_remove.strip()
            print(f"{' ' * 5}└[{Y}•{RS}] {C}User Drugs {Y}:{RS} {After_remove_space}")

        if (not XHAMSTER_USER_star_sign):
            print(f"{' ' * 5}└[{G}•{RS}] {C}User Star Sign {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            space_remove = XHAMSTER_USER_star_sign.find('div', attrs={'class': 'value'}).getText()
            After_remove_space = space_remove.strip()
            print(f"{' ' * 5}└[{G}•{RS}] {C}User Star Sign {Y}:{RS} {After_remove_space}")

        # What I look like

        print(f" \n {' ' * 5}[{G} NOTE {RS}] [ {Y}{C}What I Look Like{RS} ] \n")

        if (not XHAMSTER_USER_star_ethnicity):
            print(f"{' ' * 5}└[{R}•{RS}] {C}User Ethnicity {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            space_remove = XHAMSTER_USER_star_ethnicity.find('div', attrs={'class': 'value'}).getText()
            After_remove_space = space_remove.strip()
            print(f"{' ' * 5}└[{R}•{RS}] {C}User Ethnicity {Y}:{RS} {After_remove_space}")

        if (not XHAMSTER_USER_star_body):
            print(f"{' ' * 5}└[{B}•{RS}] {C}User Body {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            space_remove = XHAMSTER_USER_star_body.find('div', attrs={'class': 'value'}).getText()
            After_remove_space = space_remove.strip()
            print(f"{' ' * 5}└[{B}•{RS}] {C}User Body {Y}:{RS} {After_remove_space}")

        if (not XHAMSTER_USER_star_hairLength):
            print(f"{' ' * 5}└[{Y}•{RS}] {C}User Hair length {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            space_remove = XHAMSTER_USER_star_hairLength.find('div', attrs={'class': 'value'}).getText()
            After_remove_space = space_remove.strip()
            print(f"{' ' * 5}└[{Y}•{RS}] {C}User Hair length {Y}:{RS} {After_remove_space}")

        if (not XHAMSTER_USER_star_eyeColor):
            print(f"{' ' * 5}└[{G}•{RS}] {C}User Eye Color {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            space_remove = XHAMSTER_USER_star_eyeColor.find('div', attrs={'class': 'value'}).getText()
            After_remove_space = space_remove.strip()
            print(f"{' ' * 5}└[{G}•{RS}] {C}User Eye Color {Y}:{RS} {After_remove_space}")

        if (not XHAMSTER_USER_star_height):
            print(f"{' ' * 5}└[{R}•{RS}] {C}User Height {Y}:{RS} {R}Not Found ❗️{RS} ")
        else:
            space_remove = XHAMSTER_USER_star_height.find('div', attrs={'class': 'value'}).getText()
            After_remove_space = space_remove.strip()
            print(f"{' ' * 5}└[{R}•{RS}] {C}User Height {Y}:{RS} {After_remove_space}")


    elif XHAMSTER_Request.status_code == 404:
        print(f"\n[{B} X HAMSTER{RS} ]")
        print(f"{' ' * 5}└[{R}•{RS}] {C}User Info{Y}:{RS} {R}Not Found ❗️{RS}")
