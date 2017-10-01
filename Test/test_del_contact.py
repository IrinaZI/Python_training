from model.contact import Contact

def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(Firstname="Test", Middlename="", Lastname="", Nickname="", Title="",
                       Company="", Address="", Home="", Mobile="", Work="",
                       Fax="", Email="", Email2="", Email3="", Homepage="",
                       Bday="", Bmonth="", Byear="", Aday="", Amonth="", Ayear="",
                       Address2="", Phone2="", Notes=""))
    app.contact.delete_first_contact()
