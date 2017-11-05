from model.group import Group
import random

def test_add_contact_in_group(app, db): #orm, check_ui
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    group_name=group.name
    group_id=group.id
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    contact_id=contact.id
    app.contact.add_contact_in_group(contact_id, group_name)
    app.contact.del_contact_from_group(contact_id, group_name)


    #if check_ui:
        #assert sorted(new_groups, key = Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)