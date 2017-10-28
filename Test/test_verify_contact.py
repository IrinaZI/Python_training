import re
from random import randrange

def test_data_on_some_contact(app):
    contacts = app.contact.get_contact_list()
    index = randrange(len(contacts))
    contact_from_home_page=app.contact.get_contact_list()[index]
    contact_from_edit_page=app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.Firstname == contact_from_edit_page.Firstname
    assert contact_from_home_page.Lastname == contact_from_edit_page.Lastname
    assert contact_from_home_page.all_address_from_home_page == contact_from_edit_page.all_address_from_home_page
    assert contact_from_home_page.all_emails == merge_email_like_on_home_page(contact_from_edit_page)


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,[contact.Home, contact.Mobile, contact.Work, contact.Phone2]))))

def clear_email(s):
    return re.sub(" ", "", s)

def merge_email_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear_email(x),
                                filter(lambda x: x is not None,[contact.Email, contact.Email2, contact.Email3]))))