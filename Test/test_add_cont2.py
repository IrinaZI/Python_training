# -*- coding: utf-8 -*-
from model.contact import Contact




def test_add_contact(app, date_contacts):
    contact=date_contacts
    old_contacts = app.contact.get_contact_list()
    #contact = Contact (Firstname="First", Middlename="Middle", Lastname="Last", Nickname="Nick", Title="Title",
                        #Company="Company", Address="Address", Home="11231414", Mobile="123123123", Work="143432423",
                        #Fax="345", Email="ewrwer", Email2="weteww", Email3="ytrrrr", Homepage="fsfsfsfs",
                        #Bday="3", Bmonth="March", Byear="1979", Aday="10", Amonth="September", Ayear="2017",
                        #Address2="sdfsdfdfsd", Phone2="dfsdfsds", Notes="sdfsdfsdfdsf")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
