from login import get_csrf
from get_lists import get_page, get_lists_table, get_lists_urls, \
                      get_active_countries_dict, get_handles

# Global Variables #
lists_url = "https://codeforces.com/lists"
new_list_url = "https://codeforces.com/lists/new"
edit_list_url = "https://codeforces.com/data/lists"


def create_lists(session, countries_dict):
    table = get_lists_table(session, lists_url)
    lists_urls = get_lists_urls(table)
    active_country_users = get_active_countries_dict(countries_dict)
    countries_list = []
    for country in countries_dict:
        if country not in lists_urls and active_country_users[country] >= 50:
            request = session.get(new_list_url)
            csrf = get_csrf(request)
            params = {'csrf_token': csrf,
                      'action': 'saveList',
                      'englishName': country,
                      '_tta': 90}
            n = session.post(new_list_url, data=params)
            countries_list.append(country)
            print(f"\tList of {country} created! {n}")
        else:
            print(f"\tList of {country} skipped!")


def clear_diff_lists(session, countries_dict):
    table = get_lists_table(session, lists_url)
    lists_urls = get_lists_urls(table)
    for country in lists_urls:
        url = lists_urls[country]
        request = session.get(url)
        csrf = get_csrf(request)
        table = get_lists_table(session, url)
        page = get_page(session, url)
        list_a = page.find('a', {'class': 'delete-user-list-link'})
        list_id = list_a["data-userlistid"]
        handles = set(get_handles(countries_dict[country]))
        count = 0
        for row in table:
            try:
                user_id = row.findAll('td')[-1]["data-userid"]
                user_handle = row.findAll('td')[1].find('a').getText()
                if user_handle in handles:
                    continue
                params = {'action': 'deleteMember',
                          'listId': list_id,
                          'userId': user_id,
                          'csrf_token': csrf}
                session.post(edit_list_url, data=params)
                count += 1
            except (KeyError, IndexError):
                pass
        print(f'\t{count} users of {country} removed!')


def populate_list(session, handles, list_url):
    request = session.get(list_url)
    csrf = get_csrf(request)
    params = {'csrf_token': csrf,
              'action': 'addMembers',
              'handlesToAdd': handles}
    session.post(list_url, data=params)


def populate_lists(session, countries_dict):
    table = get_lists_table(session, lists_url)
    lists_urls = get_lists_urls(table)
    for country in lists_urls:
        if country in countries_dict:
            handles = get_handles(countries_dict[country])
            handles = " ".join(handles)
            populate_list(session, handles, lists_urls[country])
            print(f"\tList of {country} populated!")
