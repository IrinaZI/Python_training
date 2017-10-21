# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange

def test_modify_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create (Contact(Firstname="New_name", Lastname="NewLname"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(Firstname = "New_name")
    contact.id = old_contacts[index].id
    contact.Lastname = old_contacts[index].Lastname
    app.contact.modify_contact_by_index(contact, index)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == app.contact.count()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)