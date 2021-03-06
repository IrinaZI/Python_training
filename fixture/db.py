import mysql.connector
from model.group import Group
from model.contact import Contact
from model.relation import Relation


class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection =  mysql.connector.connect(host=host, database = name, user = user, password = password)
        self.connection.autocommit = True


    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list" )
            for row in cursor:
                (id,name,header,footer) = row
                list.append(Group (id=str(id), name = name, header = header, footer = footer))
        finally:
            cursor.close()
        return list


    def get_relations_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute('select id, group_id from address_in_groups')
            for row in cursor:
                (id, group_id) = row
                list.append(Relation(id=id, group_id=group_id))
        finally:
            cursor.close()
        return list


    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, home, mobile, work, phone2, email, email2, email3 from addressbook where deprecated = '0000-00-00 00:00:00'" )
            for row in cursor:
                (id, firstname, lastname, address, home, mobile, work, phone2, email, email2, email3) = row
                list.append(Contact(id=str(id), Firstname=firstname , Lastname=lastname, Address=address, Home=home, Mobile=mobile,
                                    Work=work, Phone2=phone2, Email=email, Email2=email2, Email3=email3))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()