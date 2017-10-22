import re

def test_phones_on_home_page(app):
    contact_from_home_page=app.contact.get_contact_list()[0]
    contact_from_edit_page=app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.Home == contact_from_edit_page.Home
    assert contact_from_view_page.Mobile == contact_from_edit_page.Mobile
    assert contact_from_view_page.Work == contact_from_edit_page.Work
    assert contact_from_view_page.Phone2 == contact_from_edit_page.Phone2

def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,[contact.Home, contact.Mobile, contact.Work, contact.Phone2]))))