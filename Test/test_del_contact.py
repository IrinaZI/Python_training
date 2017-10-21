from model.contact import Contact
from random import randrange

def test_delete_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(Firstname="Test", Middlename="", Lastname="", Nickname="", Title="",
                       Company="", Address="", Home="", Mobile="", Work="",
                       Fax="", Email="", Email2="", Email3="", Homepage="",
                       Bday="", Bmonth="", Byear="", Aday="", Amonth="", Ayear="",
                       Address2="", Phone2="", Notes=""))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == app.contact.count()
    old_contacts[index:index + 1] = []
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)