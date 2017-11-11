from model.group import Group
from model.contact import Contact
from fixture.orm import ORMFixture



def test_del_contact_from_group(app, db): #, orm
    relations = len(db.get_relations_list())
    if relations == 0:
        group = Group(name='000', header='111', footer='222')
        app.group.create(group)
        contact = Contact(Firstname='FTest', Lastname='LTest')
        app.contact.create_contact_with_adding_to_group(contact)
    gid = db.get_relations_list()[0].group_id
    db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
    cid = db.get_contacts_in_group(Group(id=gid))[0].id
    app.contact.remove_contact_from_group(cid, gid)
    new_contact_in_group_list = db.get_contacts_in_group(Group(id=gid))
    contact_id_list = []
    for contact in new_contact_in_group_list:
        id = contact.id
        contact_id_list.append(id)
    assert cid not in contact_id_list
