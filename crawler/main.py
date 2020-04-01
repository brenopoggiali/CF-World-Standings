from login import login
from get_users import get_all_active_users, separate_by_country
from set_lists import create_lists, clear_lists, populate_lists

if __name__ == "__main__":
    print("Please login first\n")
    session = login()
    print("Getting Users..")
    users = get_all_active_users()
    print("Creating Dictionary..")
    countries_dict = separate_by_country(users)
    print("Creating Lists..")
    create_lists(session, countries_dict)
    print("Emptying Lists..")
    clear_lists(session)
    print("Populating Lists..")
    populate_lists(session, countries_dict)
