# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.Login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact (Firstname="Изменили", Middlename="Изменили", Lastname="Изменили", Nickname="Nick", Title="Title",
                        Company="Company", Address="Address", Home="11231414", Mobile="123123123", Work="143432423",
                        Fax="345", Email="ewrwer", Email2="weteww", Email3="ytrrrr", Homepage="fsfsfsfs",
                        Bday="3", Bmonth="March", Byear="1979", Aday="10", Amonth="September", Ayear="2017",
                        Address2="sdfsdfdfsd", Phone2="dfsdfsds", Notes="sdfsdfsdfdsf"))
    app.session.Logout()
