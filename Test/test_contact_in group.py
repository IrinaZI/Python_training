from model.group import Group
from model.contact import Contact
from fixture.orm import ORMFixture
import random



def test_contact_in_group(app, db): #orm, check_ui
    db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
    if len (db.get_group_list()) == 0:
        app.group.create(Group(name='test'))
    if app.contact.count() == 0:
        app.contact.create (Contact(Firstname="New_name", Lastname="NewLname"))
    old_groups = db.get_group_list()
    gt = random.choice(old_groups)
    group_name=gt.name
    group_id=gt.id
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    contact_id=contact.id
    l1 = db.get_contacts_in_group(Group(id=int(group_id)))
    app.contact.add_contact_in_group(contact_id, group_name)
    l2 = db.get_contacts_in_group(Group(id=int(group_id)))
    assert l1 != l2
    l3 = db.get_contacts_in_group(Group(id=int(group_id)))
    app.contact.del_contact_from_group(contact_id, group_name)
    l2 = db.get_contacts_in_group(Group(id=int(group_id)))
    assert l3 != l2



        #app.contact.del_contact_from_group(contact_id, group_name)


    #if check_ui:
        #assert sorted(new_groups, key = Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)