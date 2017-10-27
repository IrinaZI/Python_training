from sys import maxsize
class Contact:

    def __init__(self, Firstname=None, Middlename=None, Lastname=None, Nickname=None, Title=None, Company=None, Address=None, Home=None, Mobile=None, Work=None,
                       Fax=None, Email=None, Email2=None, Email3=None, Homepage=None, Bday=None, Bmonth=None, Byear=None, Aday=None, Amonth=None, Ayear=None, Address2=None, Phone2=None,
                       Notes=None, id=None, all_phones_from_home_page=None, all_address_from_home_page=None, all_emails=None):
        self.Firstname = Firstname
        self.Middlename = Middlename
        self.Lastname = Lastname
        self.Nickname = Nickname
        self.Title = Title
        self.Company = Company
        self.Address = Address
        self.Home = Home
        self.Mobile = Mobile
        self.Work = Work
        self.Fax = Fax
        self.Email = Email
        self.Email2 = Email2
        self.Email3 = Email3
        self.Homepage = Homepage
        self.Bday = Bday
        self.Bmonth = Bmonth
        self.Byear = Byear
        self.Aday = Aday
        self.Amonth = Amonth
        self.Ayear = Ayear
        self.Address2 = Address2
        self.Phone2 = Phone2
        self.Notes = Notes
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_address_from_home_page = all_address_from_home_page
        self.all_emails=all_emails

    def __eq__(self, other):
           return (self.id is None or other.id is None or self.id == other.id) and self.Firstname == other.Firstname and self.Lastname == other.Lastname

    def __repr__(self):
        return "%s:%s;%s" % (self.Firstname, self.Lastname, self.Middlename)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
