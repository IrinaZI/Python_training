import re
from model.contact import Contact

def test_data_on_some_contact(app, db):
    contacts_from_home_page = app.contact.get_contact_list()
    new_contacts = db.get_contact_list()
    new_contacts = sorted(new_contacts, key=Contact.id_or_max)
    contacts_from_home_page = sorted(contacts_from_home_page, key=Contact.id_or_max)
    for i in range(len(db.get_contact_list())):
        assert contacts_from_home_page[i].all_phones_from_home_page == merge_phones_like_on_home_page(new_contacts[i])
        assert contacts_from_home_page[i].Firstname == new_contacts[i].Firstname
        assert contacts_from_home_page[i].Lastname == new_contacts[i].Lastname
        assert contacts_from_home_page[i].all_address_from_home_page == new_contacts[i].Address
        all_emails=contacts_from_home_page[i].all_emails
        assert clear_email(all_emails) == merge_email_like_on_home_page(new_contacts[i])
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

