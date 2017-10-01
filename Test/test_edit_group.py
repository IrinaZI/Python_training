# -*- coding: utf-8 -*-
from model.group import Group

#def test_edit_first_group(app):
#    app.session.Login(username="admin", password="secret")
#    app.group.edit_first_group(Group(name="изменили", header="изменили", footer="изменили"))
#    app.session.Logout()


def test_modify_group_name(app):
    app.group.modify_first_group(Group(name="New group"))



def test_modify_group_header(app):
    app.group.modify_first_group(Group(header="New header"))
