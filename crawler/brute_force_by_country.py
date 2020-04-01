import requests
from bs4 import BeautifulSoup

# Global Variables #
base_url = "https://codeforces.com/ratings/country/"
page_path = "/page/"
country = "Brazil"

# Static Variables #
session = requests.session()


def get_country_page(country, page):
    country_page_url = base_url + country + page_path + page
    request = session.get(country_page_url)
    plain = request.text
    page = BeautifulSoup(plain, "html.parser")
    return page


def get_handles(country_page):
    handles = []
    table_div = country_page.find('div', {'class': 'ratingsDatatable'})
    table = table_div.find('table')
    table_rows = table.find_all('tr')
    for row in table_rows:
        if row.find('a'):
            handle = row.find('a').text
            handles.append(handle)
    return handles


def get_top_1000_country_users(country):
    handles = []
    # Each page get 200 users
    for page in range(1, 6):
        country_page = get_country_page(country, str(page))
        handles += get_handles(country_page)
        print(f"Finish page #{page} for {country}")
    return handles


if __name__ == "__main__":
    print(get_top_1000_country_users(country))
