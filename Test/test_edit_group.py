# -*- coding: utf-8 -*-
from model.group import Group
import random
import pytest

def test_modify_some_group_name(app, db, check_ui):
    with pytest.allure.step('Given a non-empty group list'):
        if len (db.get_group_list()) == 0:
            app.group.create(Group(name='test'))
    with pytest.allure.step('Given a random group from the list'):
        old_groups = db.get_group_list()
        group = random.choice(old_groups)
    with pytest.allure.step('Edit a random group from the list'):
        edit_group = Group(name="New group")
        app.group.modify_group_by_id(edit_group, group.id)
    with pytest.allure.step('Then the new group list is equal to the old list'):
        new_groups = db.get_group_list()
        assert len(old_groups) == app.group.count()
        if check_ui:
            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)