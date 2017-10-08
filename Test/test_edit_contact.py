# -*- coding: utf-8 -*-
from model.contact import Contact

def test_modify_contact_Firstname(app):
    if app.contact.count() == 0:
        app.contact.create (Contact(Firstname = "New"))
    app.contact.modify_first_contact(Contact(Firstname="New_name"))