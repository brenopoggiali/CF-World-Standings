from bs4 import BeautifulSoup

# Global Variables #
cf_url = "https://codeforces.com"


def get_page(session, url):
    request = session.get(url)
    plain = request.text
    page = BeautifulSoup(plain, "html.parser")
    return page


def get_lists_table(session, url):
    page = get_page(session, url)
    table_div = page.find('div', {'class': 'datatable'})
    table = table_div.find('table')
    table_rows = table.find_all('tr')
    return table_rows


def get_lists_urls(table):
    urls = {}
    for row in table:
        if row.find('a'):
            country = row.find('a').text
            country_list_url = cf_url + row.find('a')['href']
            urls[country] = country_list_url
    return urls


def get_active_countries_dict(countries_dict):
    active_countries_dict = {}
    for country, users in countries_dict.items():
        active_countries_dict[country] = 0
        for user in users:
            if user[0]:
                active_countries_dict[country] += 1
    return active_countries_dict


def get_handles(country_handles):
    handles = []
    for user in country_handles[:1000]:
        handles.append(user[2])
    return handles
