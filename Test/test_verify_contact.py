import re
from model.contact import Contact
from random import randrange

def test_data_on_some_contact(app, db):
    contacts_from_home_page = app.contact.get_contact_list()
    new_contacts = db.get_contact_list()
    new_contacts = sorted(new_contacts, key=Contact.id_or_max)
    contacts_from_home_page = sorted(contacts_from_home_page, key=Contact.id_or_max)

    print(contacts_from_home_page[2].all_emails)
    print(contacts_from_home_page)
    print(merge_email_like_on_home_page(new_contacts[2]))
    print(new_contacts)
    #contact_from_edit_page=app.contact.get_contact_info_from_edit_page()
    assert contacts_from_home_page[2].all_phones_from_home_page == merge_phones_like_on_home_page(new_contacts[2])
    assert contacts_from_home_page[2].Firstname == new_contacts[2].Firstname
    assert contacts_from_home_page[2].Lastname == new_contacts[2].Lastname
    assert contacts_from_home_page[2].all_address_from_home_page == new_contacts[2].Address
    assert contacts_from_home_page[2].all_emails == merge_email_like_on_home_page(new_contacts[2])
    assert sorted(new_contacts, key=Contact.id_or_max) == sorted(contacts_from_home_page, key=Contact.id_or_max)


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