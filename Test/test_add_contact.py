# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application
from model.contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.Login(username="admin", password="secret")
    app.create_contact(Contact (Firstname="First", Middlename="Middle", Lastname="Last", Nickname="Nick", Title="Title",
                            Company="Company", Address="Address", Home="11231414",Mobile="123123123", Work="143432423",
                            Fax="345", Email="ewrwer", Email2="weteww", Email3="ytrrrr", Homepage="fsfsfsfs",
                            Bday="3", Bmonth="March", Byear="1979", Aday="10", Amonth="September", Ayear="2017",
                            Address2="sdfsdfdfsd", Phone2="dfsdfsds", Notes="sdfsdfsdfdsf"))
    app.session.Logout()

def test_add_empty_contact(app):
    app.session.Login( username="admin", password="secret")
    app.create_contact( Contact(Firstname="", Middlename="", Lastname="", Nickname="", Title="",
                            Company="", Address="", Home="",Mobile="", Work="",
                            Fax="", Email="", Email2="", Email3="", Homepage="",
                            Bday="", Bmonth="", Byear="", Aday="", Amonth="", Ayear="",
                            Address2="", Phone2="", Notes=""))
    app.session.Logout()



