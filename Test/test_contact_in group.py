from model.group import Group
from model.contact import Contact
from fixture.orm import ORMFixture
import random


gt = ""
#gti = 0

def test_add_contact_in_group(app, db): #orm, check_ui
    db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
    if len (db.get_group_list()) == 0:
        app.group.create(Group(name='test'))
    if app.contact.count() == 0:
        app.contact.create (Contact(Firstname="New_name", Lastname="NewLname"))
    old_groups = db.get_group_list()
    global gt
    #global gti
    gt = random.choice(old_groups)
    group_name=gt.name
    #print(gt)
    print
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    contact_id=contact.id
    print(contact_id)
    app.contact.add_contact_in_group(contact_id, group_name)
    l = db.get_contacts_in_group(Group(id=int(gt.id)))
    print (l)
    #print (contact.id)


        #app.contact.del_contact_from_group(contact_id, group_name)


    #if check_ui:
        #assert sorted(new_groups, key = Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)