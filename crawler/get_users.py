from datetime import datetime
import requests
import json

# Global Variables #
active_users_url = "https://codeforces.com/api/user.ratedList?activeOnly=false"
unknown = "Unknown"

# Static Variables #
session = requests.session()


def get_all_active_users():
    request = session.get(active_users_url)
    plain = request.text
    users_json = json.loads(plain)["result"]
    return users_json


def separate_by_country(users):
    countries = {unknown: []}
    for user in users:
        user_datetime = datetime.fromtimestamp(user["lastOnlineTimeSeconds"])
        active = (datetime.now()-user_datetime).days < 30
        active = True
        if "country" in user:
            country = user["country"]
            if country not in countries:
                countries[country] = []
            countries[country].append([active, user["rating"], user["handle"]])
        else:
            countries[unknown].append([active, user["rating"], user["handle"]])
    for country in countries:
        countries[country] = sorted(countries[country])[::-1]
    return countries
