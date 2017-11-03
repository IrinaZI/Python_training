from model.contact import Contact
import random

def test_delete_some_contact(app, db, check_ui):
    if len (db.get_contact_list()) == 0:
        app.contact.create(Contact(Firstname="Test", Middlename="", Lastname="", Nickname="", Title="",
                       Company="", Address="", Home="", Mobile="", Work="",
                       Fax="", Email="", Email2="", Email3="", Homepage="",
                       Bday="", Bmonth="", Byear="", Aday="", Amonth="", Ayear="",
                       Address2="", Phone2="", Notes=""))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = app.contact.get_contact_list()
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == app.contact.count()
    old_contacts.remove(contact)
    assert new_contacts == old_contacts
    if check_ui:
       assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)