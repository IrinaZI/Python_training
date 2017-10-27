# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_number(prefix, maxlen):
    symbols = string.punctuation + "" + string.digits*40
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

data_cont = [Contact(Firstname=random_string("First", 10), Middlename=random_string("Middle", 10),
                         Lastname=random_string("Last", 10),
                         Nickname=random_string("Nick", 8), Title=random_string("Title", 15),
                         Company=random_string("Company", 20),
                         Address=random_string("Address", 40), Home=random_number("", 8), Mobile=random_number("", 10),
                         Work=random_number("", 10), Fax=random_number("", 10), Email=random_string("mail@", 15),
                         Email2=random_string("mail2@", 15), Email3=random_string("mail", 15),
                         Homepage=random_string("www.", 15),
                         Bday="3", Bmonth="March", Byear="1979",
                         Aday="10", Amonth="September", Ayear="2017",
                         Address2=random_string("Address", 40), Phone2=random_number("", 12),
                         Notes=random_string("Address", 70))
                 for i in range(7)]

@pytest.mark.parametrize("contact", data_cont, ids=[repr(x) for x in data_cont])
def test_add_contact(app, contact):
    #pass
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
