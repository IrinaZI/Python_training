

class ContactHelper:
    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.open_contact_page()
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        # fill contact form
        self.fill_contact_form(contact)
        # submit contact creation
        #wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        wd.find_element_by_name("submit").click()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.type("firstname", contact.Firstname)
        self.type("middlename", contact.Middlename)
        self.type("lastname", contact.Lastname)
        self.type("nickname", contact.Nickname)
        self.type("title", contact.Title)
        self.type("company", contact.Company)
        self.type("address", contact.Address)
        self.type("home", contact.Home)
        self.type("mobile", contact.Mobile)
        self.type("work", contact.Work)
        self.type("fax", contact.Fax)
        self.type("email", contact.Email)
        self.type("email2", contact.Email2)
        self.type("email3", contact.Email3)
        self.type("homepage", contact.Homepage)
        self.type("bday", contact.Bday)
        self.type("bmonth", contact.Bmonth)
        self.type("byear", contact.Byear)
        self.type("aday", contact.Aday)
        self.type("amonth", contact.Amonth)
        self.type("ayear", contact.Ayear)
        self.type("address2", contact.Address2)
        self.type("phone2", contact.Phone2)
        self.type("notes", contact.Notes)


    def type(self, fild_name, text):
        wd = self.app.wd
        if fild_name is 'bday':
             if text is not None:
                 wd.find_element_by_name(fild_name).click()
                 wd.find_element_by_name(fild_name).is_selected()
                 wd.find_element_by_name(fild_name).send_keys(text)
        elif fild_name is 'bmonth':
             if text is not None:
                 wd.find_element_by_name(fild_name).click()
                 wd.find_element_by_name(fild_name).is_selected()
                 wd.find_element_by_name(fild_name).send_keys(text)
        elif fild_name is 'aday':
             if text is not None:
                 wd.find_element_by_name(fild_name).click()
                 wd.find_element_by_name(fild_name).is_selected()
                 wd.find_element_by_name(fild_name).send_keys(text)
        elif fild_name is 'amonth':
             if text is not None:
                 wd.find_element_by_name(fild_name).click()
                 wd.find_element_by_name(fild_name).is_selected()
                 wd.find_element_by_name(fild_name).send_keys(text)
        else:
            if text is not None:
                wd.find_element_by_name(fild_name).click()
                wd.find_element_by_name(fild_name).clear()
                wd.find_element_by_name(fild_name).send_keys(text)

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_contact_page()
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()


    #def edit_first_contact(self, contact):
      #  wd = self.app.wd
      #  self.open_contact_page()
        # select first contact
      #  wd.find_element_by_name("selected[]").click()
        # edit contact
      #  wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        # edit contact form
      #  wd.find_element_by_name("firstname").click()
       # wd.find_element_by_name("firstname").clear()
       # wd.find_element_by_name("firstname").send_keys(contact.Firstname)
      #  wd.find_element_by_name("middlename").click()
       # wd.find_element_by_name("middlename").clear()
      #  wd.find_element_by_name("middlename").send_keys(contact.Middlename)
       # wd.find_element_by_name("lastname").click()
      # wd.find_element_by_name("lastname").send_keys(contact.Lastname)
       # wd.find_element_by_name("nickname").click()
       # wd.find_element_by_name("nickname").clear()
       # wd.find_element_by_name("nickname").send_keys(contact.Nickname)
      #  wd.find_element_by_name("title").click()
       # wd.find_element_by_name("title").clear()
       # wd.find_element_by_name("company").click()
       # wd.find_element_by_name("company").clear()
       # wd.find_element_by_name("company").send_keys(contact.Company)
       # wd.find_element_by_name("address").click()
       # wd.find_element_by_name("address").clear()
       # wd.find_element_by_name("address").send_keys(contact.Address)
       # wd.find_element_by_name("home").click()
       # wd.find_element_by_name("home").clear()
       # wd.find_element_by_name("home").send_keys(contact.Home)
       # wd.find_element_by_name("mobile").click()
       # wd.find_element_by_name("mobile").clear()
       # wd.find_element_by_name("mobile").send_keys(contact.Mobile)
       # wd.find_element_by_name("work").click()
       # wd.find_element_by_name("work").clear()
       # wd.find_element_by_name("work").send_keys(contact.Work)
       # wd.find_element_by_name("fax").click()
       # wd.find_element_by_name("fax").clear()
       # wd.find_element_by_name("fax").send_keys(contact.Fax)
       # wd.find_element_by_name("email").click()
       # wd.find_element_by_name("email").clear()
       # wd.find_element_by_name("email").send_keys(contact.Email)
       #wd.find_element_by_name("email2").click()
       # wd.find_element_by_name("email2").clear()
       # wd.find_element_by_name("email2").send_keys(contact.Email2)
       # wd.find_element_by_name("email3").click()
       # wd.find_element_by_name("email3").clear()
       # wd.find_element_by_name("email3").send_keys(contact.Email3)
       # wd.find_element_by_name("homepage").click()
       # wd.find_element_by_name("homepage").clear()
       # wd.find_element_by_name("homepage").send_keys(contact.Homepage)
       # wd.find_element_by_name("bday").click()
       # wd.find_element_by_name("bday").is_selected()
       # wd.find_element_by_name("bday").send_keys(contact.Bday)
       # wd.find_element_by_name("bmonth").click()
       ## wd.find_element_by_name("bmonth").send_keys(contact.Bmonth)
       # wd.find_element_by_name("byear").click()
       # wd.find_element_by_name("byear").clear()
       # wd.find_element_by_name("byear").send_keys(contact.Byear)
       # wd.find_element_by_name("aday").click()
       # wd.find_element_by_name("aday").is_selected()
       # wd.find_element_by_name("aday").send_keys(contact.Aday)
       # wd.find_element_by_name("amonth").click()
       # wd.find_element_by_name("amonth").is_selected()
       # wd.find_element_by_name("amonth").send_keys(contact.Amonth)
       # wd.find_element_by_name("ayear").click()
       # wd.find_element_by_name("ayear").clear()
       # wd.find_element_by_name("ayear").send_keys(contact.Ayear)
       # wd.find_element_by_name("address2").click()
       # wd.find_element_by_name("address2").clear()
       # wd.find_element_by_name("address2").send_keys(contact.Address2)
       # wd.find_element_by_name("phone2").click()
       # wd.find_element_by_name("phone2").clear()
       # wd.find_element_by_name("phone2").send_keys(contact.Phone2)
        #wd.find_element_by_name("notes").click()
       # wd.find_element_by_name("notes").clear()
       # wd.find_element_by_name("notes").send_keys(contact.Notes)
        # submit edit contact
       # wd.find_element_by_name("update").click()
        #self.return_home_page()


    def open_contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("http://localhost/addressbook/") and wd.find_element_by_id("search-az")):
           wd.find_element_by_link_text("home").click()

    def return_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def count(self):
        wd = self.app.wd
        self.open_contact_page()
        return len(wd.find_elements_by_name("selected[]"))


    def modify_first_contact(self, new_contact_data):
         wd = self.app.wd
         self.open_contact_page()
         self.select_first_contact()
        # open modification form
         wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        # fill contact form
         self.fill_contact_form(new_contact_data)
       # submit modification
         wd.find_element_by_name("update").click()
         self.return_home_page()


    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

