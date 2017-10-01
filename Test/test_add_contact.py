# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact (Firstname="First", Middlename="Middle", Lastname="Last", Nickname="Nick", Title="Title",
                        Company="Company", Address="Address", Home="11231414", Mobile="123123123", Work="143432423",
                        Fax="345", Email="ewrwer", Email2="weteww", Email3="ytrrrr", Homepage="fsfsfsfs",
                        Bday="3", Bmonth="March", Byear="1979", Aday="10", Amonth="September", Ayear="2017",
                        Address2="sdfsdfdfsd", Phone2="dfsdfsds", Notes="sdfsdfsdfdsf"))


def test_add_empty_contact(app):
    app.contact.create(Contact(Firstname="", Middlename="", Lastname="", Nickname="", Title="",
                       Company="", Address="", Home="", Mobile="", Work="",
                       Fax="", Email="", Email2="", Email3="", Homepage="",
                       Bday="", Bmonth="", Byear="", Aday="", Amonth="", Ayear="",
                       Address2="", Phone2="", Notes=""))




