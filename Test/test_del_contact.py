from model.contact import Contact
import random
import pytest

def test_delete_some_contact(app, db, check_ui):
    with pytest.allure.step('Given a non-empty contact list'):
        if len (db.get_contact_list()) == 0:
            app.contact.create(Contact(Firstname="Test", Middlename="", Lastname="", Nickname="", Title="",
                       Company="", Address="", Home="", Mobile="", Work="",
                       Fax="", Email="", Email2="", Email3="", Homepage="",
                       Bday="", Bmonth="", Byear="", Aday="", Amonth="", Ayear="",
                       Address2="", Phone2="", Notes=""))
    with pytest.allure.step('Given a random contact from the list'):
        old_contacts = db.get_contact_list()
        contact = random.choice(old_contacts)
    with pytest.allure.step('Delete a random contact from the list'):
        app.contact.delete_contact_by_id(contact.id)
    with pytest.allure.step('Then the new contacts is equal to the old list with the delete group'):
        new_contacts = app.contact.get_contact_list()
        new_contacts = db.get_contact_list()
        assert len(old_contacts) - 1 == app.contact.count()
        old_contacts.remove(contact)
        assert new_contacts == old_contacts
        if check_ui:
            assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)