from model.group import Group
from model.contact import Contact
from fixture.orm import ORMFixture
import random



def test_add_contact_in_group(app, db, check_ui):
    db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
    if len (db.get_group_list()) == 0:
        app.group.create(Group(name='test'))
    if app.contact.count() == 0:
        app.contact.create (Contact(Firstname="New_name", Lastname="NewLname"))
    old_groups = db.get_group_list()
    gt = random.choice(old_groups)
    group_name=gt.name
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    contact_id=contact.id
    app.contact.add_contact_in_group(contact_id, group_name)
    new_contacts = db.get_contact_list()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),

                                                                             key=Contact.id_or_max)