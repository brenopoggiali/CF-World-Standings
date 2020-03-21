import requests
from bs4 import BeautifulSoup
from login import login, get_csrf

# Global Variables #
cf_url = "https://codeforces.com"
lists_url = "https://codeforces.com/lists"
new_list_url = "https://codeforces.com/lists/new"

def get_page(session, url):
	request = session.get(url)
	plain = request.text
	page = BeautifulSoup(plain, "html.parser")
	return page

def get_lists_table(session):
	page = get_page(session, lists_url)
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

def create_lists(session, countries_dict):
	table = get_lists_table(session)
	lists_urls = get_lists_urls(table)
	countries_list = []
	for country in countries_dict:
		if country not in lists_urls and len(countries_dict[country]) >= 5:
			request = session.get(new_list_url)
			csrf = get_csrf(request)
			n = session.post(new_list_url, data={ 'csrf_token': csrf, 'action': 'saveList', 'englishName': country, '_tta': 90 })
			countries_list.append(country)
			print(f"\tList of {country} created! {n}")

def populate_list(session, handles, list_url):
	request = session.get(list_url)
	csrf = get_csrf(request)
	params = {'csrf_token': csrf, 'action': 'addMembers', 'handlesToAdd': handles }
	session.post(list_url, data=params)

def populate_lists(session, countries_dict):
	table = get_lists_table(session)
	lists_urls = get_lists_urls(table)
	for country in lists_urls:
		if country in countries_dict:
			handles = ' '.join(countries_dict[country])
			populate_list(session, handles, lists_urls[country])
			print(f"\tList of {country} populated!")

if __name__ == "__main__":
	login()
