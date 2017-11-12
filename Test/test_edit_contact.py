# -*- coding: utf-8 -*-
from model.contact import Contact
import random
import pytest

def test_modify_some_contact(app, db, check_ui):
    with pytest.allure.step('Given a non-empty contact list'):
        if app.contact.count() == 0:
            app.contact.create (Contact(Firstname="New_name", Lastname="NewLname"))
    with pytest.allure.step('Given a random contact from the list'):
        old_contacts = db.get_contact_list()
        contact = random.choice(old_contacts)
    with pytest.allure.step('Edit a random contact from the list'):
        edit_contact = Contact(Firstname="New_name", id = contact.id, Lastname = contact.Lastname)
        app.contact.modify_contact_by_id(edit_contact, contact.id)
    with pytest.allure.step('Then the new contact list is equal to the old list'):
        new_contacts = db.get_contact_list()
        assert len(old_contacts) == len(db.get_contact_list())
        if check_ui:
            assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)